from threading import Thread

import pytest

import diaper

# Might as well overengineer the tests while we're in here...


@pytest.fixture
def clean_diaper():
    diaper.change()


@pytest.fixture
def dirty_diaper():
    diaper.soil()


def explode():
    raise Exception("I exploded and you'll never find out about it!")


def explode_and_report(store, *args, **kwargs):
    # stash the args so we can see that this got called after the fact
    store['args'] = args
    store['kwargs'] = kwargs
    explode()


def test_diaper_methods(clean_diaper):
    diaper.soil()
    assert diaper.smelly
    diaper.change()
    assert not diaper.smelly


def test_diaper_callable(clean_diaper):
    store = {}
    diaper(explode_and_report, store, 'arg', key='value')
    assert diaper.smelly
    assert 'arg' in store['args']
    assert store['kwargs'] == {'key': 'value'}


def test_diaper_context_manager(clean_diaper):
    store = {}
    with diaper as d:
        explode_and_report(store, 'arg', key='value')
    assert d is diaper
    assert diaper.smelly
    assert 'arg' in store['args']
    assert store['kwargs'] == {'key': 'value'}


def test_change_diaper(dirty_diaper):
    # new diapers should be clean
    diaper.change()
    assert not diaper.smelly


def test_diaper_autochange_func(dirty_diaper):
    # we should always start with a fresh diaper
    diaper(lambda: None)
    assert not diaper.smelly


def test_diaper_autochange_cm(dirty_diaper):
    with diaper:
        pass
    assert not diaper.smelly


def test_diaper_smell_func(clean_diaper):
    # If the diaper caught something, it should be smelly
    diaper(lambda: None[0])
    assert diaper.smelly


def test_diaper_smell_cm(clean_diaper):
    with diaper:
        raise Exception
    assert diaper.smelly


def test_diaper_threadsafe(clean_diaper):
    # diaper soiled in foreign thread is not smelly in main thread
    Thread(target=diaper, args=(explode,)).start()
    assert not diaper.smelly


def test_diaper_foreign_thread_explosions(clean_diaper):
    # use a mutable type to make it relatively easy to alter in a thread
    diaper_smelliness_in_thread = []

    # diaper soiled in foreign thread is not smelly in another foreign thread
    def smelly_in_thread():
        try:
            diaper.smelly
        except AttributeError:
            diaper_smelliness_in_thread.append(True)

    Thread(target=diaper, args=(explode,)).start()
    Thread(target=smelly_in_thread).start()

    assert not diaper_smelliness_in_thread, 'diaper in thread exploded on smelliness check'

import diaper

def explode_and_report(store, *args, **kwargs):
    # stash the args so we can see that this got called after the fact
    store['args'] = args
    store['kwargs'] = kwargs
    raise Exception("I exploded and you'll never find out about it!")


def test_callable():
    store = {}
    diaper(explode_and_report, store, 'arg', key='value')
    assert 'arg' in store['args']
    assert store['kwargs'] == {'key': 'value'}


def test_context_manager():
    store = {}
    with diaper:
        explode_and_report(store, 'arg', key='value')
    assert 'arg' in store['args']
    assert store['kwargs'] == {'key': 'value'}

from Lists import Lists


def test_insert():
    """insert(x,y) integer x at position y"""
    l = Lists()
    l.insert('algo', 0)
    l.insert('banana', 1)
    assert l.at(1) == 'banana'
    
    
from Lists import Lists


def test_insert():
    """insert(x,y) insert x at position y"""
    l = Lists()
    l.insert('algo', 0)
    l.insert('banana', 1)
    assert l.at(1) == 'banana'
 

def test_remove():
    """remove(element) delete first ocurrence of element"""
    l = Lists()
    l.insert('algo', 0)
    l.insert('banana', 1)
    l.remove('algo')
    assert l.at(0) == 'banana'
    

def test_append():
    """append(e) insert e at the end of the list"""
    l = Lists()
    l.append('algo')
    assert l.at(0) == 'algo'
    l.append('banana')
    assert l.at(1) == 'banana'


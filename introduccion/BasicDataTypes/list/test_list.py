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


def test_sort():
    """sort list"""
    l = Lists()
    l.append(5)
    l.append(2)
    l.append(1)
    l.append(9)
    l.append(4)
    l.sort()
    assert l.at(0) == 1
    assert l.at(1) == 2
    assert l.at(2) == 4
    assert l.at(3) == 5
    assert l.at(4) == 9


def test_pop():
    """pop the last element from the list"""
    l = Lists()
    l.append(2)
    l.append(3)
    l.append(5)
    assert l.pop() == 5
    assert l.pop() == 3


def test_print(capsys):
    """reverse the orden of the list"""
    l = Lists()
    l.append(2)
    l.append(3)
    l.append(5)
    l.to_print()
    stout, sterr = capsys.readouterr()
    assert '[2, 3, 5]\n' == stout
 
def test_reverse():
    """reverse the orden of the list"""
    l = Lists()
    l.append(2)
    l.append(3)
    l.append(5)
    l.reverse()
    assert l.at(0) == 5
    assert l.at(1) == 3
       

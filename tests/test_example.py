from pylenium.driver import Pylenium


from cal import calcu

def test():
    assert calcu(2+8+9+3+7)==29

def test():
    assert calcu(7-5*6/3)==4

def test():
    assert calcu(5+2/3-1*2)==2.66

def test():
    assert calcu(6*5*5-5/5)==29
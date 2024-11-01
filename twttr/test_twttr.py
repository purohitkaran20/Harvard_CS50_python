from twttr import shorten

def test_shorten():
    assert shorten('Karan PUROHIT') == 'Krn PRHT'
    assert shorten('123abc456') == '123bc456'

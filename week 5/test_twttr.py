from twttr import shorten
import pytest

def main():
    test_upper_lower_case()
    test_num()
    
    




    
def test_upper_lower_case():
    assert shorten("SAJJAD")=="SJJD"
    assert shorten("sajjad")=="sjjd"
    assert shorten("SAJjad")=="SJjd"
def test_num():
    assert shorten("Sajjad,u.123") == "Sjjd,.123"





if __name__=="__main__":
    main()




from bank import value

def main():
    test_hello()


def test_hello():
    assert value("hello,karim")== "0$"
    assert value("hello,")== "0$"
    assert value("hello")== "0$"



if __name__  == "__main__":
    main()




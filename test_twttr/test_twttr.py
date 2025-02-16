from twttr import shorten

def main():
    test_shorten()
    test_shorten_ponctuation()
    test_shorten_numbers()
    test_shorten_cap()

def test_shorten():
    assert shorten("Something") == "Smthng"

def test_shorten_ponctuation():
    assert shorten("!@#$%^&") == "!@#$%^&"

def test_shorten_numbers():
    assert shorten("123456789") == "123456789"

def test_shorten_cap():
    assert shorten("EXCELENT") == "XCLNT"

if __name__ == "__main__":
    main()



from bank import value

def main():
    test_value_0()
    test_value_20()
    test_value_100()

def test_value_0():
    assert value("Hello") == "$0"

def test_value_20():
    assert value("Hey") == "$20"

def test_value_100():
    assert value("What's happening ?") == "$100"

if __name__ == "__name__":
    main()

    
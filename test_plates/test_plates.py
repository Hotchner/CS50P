from plates import is_valid

def main():
    test_is_valid()


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("12THT") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("##  AAA") == False
    assert is_valid("111111") == False

if __name__ == "__main__":
    main()

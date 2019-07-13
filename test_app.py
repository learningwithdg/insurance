from dummy import is_prime, sumof

def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)

def test_sumof():
    assert sumof(1) == 2
    assert sumof(2) == 4
    assert sumof(3) == 6
    assert sumof(4) == 8
    assert sumof(5) == 10

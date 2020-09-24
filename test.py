import scramble as s


def test_single_letters():
    assert s.scramble("a") == "a"
    assert s.scramble("a b c") == "a b c"


def test_two_letters():
    assert s.scramble("at") == "at"
    assert s.scramble("go to of") == "go to of"


def test_three_letters():
    assert s.scramble("you") == "you"
    assert s.scramble("can you sit") == "can you sit"


def test_four_letters():
    assert s.scramble("read") in ["raed"]
    assert s.scramble("type") in ["tpye"]


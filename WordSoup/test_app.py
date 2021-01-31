import app

def test_no_match_setCheck():
    text_input = 'abq'
    soup_bowl = 'abcdef'
    assert app.setCheck(text_input, soup_bowl)==False

def test_match_setCheck():
    text_input = 'aaaaaaaaaaa'
    soup_bowl = 'xzcvvzzxvvca'
    assert app.setCheck(text_input, soup_bowl)==True

def test_checkForMatch():
    text_input = 'ab'
    soup_bowl = 'abc'
    assert app.checkForMatch(text_input, soup_bowl) == True

def test_not_enough_checkForMatch():
    text_input = 'abbbb'
    soup_bowl = 'ab'
    assert app.checkForMatch(text_input, soup_bowl) == False

def test_no_match_fullCheck():
    text_input = 'aeiou12333333'
    soup_bowl = 'aeiou123'
    assert app.fullCheck(text_input, soup_bowl) == False

def test_match_fullCheck():
    text_input = 'aeiou1233'
    soup_bowl = 'aeiou1233xxz'
    assert app.fullCheck(text_input, soup_bowl) == True

def test_match_LARGE_fullCheck():
    text_input = 'abc'
    soup_bowl = f"{'xzxzxz'*100000}{text_input}"
    assert app.fullCheck(text_input, soup_bowl) == True

def test_no_match_LARGE_fullCheck():
    text_input = 'abcc'
    soup_bowl = f"{'xzxzxz'*100000}abc"
    assert app.fullCheck(text_input, soup_bowl) == False
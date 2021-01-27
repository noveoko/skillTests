import app

def test_find():
    text_input = 'abc'
    text_bowl = 'qqqqqqqqqqqqqqqaqqqqqqqbqqqqqqqqc'
    assert app.find(text_input, text_bowl) == False
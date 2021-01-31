def setCheck(text_input, soup_bowl):
    #check if sets of inputs contain min chars required
    inputSet = set([a for a in text_input])
    soupSet = set([a for a in soup_bowl])
    if len(inputSet-soupSet)==0:
        return True
    else:
        return False

def checkForMatch(text_input, soup_bowl):
    input_chars = {a:text_input.count(a) for a in text_input}
    soup_chars = {a:0 for a in text_input}
    char_keys = input_chars.keys()
    while input_chars != soup_chars:
        for char in soup_bowl:
                if char in char_keys:
                    soup_chars[char]+=1
        if input_chars == soup_chars:
            return True
        else:
            return False

def fullCheck(text_input,soup_bowl):
    if setCheck(text_input, soup_bowl)==True:
        if checkForMatch(text_input, soup_bowl) == True:
            return True
        else:
            return False

if __name__ ==  "__main__":
    pass
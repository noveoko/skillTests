import random

def find(text_input, text_bowl):
    key = {letter:text_input.count(letter) for letter in text_input}
    letters = set(text_input)
    bowl_key = {}
    while bowl_key != key:
        for letter in text_bowl:
            if letter in letters:
                try:
                    if letter not in key.keys():
                        bowl_key[letter]=1
                    else:
                        bowl_key[letter]+=1
                except Exception as ee:
                    print(ee)
    return key == bowl_key
    

if __name__ ==  "__main__":
    pass
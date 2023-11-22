import json
from difflib import get_close_matches

data = json.load(open("data.json"))
# print(data)

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead?" %get_close_matches(word,data.keys())[0])
        opt=input("Please enter Yes(Y)/No(N):")
        if opt.lower()=='y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "please check once and enter again"
    else:
        return "Sorry there is no such a word %s" %word




word=input("Enter the word:")
print(translate(word))
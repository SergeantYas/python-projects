def morse(c, in_alpha):
    if in_alpha == True:
        if c == "a": return ".-"
        elif c == "b": return "-..."
        elif c == "c": return "-.-."
        elif c == "d": return "-.."
        elif c == "e": return "."
        elif c == "f": return "..-."
        elif c == "g": return "--."
        elif c == "h": return "...."
        elif c == "i": return ".."
        elif c == "j": return ".---"
        elif c == "k": return "-.-"
        elif c == "l": return ".-.."
        elif c == "m": return "--"
        elif c == "n": return "-."
        elif c == "o": return "---"
        elif c == "p": return ".--."
        elif c == "q": return "--.-"
        elif c == "r": return ".-."
        elif c == "s": return "..."
        elif c == "t": return "-"
        elif c == "u": return "..-"
        elif c == "v": return "...-"
        elif c == "w": return ".--"
        elif c == "x": return "-..-"
        elif c == "y": return "-.--"
        elif c == "z": return "--.."
        elif c == "1": return ".----"
        elif c == "2": return "..---"
        elif c == "3": return "...--"
        elif c == "4": return "....-"
        elif c == "5": return "....."
        elif c == "6": return "-...."
        elif c == "7": return "--..."
        elif c == "8": return "---.."
        elif c == "9": return "----."
        elif c == "0": return "-----"
        elif c == "/": return "-..-."
        else: return c
    else:
        if c == ".-": return "a"
        elif c == "-...": return "b"
        elif c == "-.-.": return "c"
        elif c == "-..": return "d"
        elif c == ".": return "e"
        elif c == "..-.": return "f"
        elif c == "--.": return "g"
        elif c == "....": return "h"
        elif c == "..": return "i"
        elif c == ".---": return "j"
        elif c == "-.-": return "k"
        elif c == ".-..": return "l"
        elif c == "--": return "m"
        elif c == "-.": return "n"
        elif c == "---": return "o"
        elif c == ".--.": return "p"
        elif c == "--.-": return "q"
        elif c == ".-.": return "r"
        elif c == "...": return "s"
        elif c == "-": return "t"
        elif c == "..-": return "u"
        elif c == "...-": return "v"
        elif c == ".--": return "w"
        elif c == "-..-": return "x"
        elif c == "-.--": return "y"
        elif c == "--..": return "z"
        elif c == ".----": return "1"
        elif c == "..---": return "2"
        elif c == "...--": return "3"
        elif c == "....-": return "4"
        elif c == ".....": return "5"
        elif c == "-....": return "6"
        elif c == "--...": return "7"
        elif c == "---..": return "8"
        elif c == "----.": return "9"
        elif c == "-----": return "0"
        elif c == "-..-.": return "/"
        elif c == "/": return " "
        else: return c

def audio(m):
    for i in m:
        if i == ".": playsound("dot.wav")  
        elif i == "-": playsound("dash.wav")
        elif i == " ": pass
        else: audio(morse(invalid, False))

from playsound import playsound
import time, random
invalid = "......"

def translate(s):
    in_alpha = False
    for i in s:
        if i.isalpha() or i in [0,1,2,3,4,5,6,7,8,9]:
            in_alpha = True
    if in_alpha == True:
        for i in s:
            i = i.lower()
            if i != " ": print(morse(i, in_alpha), end=" "); audio(morse(i, in_alpha))
            else: print(" /  ", end=""); time.sleep(1)
            time.sleep(1)
    else:
        s = s.split(" ")
        for i in s:
            if " " in i: # deal with spaces between words
                i = "".join(i.split(" ")[-1])
                print(" ", end="")
            print(morse(i, in_alpha), end="")
    u = input()
    
def silent_translate(s):
    in_alpha = False
    for i in s:
        if i.isalpha() or i in [0,1,2,3,4,5,6,7,8,9]:
            in_alpha = True
    if in_alpha == True:
        for i in s:
            i = i.lower()
            if i != " ": print(morse(i, in_alpha), end=" ")
            else: print(" /  ", end="")
    else:
        s = s[:-1].split(" ")
        for i in s:
            if " " in i: # deal with spaces between words
                i = "".join(i.split(" ")[-1])
                print(" ", end="")
            print(morse(i, in_alpha), end="")
    u = input()
        
def learn():
    diff = ""
    while diff not in [1,2,3,4,5]:
        diff = int(input("Difficulty (easy = 1) (1-5): "))
        
    if diff == 1:
        while True: # audio + text 1 word
            letter = chr(random.randint(0,25) + ord("a"))
            translate(letter)
            if input(": ") == letter: print("Correct")
            else: print("Incorrect:", letter)
            time.sleep(2)
            
    elif diff == 2: # audio + text 1 word
        with open("common 1000 words.txt", "r") as f:
            word_list = f.read().split("\n")
        while True:
            word = random.choice(word_list)
            translate(word)
            if input(": ") == word: print("Correct")
            else: print("Incorrect:", word)
            time.sleep(3)
            
    elif diff == 3: # audio 1 word
        with open("common 1000 words.txt", "r") as f:
            word_list = f.read().split("\n")
        while True:
            word = random.choice(word_list)
            for i in word:
                audio(morse(i, True))
                time.sleep(1)
            if input(": ") == word: print("Correct")
            else: print("Incorrect:", word)
            time.sleep(3)
    
    elif diff == 4: # audio 1 phrase
        with open("common 1000 words.txt", "r") as f:
            word_list = f.read().split("\n")
        phrase = []
        for i in range(random.randint(3,8)):
            word = random.choice(word_list)
            if word not in phrase: phrase.append(word)
        phrase = " ".join(phrase)
        while True:
            for i in phrase:
                audio(morse(i, True))
                time.sleep(1)
            if input(": ") == phrase: print("Correct")
            else: print("Incorrect:", phrase)
            time.sleep(5)
    elif diff == 5: # audio 1 sentance 
        with open("common 1000 words.txt", "r") as f:
            word_list = f.read().split("\n")
        sentance = []
        for i in range(random.randint(5,13)):
            word = random.choice(word_list)
            if word not in sentance: sentance.append(word)
        sentance = " ".join(sentance)
        while True:
            for i in sentance:
                audio(morse(i, True))
                time.sleep(1)
            if input(": ") == sentance: print("Correct")
            else: print("Incorrect:", sentance)
            time.sleep(5)

inp = ""
while inp not in ["t", "T", "l", "L"]:
    inp = input("Translate or learn? (t/l): ")
    
if inp in ["t", "T"]:
    yn = ""
    while yn not in ["y", "n"]:
        yn = input("Audio (slow) (if appliable), yes or no? (y/n): ")
    if yn == "y":
        translate(input("Message: "))
    else:
        silent_translate(input("Message: "))
else: learn()
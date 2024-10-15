def main():
    path_in = input("Please enter path to yout text file: ")
    print(type(path_in))

    #path_in = None

    if path_in == None or path_in == "":
        in_path = "./books/frankenstein.txt"
        print("Please provide a text file. Have Frankenstein instead:")

    print("_START_\n")

    text = read_text(in_path)
    print(f"{nice_path(in_path)} contained {word_count(text)} words.")

    print("It had this many letters:")
    letters = sort_letters(letter_count(text))
    print(nice_letters(letters))

    print("\n_END_")

def read_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    words = string.split()
    return len(words)

def letter_count(string): #count the letters in the string case-sensitive, then merge upper and lower case
    list = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0
    }
    
    for letter in string:
        if letter in list:
            #print(letter)
            list[letter] += 1
    letter_count = { # sum upper and lower case. Not very elegant, I know
        "a": list["A"] + list["a"],
        "b": list["B"] + list["b"],
        "c": list["C"] + list["c"],
        "d": list["D"] + list["d"],
        "e": list["E"] + list["e"],
        "f": list["F"] + list["f"],
        "g": list["G"] + list["g"],
        "h": list["H"] + list["h"],
        "i": list["I"] + list["i"],
        "j": list["J"] + list["j"],
        "k": list["K"] + list["k"],
        "l": list["L"] + list["l"],
        "m": list["M"] + list["m"],
        "n": list["N"] + list["n"],
        "o": list["O"] + list["o"],
        "p": list["P"] + list["p"],
        "q": list["Q"] + list["q"],
        "r": list["R"] + list["r"],
        "s": list["S"] + list["s"],
        "t": list["T"] + list["t"],
        "u": list["U"] + list["u"],
        "v": list["V"] + list["v"],
        "w": list["W"] + list["w"],
        "x": list["X"] + list["x"],
        "y": list["Y"] + list["y"],
        "z": list["Z"] + list["z"]
    }

    return letter_count

def nice_letters(dictionary):
    nice_text = ""
    for item in dictionary:
        nice_text += f"{item} {dictionary[item]}\n"
    nice_text = nice_text[:-2] #truncate last new line command
    return nice_text

def sort_letters(dict):
    sorted_dict = {}
    sort_order = sorted(dict, key=dict.get, reverse=True)
    for letter in sort_order:
        sorted_dict[letter] = dict[letter]
    return (sorted_dict)

def nice_path(path):
    length = len(path)
    last_slash = path[::-1].find("/")
    nice_path = path[length-last_slash:length]
    return nice_path

main()
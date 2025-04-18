import sys

from stats import word_count, letter_count, nice_letters, sort_letters

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    in_path = sys.argv[1]

    print("_START_\n")

    text = try_path(in_path)
    print(f"{nice_path(in_path)} contained {word_count(text)} words.")

    print("It had this many letters:")
    letters = sort_letters(letter_count(text))
    print(nice_letters(letters))

    print("\n_END_")

def read_text(path):
    with open(path) as f:
        return f.read()

def nice_path(path):
    length = len(path)
    last_slash = path[::-1].find("/")
    nice_path = path[length-last_slash:length]
    return nice_path

def try_path(in_path):
    try:
        read_text(in_path)
        return read_text(in_path)
    except FileNotFoundError:
        print("No such file found. Sorry. Have Frankenstein instead:")
    return read_text("./books/frankenstein.txt")

main()
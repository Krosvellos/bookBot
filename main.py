

def main() :
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        words = file_contents.split()
        count = 0
        for word in words: 
            count = count + 1
        print(count)
        character_count(file_contents)

def character_count(file_contents) :
    dictionary = {}
    myString = file_contents.lower()
    for character in myString :
        if character in dictionary :
            dictionary[character] += 1
        else: dictionary[character] = 1
    print(dictionary)

main()


def main() :
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

        words = file_contents.split()
        count = 0
        for word in words: 
            count = count + 1
        print(f"{count} words found in the document")
        character_count(file_contents)

def sort_on(dictionaries) :
    return dictionaries[1]

def character_count(file_contents) :
    dictionary = {}
    dictionaries = []
    myString = file_contents.lower()
    for character in myString :
        if character in dictionary :
            dictionary[character] += 1
        else: dictionary[character] = 1
    items = list(dictionary.items())
    items.sort(key=lambda item: item[1], reverse=True)
    
    print("--- Begin report of books/frankenstein.txt ---")
    for character,count in items :
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

main()
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Split into words and count them
    words = file_contents.split()
    # print(f"{len(words)}")
    
    letters = charCounts(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    for letter, count in letters.items():
        print(f"The '{letter} character was found {count} times.")
    print("--- End report ---")

def charCounts(bText: str):
    bText=bText.lower()

    charDict = {}
    for char in bText:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    return charDict

main()
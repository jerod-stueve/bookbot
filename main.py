def main():
    with open("books/frankenstein.txt") as f:
        fileContents = f.read()
        # print(fileContents)

        countWords(fileContents)
        countLetters(fileContents)

def countWords(book):
    wordCount = 0
    words = book.split()

    for i in range(0, len(words)):
        wordCount += 1

    print()
    print(f"Word Count: {wordCount}")

def countLetters(book):
    lowerCaseBook = book.lower()
    words = lowerCaseBook.split()

    charCounts = {}

    for word in words:
        for char in word:
            if char in charCounts:
                charCounts[char] += 1
            else:
                charCounts.update({char: 1})

    print(charCounts)
            
main()
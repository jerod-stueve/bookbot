def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        fileContents = f.read()
        # print(fileContents)

        wordCount = countWords(fileContents)
        charCount = countLetters(fileContents)
        createReport(book, charCount, wordCount)

def countWords(book):
    wordCount = 0
    words = book.split()

    for i in range(0, len(words)):
        wordCount += 1

    return wordCount

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

    return(charCounts)

            
def  createReport(book, charCounts, wordCount):
    charCountList = list(charCounts.items())
    charCountList.sort(key=lambda x: x[1], reverse=True)

    print(f"--- Begin report of {book} ---")
    print(f"{wordCount} words found in the document")
    print()
    for char in charCountList:
        if char[0].isalpha():
           print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")


main()

f = open("469 books.txt", "r")
books = f.readlines()

#creates the first iteration
index = 0
for index in range(len(books)):

    book = books[index]
    sentence = ""
    length = 0
    found = True
    while(found and length < len(book)):
        found = False
        for i in range(len(books)):
            if(i != index):
                if(sentence in books[i]):
                    sentence += book[length]
                    length   += 1
                    found     = True
                    break


    for i in range(len(books)):
        books[i] = books[i].replace(sentence[:-1], " " + sentence[:-1] + " ")

#first iteration done!

#iteratively use the first iteration for finding new things
cut = True
while(cut):
    cut = False
    for index in range(len(books)):
        book = books[index]
        for sentence in book.split():
            if(len(sentence) >= 4):
                for j in range(len(books)):
                    for s in books[j].split():
                        if(sentence in s) and (sentence != s):
                            cut = True
                            books[j] = books[j].replace(sentence, " " + sentence + " ")
                            break
    

for book in books:
    print(book, end='')

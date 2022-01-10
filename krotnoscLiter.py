def countLetters(word):
    temp = []
    word = sorted(word)

    for i in word:
        if i not in temp:
            temp.append(i)

    dict = []
    b = []

    for j in temp:
        n = 0
        for k in word:
            if k == j:
                n+=1
        b.append(n)

    dict.append(temp)
    dict.append(b)

    return dict

def heapify(i, list):
    l = 2 * i+1
    r = 2 * i+2

    largest = i

    if l < len(list[0]) and list[1][l] > list[1][i]:
        largest = l

    if r < len(list[0]) and list[1][r] > list[1][largest]:
        largest = r

    if largest != i:
        list[1][i], list[1][largest] = list[1][largest], list[1][i]
        heapify(largest,list)

def heapSort(list):
    i = len(list[0]) // 2
    while i >= 0:
        heapify(i, list)
        i -= 1

# 0: [a,b,c,d] 1: [1,1,2,3]
def findMinimum(list):
    letter = list[0][0]
    numof = list[1][0]

    for e in list[1]:
        tempindex = 0
        i = 0
        if e <= numof:
            numof = e
            letter = list[0][i]
            tempindex = i
        i+=1

    del list[0][tempindex]
    del list[1][tempindex]

    heapSort(list)
    return letter, numof

def insert(list, key, value):
    list[0].append(key)
    list[1].append(value)
    heapSort(list)

def huffman(word):
    dict = countLetters(word)
    list2 = {}
    while len(dict[0])!=1:
        letter1, numof1 = findMinimum(dict)
        letter2, numof2 = findMinimum(dict)

        if numof1 < numof2:
            name = letter1+letter2
            list2[letter2] = numof2
            list2[letter1] = numof1
            list2[name] = numof1+numof2

        if numof2 < numof1:
            name = letter2 + letter1
            list2[letter1] = numof1
            list2[letter2] = numof2
            list2[name] = numof1 + numof2

        if numof2 == numof1:
            name = letter2 + letter1
            list2[letter1] = numof1
            list2[letter2] = numof2
            list2[name] = numof1 + numof2

        insert(dict, name, numof2+numof1)
    return newDict(list(list2.keys()))

def toBits(letter, list2):
    code = ""
    for key in list2:
        if key != letter:
            if key.startswith(letter):
                letter = key
                code += "0"
            elif key.endswith(letter):
                letter = key
                code += "1"
    return code[::-1]

def newDict(list2):
    dict = {}
    for letter in list2:
        if len(letter) == 1:
            dict[letter] = toBits(letter, list2)
    return dict

def translateToNumbers(word):
    newerdict = huffman(word)
    table = file.maketrans(newerdict)
    translated = file.translate(table)
    return translated

#
with open('word.txt', 'r') as file:
    file = file.read().replace('\n', '')
print(huffman(file))
print(translateToNumbers(file))
print (countLetters(file))

with open('newword.txt', 'w') as f:
    f.write(str(huffman(file)))

with open('huffmanword.txt', 'w') as f:
    f.write((translateToNumbers(file)))


#cos jest nie tak/ huffman nie powinien byc ciezszy
import os
a = os.path.getsize("word.txt")
b = os.path.getsize("newword.txt")
c = os.path.getsize("huffmanword.txt")
print(a)
print(b)
print(c)
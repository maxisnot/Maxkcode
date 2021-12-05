# global variables 

with open("words.txt", mode="r",encoding="utf-8") as words:
    words = words.read()

with open("clues.txt", mode="r",encoding="utf-8") as clues:
    clues = clues.read()
    clues = clues.replace('\n','')

with open("solved.txt", mode="r",encoding="utf-8") as ANS:
    ANS = ANS.read().splitlines()

amm = 0
#splits the list
clueslst = []
for n in clues:
    clueslst.append(n)
    amm += 1

    # items in a list sym to str
    # outputs = ['A', '#', 'M', '*', 'N', '%']
    # now we want a sub list giving of [['A', '#'],['M', '*'],[ 'N', '%']]
    # then we will flip our list making it able to be broken down and used with a 
    # .replace(x,y) this will replave our sym with a str

# take first two terms ona arry then grab last and 1st ittorate this per time you have a  var
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]
even = [0,2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64]
num = 0


for x in range(len(clueslst)):
    
    if num in even:
        y = clueslst[num]
        print(y)  
    elif num in odd:
        x = clueslst[num]
        print(x)
    num += 1
    clueslst = clueslst.replace(y ,x)
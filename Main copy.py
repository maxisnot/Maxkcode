

def clues():
    with open('clues.txt','r') as f:
        print("using the clues including:")
        #for num of line print all in text file
        for line in f:
            print(line, end='')
        #return the statements above  
        f.close()
        return
def words():
    with open('words.txt','r') as w:
        print("using the clues including:")
        #for num of line print all in text file
        for line in w:
            print(line, end='')
        #return the statements above  
        w.close()
        return
    

with open('words.txt','r') as y:
    #word canculator
    with open('words.txt',"r",encoding="utf-8") as my_file:
        n = (sum(1 for _ in my_file))
    m = n

    # M is the math operrator on num of lines in a math op stand point 

#user interfave on tasks
def start():
    print('you will have a random assortment of symbols')
    print('your task is to work out the word made from the sybols.')
    print('you will have {0} of words work out what they are,'.format(m))
    clues()
    print()
    print('for example if A is represented by the symbol #, M by *, and N by %, ')
    print('then the word MANNA would be represented by the symbols *#%%#')
    print('your symbols you will need for this is')
    words()
    ansmaker()

def ansmaker():
    wordslft = m
    score = 0
    with open("solved.txt", mode="r",encoding="utf-8") as my_solved:
        solved = my_solved.read().splitlines()
    write = open("done.txt","w",encoding="utf-8") 
    if score != m:   
        while score != m:
            with open("done.txt","r",encoding="utf-8") as done_r:
                finished_r = done_r.read().splitlines()
            answer = input("enter a term on the list: ")
            if answer in solved:
                wordslft =- 1
                score += 1 
                print("you have {0} right".format(score))
                write.write(answer)
                done_r.close()
            elif answer in finished_r:
                print("you all ready done that")
            else:
                print('thats incorrect')
            
print("welcome to the word game")
begin = input("would you laike to start")

if begin == "yes" or "y":
    listreplace()
    #start()
else :
    print("oh ok i spent time making this")

# contence's
# f = clues.txt
# y = words.txt
# n = num of lines y 
# m = math op for n
# .replace


#this will turn our array into a list we can check for data 

    
    

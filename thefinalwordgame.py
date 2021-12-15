import datetime 
# the final word game by max knight
# date: 
# due : 16/12/2021



"""""""""
Tasks
1.   Develop the part of the program that loads the list of ten coded words from the external file words.txt that your teacher has given you, and displays the content of this file in an appropriate way. Figure 1 shows the content of this file.
2.   Develop the part of the program that loads the three letter and symbol pairings from the external file clues.txt your teacher has given you, and displays the content of the file in an appropriate way. Figure 2 shows the content of this file.
3.   Develop the part of the program that displays the list of ten words with the substitutions made based on the letter and symbol pairings. An example is shown in Figure 3for the substitutions made for the letters A, M and N. 
4.   Develop the part of the program that allows the user to enter a letter and symbol pairing.
    a.   If the letter entered has already been matched to a symbol then they are told that the letter is already matched and they are asked to enter another letter and symbol pairing.
    b.   If the symbol entered has already been matched to a letter then they are told that the symbol is already matched and they are asked to enter another letter and symbol pairing.
5.   Develop the part of the program that allows the user to delete a letter and symbol pairing.
6.   Develop the part of the program that allows Tasks 3, 4 and 5to be repeated continuously until all symbols have been substituted by letters for each word in the list.
7.   Develop the part of the program that checks the users list of words against the external file solved.txt and displays an appropriate success or fail message.  If the puzzle has not been completed correctly, the user should be allowed to continue to try to solve the puzzle or exit the program.
8.   When trying to solve puzzles of this type, it may help the user to know the frequency with which each symbol is used in the code words.  For example, the symbol # is used eight times, * is used four times and % is used four times in the code words shown in Figure 1.
     Extend the program so that it calculates the frequency with which the symbols are used in the code words.  Display the results of this calculation in an appropriate format. 

possible ideas:
1. create a sublist in a area where we can break down cluies .txt and change them into var and eather use a llambder to replace or use a .replace() function appon lists
2. Hard wire make the problem for example make evey term in clues.txt and change this into a var eg.
        a = a
        b = *
        c = c
        d = /
        e = d
        f = &
        words = words.replace(a,b)
        words = words.replace(c,d)
        words = words.replace(e,f)
        print(words)
    apon futher thoughts this wouldasnt be a good idea as our code coudnt be changed for a ind letter and it a bit redudndent
3. write appon a  file 

assumptuions:
1. our clues.txt is always == 3 and never becomes != 3 (e.g. words.txt.appeal() > 3 or words.txt.appeal() < 3) this makes our jopob easyer
2. our user might type in a lower or upper case for this we can eather make a boolian .isupper()/.islower() or we could .upper()/.lower()

nice added bonesses:
1. make a time bar
2. add a grafical user interface(probbibly not though)
3. a menu
4. end if you enter apon ending 
4. point / score sytem

"""""""""
print('This is a puzzle where you must work out what ten words are by cracking the code. Each symbol used in the coded words represents a unique letter...')



#Open and display file with the encrypted words in it and display it
def Read_and_print_words(x):#Bring in 'x', the file name
    # whats a try function except statement can handle exceptions. Exceptions may happen when you run a program.
    # Exceptions are errors that happen during execution of the program. Python won’t tell you about errors like syntax errors (grammar faults), instead it will abruptly stop.
    # An abrupt exit is bad for both the end user and developer.
    # Instead of an emergency halt, you can use a try except statement to properly deal with the problem. An emergency halt will happen if you do not properly handle exceptions.
    try:
        lines=open(x, 'r') 
        words=lines.read() #fomat it
        lines.close() 
        words=words.rstrip() #remove the new lin
    except: #so no run time err
        print('\nThe file:', x, 'could not be found.')
        print('Please make sure that it is in the same folder as this program and that it is a .txt file')
        print('It should be named', x)
        print('Run the program again once you think the problem is fixed...')
        exit(input('Please press enter to end the program...')) #fin the read_and_print_words
    return (words) #Return the file



#Let the user how many clues to choose
def Replace_clues(ten_words):
    (clues)=Read_and_print_words('clues.txt') 
    print('\nHere are the ten words...'), print(ten_words)
    clue_choice=input('\nDo you want 0, 1, 2 or all 3 clues? ') #
    while(clue_choice!='0' and clue_choice!='1' and clue_choice!='2' and clue_choice!='3'): #make shue its in the sattment
        print('Please enter a valid number, from 0-3...') # if incorect print this
        clue_choice=input('\nDo you want 0, 1, 2 or all 3 clues? ') #Ask the user how many cluds
    clue_choice=int(clue_choice)#change into a int for a santax error and to make code simpler
    clues=list(clues) #make list
    clues.remove('\n'), clues.remove('\n') #removes \n to stop newline tag in funct
    symbol_attempts=[] #Create the empty list for sybols
    letter_attempts=[] #Create the empty list words
    for i in range(0,(clue_choice*2), 2):#For the chosen amount of clues that they want...
        # this will take the chosen amount of clues ,then get a letter of the clue (1),get sybols in list(2),show the clues(3)
        # replace letter with sybol (4), add the sybol to the list (5), add the letter to list(6)
        letter=clues[i] # (1)
        symbol=clues[i+1] # (2)
        print(letter, '=', symbol) # (3)
        ten_words=ten_words.replace(symbol, letter) # (4)
        symbol_attempts.append(symbol) # (5)
        letter_attempts.append(letter) # (6)
    if clue_choice!=0:
        print('\nHere are the ten words with the clue(s) in it...'), print(ten_words)#Display the new anount words
    return (ten_words,symbol_attempts,letter_attempts,clue_choice,clues)




#Check if the user's chosen letter has already been entered
def Get_letter_choice(letter_attempts, ten_words, symbol_choice):
    letter_choice=input(str('Please enter the letter that you want to replace it with: '))
    while(len(letter_choice)!=1 or letter_choice.isalpha()==False or letter_choice.title() in letter_attempts):
        print('Please enter a valid, single letter that hasn\'t been entered yet...') 
        letter_choice=input(str('Please enter the letter that you want to replace it with: '))
    letter_attempts.append(letter_choice.upper())
    ten_words=ten_words.replace(symbol_choice,letter_choice.upper()) 
    print('\nHere are the new ten words:'), print(ten_words) # display the new words
    return(ten_words, letter_attempts)



#Check if the user's chosen symbol has already been entered
def Get_symbol_choice(symbol_attempts):
    symbol_choice=input(str('\nPlease enter the symbol that you want to replace: ')) #Allow the user to choose the symbol
    while(len(symbol_choice)!=1 or symbol_choice.isalpha()==True or symbol_choice in symbol_attempts or symbol_choice not in ten_words): #Make sure the user only enters one symbol
        print('\nPlease enter a valid symbol, that is one character and is in the words above...') #Display error message
        symbol_choice=input(str('\nPlease enter the symbol that you want to replace: '))#Allow the user to choose the symbol
    symbol_attempts.append(symbol_choice) 
    return (symbol_choice, symbol_attempts)



#Allow the user to enter a letter and symbol pairing
def Replace_user_choice(ten_words, symbol_attempts, letter_attempts, clue_choice):
    menu_choice='1'#Make sure that the 'while' loop below is carried out
    while(menu_choice.title()=='1' or menu_choice.title()=='2' or menu_choice.title()=='3' or menu_choice.title()=='4'):
        (symbol_choice, symbol_attempts)=Get_symbol_choice(symbol_attempts)
        (ten_words, letter_attempts)=Get_letter_choice(letter_attempts, ten_words, symbol_choice)
        menu_choice=input(str('\n1. Would you like to enter another symbol\t2. Receive a clue\n3. Delete a letter and return it to normal\t4. Get some help\n5. Check answers or stop playing\n'))
        while(menu_choice.title()!='1' and menu_choice.title()!='2' and menu_choice.title()!='3' and menu_choice.title()!='4' and menu_choice.title()!='5'):#Make sure their input is valid
            print('\nPlease enter a valid answer. Enter 1, 2, 3, 4 or 5...\n') 
            menu_choice=input(str('1. Would you like to enter another symbol\t2. Receive a clue\n3. Delete a letter and return it to normal\t\t4. Get some help\n5. Stop playing\n'))
        if menu_choice=='2':#If the user wants to receive an extra clue
            (ten_words,symbol_attempts,letter_attempts)=Extra_clue(ten_words, clue_choice, symbol_attempts, letter_attempts, clues)
        elif menu_choice=='3':#If the user wants to delete
            (ten_words, letter_attempts, symbol_attempts)=Delete_pair(ten_words, letter_attempts, symbol_attempts)
        elif menu_choice=='4':#If the user help
            (frequency)=Help(ten_words, symbol_attempts, letter_attempts, start_time)
    return (ten_words)

def Extra_clue(ten_words, clue_choice, symbol_attempts, letter_attempts, clues):
    if clue_choice==0 or clue_choice==1 or clue_choice==2:
        while clue_choice!=3 and clues[clue_choice*2] in letter_attempts:#Make sure that they haven't mnually entered the clu already
            if clue_choice<3:
                clue_choice+=1
        if clue_choice!=3:
            ten_words=ten_words.replace(clues[clue_choice*2+1], clues[clue_choice*2]) #Substitte the clues in
            print(), print(clues[clue_choice*2], '=', clues[clue_choice*2+1], '\n'), print('Here are the new ten words:'), print(ten_words)
            
            #Give them the clue and display the new ten  words
            letter_attempts.append(clues[clue_choice*2])
            symbol_attempts.append(clues[clue_choice*2+1])
        else:
            print('All of the clues are already in the ten words...')
    elif clue_choice==3:#If they already have all thre of the clues
        print('Your already have all of the clues...') #isplay error message
    return (ten_words,symbol_attempts,letter_attempts)

#low the user to delete a leter and symbol pairing
def Delete_pair(ten_words,letter_attempts,symbol_attempts):
    delete_letter=input('Which letter would you like to return to normal? ')
    while(delete_letter.isalpha()==False or len(delete_letter)!=1 or delete_letter.title() not in letter_attempts):
        print('Please enter a valid, single letter')
        delete_letter=input('Which letter would you like to return to normal? ')
    index_of_letter=letter_attempts.index(delete_letter.title())
    letter_being_removed=letter_attempts.pop(index_of_letter) #Remove the letter from the list of attempts
    symbol_being_replaced=symbol_attempts.pop(index_of_letter) #Remove thesymbofrom the list of ttempts
    ten_words=ten_words.replace(letter_being_removed, symbol_being_replaced)
    print('Here are the new ten words:'), print(ten_words)
    return(ten_words, letter_attempts, symbol_attempts)

#Check if the user's answers are right
def Check_answers(ten_words, start_time):
    again='No'
    ten_words=ten_words.rstrip()
    (solved)=Read_and_print_words('solved.txt')
    if solved!=ten_words: #Check if the user's answers are the same as the corect answers
        again=input('Your answers are incorrect...\nWould you still like to quit the puzzle? ')
        while(again.title()!='Yes' and again.title()!='No'):
            print('Please enter a valid answer: Yes or No\n')
            again=input('Would you still like to quit the puzzle? ')
        if again.title()=='Yes':
            print('\nHere are the solutions'), print(solved)
            end_time=datetime.datetime.now()
            print('\nYou have been', (end_time.minute - start_time.minute) ,'minutes and', (end_time.second - start_time.second), 'seconds')
        elif again.title()=='No':
            print(ten_words)
    elif solved==ten_words:
        print('You are correct!') #Tell them if they are corret
        again='Yes'
        end_time=datetime.datetime.now()
        print('\nYou were', (end_time.minute - start_time.minute) ,'minutes and', (end_time.second - start_time.second), 'seconds')
    return again
#Calclate the frequncy with wich each and tell the user how long they have been
def Help(ten_words, symbol_attempts, letter_attempts, start_time):
    frequency={} #Create an epty dictionary
    for key in ten_words:#Scan through the charaters in the ten words
        if key in frequency:#If that chaacte is alredy in the dictionary
            frequency[key]+=1 
        else:#If that chacter isn't in the dictionar
            frequency[key]=1 #reate a key for that symol in the dictioary
    del frequency['\n'] #Delete the empty one
    loopcounter=0
    for key in frequency:#For every key in the dictionary of symbols
        if frequency[key]==1 and key.isalpha()==False:#Tell the user how manties that symbol is in it
            print(key, 'is in the coded words', frequency[key], 'time')
        elif key.isalpha()==False:
            print(key, 'is in the coded words', frequency[key], 'times')
        loopcounter+=1
    if loopcounter==0:
        print('The frequency cannot be displayed, as all of the symbols have been entered...')
    end_time=datetime.datetime.now() #Create a variable that stores the currenttime
    minutes_taken=end_time.minute - start_time.minute
    seconds_taken=end_time.second - start_time.second
    if seconds_taken<0:
        seconds_taken=seconds_taken*(-1)
    print('\nYou have been', minutes_taken ,'minutes and', seconds_taken, 'seconds') #Tell the  how long they have been
    return frequency

#Run the program
(ten_words)=Read_and_print_words('words.txt')
(ten_words, symbol_attempts, letter_attempts, clue_choice, clues)=Replace_clues(ten_words)
again='No'
start_time=datetime.datetime.now() #Record the start me
while(again.title()=='No'):#While they kee wanting  play
    (ten_words)=Replace_user_choice(ten_words, symbol_attempts, letter_attempts, clue_choice)
    again=Check_answers(ten_words, start_time)
exit(input('Please press enter to end the program...'))
def task1():
    try: 
        1 / 0
    except ZeroDivisionError: 
        print('Divided by zero')

    print('Should reach here')


def fail():
    1 / 0

try:
    fail()
except:
    print('Exception occured')

print('Program continues')
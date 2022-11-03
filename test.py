
def hello():
    a = input('If you agree with me, input "y"')
    if a == 'Y' or 'Yes' or 'YES' or 'y':
        print('Hello, World!')
    elif a == 'N' or 'n' or 'No' or 'NO':
        print('Bye, World!')
    else:
        print('Whats wrong? try again')
        hello()

    

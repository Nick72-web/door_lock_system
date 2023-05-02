#program written by Nick AKA Mr PA
#program to ask user to enter correct password
#after there the user will be required to make decisions making
import datetime
now = datetime.datetime.now()
pswd = 'jkl'
password = input('Enter correct password:')
while password != pswd:
    print('Oooops!!! Try again pliz.')
    password = input('Enter correct password:')
    if password == pswd:
        print("*"*5,"Enter open to open door.","*" * 5)
        print("*"*5,"Enter close to close door.","*" * 5)
        print("*"*5,"Enter quit to terminate the process.","*" * 5)
        
# This acts as function calling
comment = ''
opened = False
closed = False

#use while loop until the condition is met for further execution
while comment != 'quit':
    comment = input('Enter your decision pliz:').lower()
    if comment == 'open':
        if opened:
            print('The door is already opened.')
        else:
            opened = True
            print("The door is opened.")
            print("You have open the door at:", end = "")
            print("*" * 5 , end = '')
            print(now.strftime('%Y-%m-%d %H:%M:%S'), end = '')
            print("*" * 5)        
    elif comment == 'close':
        if closed:
            print("The door is already closed.")
        else:
            closed = True
            print("The door is now closed at:", end = "")
            print("*" * 5 , end = '')
            print(now.strftime('%Y-%m-%d %H:%M:%S') ,end = "")
            print("*" * 5)
    elif comment == 'quit':
        print("Process Terminated Thank You.")
    else:
        print("Invalid Input Please Enter the valid one.")    
        
                     
Interactive Quiz Game
Concept Utilized: Variables, Data Types, Input/Output, Control Flow (if/elif/else), Loops (for or while), Data Structures (Lists for questions/answers, Dictionaries for question-answer mapping), String Handling.
Idea: Create a simple text-based quiz. Store questions and answers, loop through them, take user input, compare answers (case-insensitively), keep score, and provide feedback.
Enhancements: Multiple-choice options, timed questions, difficulty levels, saving high scores.

features 

1- lgin 
2- signup 
3- question 
4- 30 mcq -> question line wise 
5- history + 



Signup()

def signup():
    name=input("Enter Your Name: ")
    user_name=input("Enter Your Username: ")
    while True:
        passcode=input("Enter a 4 digit passcode: ")
        passcode_check=input("Enter the passcode again: ")
        if passcode==passcode_check:
            if len(passcode)<5 and len(passcode) > 0:
                print("Details of user")
                print(name,"\n")
                print(user_name,"\n")
                print(passcode,"\n")
                break
            else:
                print("Length of Password exceeded Try again !!!")
                
        else:
            print("\n")
            print("Passcode didn't match !! \n")
            print("Try again !!")


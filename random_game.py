import random

print("You have to Guess a random no. between two values")

first_no=int(input("Enter First value=  "))
second_no=int(input("Enter second value=  "))



def game(b):
    a=random.randint(first_no,second_no)
    print(f"Turn of Player {b+1}")
    input_value=0
    n=0
    while input_value != a:
        input_value=int(input(f"Guess the no. beetween {first_no} and {second_no}  "))
        if input_value==a:
            print("Congratulaions you guessed it right")
            n=n+1
        elif first_no>input_value or second_no<input_value:
            print(f"You entered out of range value plese enter vlaue in beetween{first_no} and {second_no}")
            n=n+1
        elif input_value>a:
            print("Value is gretar than the actual no. try smaller value")
            n=n+1
        elif input_value<a:
            print("Value is smaller than the actual no. try grater value")
            n=n+1

    print(f"You take {n} guesses and your no was {a}")
    return n

o=game(0)
p=game(1)

if o<p:
    print("Player 1 won")
elif o==p:
    print("Oops its tie")
else:
    print("Player 2 won")

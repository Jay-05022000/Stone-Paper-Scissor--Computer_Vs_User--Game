''' stone,paper,scissors
 you have to develop user vs computer kind of game.where you ask user to give input and then
 compare it with computer generated action and print the result of attempt.also update the score board.
 max attempt is 10 and after that end the game and print winner of game.'''

# variable declaration
i=0
user=0
computer=0

# computer input generation
import random
computer_choices=('stone','paper','scissors')
computer_input=random.choice(computer_choices)

# main loop
while (i<10) :
    user_choices={'s1':'stone','p':'paper','s2':'scissors'}
    user_input=input("s1 for stone,p for paper and s3 for scissors : ")
    # print(user_choices[user_input])
    try:
        if (computer_input=='stone') and (user_choices[user_input]=='stone'):
            print("ohh! its a clash")
            i+=1
        elif (computer_input=='stone') and (user_choices[user_input]=='paper'):
            print('user won!')
            user= user+1
            i+=1
        elif (computer_input == 'stone') and (user_choices[user_input] == 'scissors'):
            print('computer won!')
            computer=computer+1
            i+=1

        if (computer_input=='paper') and (user_choices[user_input]=='paper'):
            print("ohh! its a clash")
            i+=1
        elif (computer_input=='paper') and (user_choices[user_input]=='stone'):
            print('computer won!')
            computer= computer+1
            i+=1
        elif (computer_input == 'paper') and (user_choices[user_input] == 'scissors'):
            print('user won!')
            user=user+1
            i+=1

        if (computer_input=='scissors') and (user_choices[user_input]=='scissors'):
            print("ohh! its a clash")
            i+=1
        elif (computer_input=='scissors') and (user_choices[user_input]=='stone'):
            print('user won!')
            user= user+1
            i+=1
        elif (computer_input == 'scissors') and (user_choices[user_input] == 'paper'):
            print('computer won!')
            computer=computer+1
            i+=1
    except Exception as e:
        print(e)
        break

# result announcement
print(f'computer score: {computer} & your score: {user}')
if (computer>user):
    print('sorry,you loose the game.')
elif (computer<user):
    print("congratulations!you have won the game")
else:
    print('game is tie')

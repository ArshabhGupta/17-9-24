import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {'Apple':'red', 'Mango':'yellow', 'Orange':'orange', 'Watermelon':'green'}
    def Quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_answer = input()
            if user_answer.lower() == color:
                print("The correct answer!")
            else:
                print("Wrong answer!")
            option = int(input("Enter 0 if you want to play again else type 1: "))
            if (option):
                break
print("Welcome to the quiz!")
f1 = FruitQuiz()
f1.Quiz()
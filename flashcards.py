class Flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
Flash = []
print("Welcome to the Flashcard Application")
while True:
    word = input("Enter a word: ")
    meaning = input("Enter the meaning of the word: ")
    Flash.append(Flashcards(word, meaning))
    option = int(input("Enter 0 if you want to another flashcard else type 1: "))
    if (option):
        break
print("Your flashcard: ")
for i in Flash:
    print(">", i)
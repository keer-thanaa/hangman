import random
flowers = [
    "Rose", "Tulip", "Lily", "Daffodil", "Marigold", "Jasmine", "Orchid", "Sunflower", "Daisy", "Hibiscus",
    "Peony", "Lavender", "Lotus", "Poppy", "Camellia", "Chrysanthemum", "Zinnia", "Carnation", "Magnolia", "Geranium"]

sports = [
    "Football", "Basketball", "Cricket", "Tennis", "Badminton", "Volleyball", "Baseball", "Table Tennis", "Hockey", "Golf",
    "Swimming", "Rugby", "Athletics", "Gymnastics", "Boxing", "Wrestling", "Ice Skating", "Cycling", "Archery", "Skateboarding"]

colours = [
    "Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Black", "White", "Grey",
    "Brown", "Cyan", "Magenta", "Maroon", "Indigo", "Turquoise", "Teal", "Gold", "Silver", "Lavender"]

animals = [
    "Lion", "Elephant", "Tiger", "Giraffe", "Zebra", "Kangaroo", "Panda", "Dolphin", "Penguin", "Bear",
    "Rabbit", "Fox", "Wolf", "Horse", "Cow", "Cat", "Dog", "Owl", "Deer", "Monkey"]
print("Heyy user!! Welcome to Hangman")
inp1=input("Choose your genre : flowers/sports/colours/animals:")
if(inp1=='flowers'):
    ans=random_flower = random.choice(flowers).lower()
elif(inp1=='sports'):
    ans=ans=random_flower = random.choice(sports).lower()
elif(inp1=='colours'):
    ans=random_flower = random.choice(colours).lower()
elif(inp1=='animals'):
    ans=random_flower = random.choice(animals).lower()
print("Nice choice")
print("Now guess the word!")
L=[]

for i in range(len(ans)):
    L.append('_')
length=len(L)
for i in L:
    print(i,end=' ')
checker=1
print('\n')
for i in range(len(L)):
    amt=length-i
    amount=str(amt)
    print("You have "+ amount +" guesses left \n")
    guess=input("Enter your guess ").lower()
    for j in range(len(ans)):
        if(guess==ans[j]):
            L[j]=guess
    for k in L:
        print(k,end=' ')
    print('\n')
    guess2=input("Do you want to guess the word?(y/n)")
    if(guess2 in 'Yy'):
        guess3=input("Enter the word:").lower()
        if(guess3==ans):
            print("Congrats! You won!")
            checker=2
            break
        else:
            print("Oops ! thats not right")
            continue
    
if(checker==2 or '_' not in L):
    pass
else:
    print("Sorry you lost")
    print("Your word was " , ans)

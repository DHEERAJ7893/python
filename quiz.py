print("this is online quiz")

playing = input("if you want play yes or no:")

if playing != "yes":
    quit()

print("okay! lets play a game")

question1 = int(input("what is this year?"))
if question1 == 2024:
    print("correct!")
else:
    print("incorrect!")
question2 = input("what is the first month?")
if question2 == "january":
    print("correct!")
else:
    print("incorrect!")
question3 = input("what is the last month?")
if question3 == "december":
    print("correct!")
else:
    print("incorrect!")    
question2 = input("what is special on december 25?")
if question2 == "chrishyesmas":
    print("correct!")
else:
    print("incorrect!")
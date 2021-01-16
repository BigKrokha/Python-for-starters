from random import randint

answers = ("yes", "no", "maybe")
ask = ""
print("Ask!")
while ask != "stop":
    ask = input()
    answer = answers[randint(0,len(answers)-1)]
    print(answer) 
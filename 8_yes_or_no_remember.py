from random import randint

buffer = []
answers = ("yes", "no", "maybe")
answer = ""
ask = ""
print("Ask!")

def already_asked(a):
    for ask, ans in buffer:
        if ask == a:
            global answer 
            answer = ans
            return 1
    return 0

while ask != "stop":
    ask = input()
    if already_asked(ask):
        print(answer)
    else:
        answer = answers[randint(0,len(answers)-1)]
        buffer += [ (ask, answer) ]
        print(answer) 

#Ask!
#a -------- first ask
#maybe
#b -------- first ask
#yes
#a -------- the same
#maybe
#a
#maybe
#a
#maybe
#b -------- the same
#yes
#b
#yes
#b
#yes
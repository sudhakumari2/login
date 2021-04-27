import random
numdigit=5
list2=[]
maxchance=10
def getsecretnum():
    numbers=list(range(10))
    random.shuffle(numbers)
    secretnum=""
    for i in range(numdigit):
        secretnum+=str(numbers[i])
    return secretnum
def getclue(guess,secretnum):
    if guess==secretnum:
        return "you got it"
        list2.append(secretnum)
    clue=[]
    for i in range (len(guess)):
        if guess[i]==secretnum[i]:
            return "bull"
        elif guess[i] in secretnum:
            clue.append("cow")
        elif guess[i] in secretnum:
            clue.append("cow")
        elif guess[i] in secretnum:
            clue.append("cow")
        else:
            clue.append("none")
    return''.join(clue)
def isonlydigit(num):
    if num =='':
        return False
    for i in num:
        if i not in [1,2,3,4,5,6,7,8,9,10]:
            return False
    return True
print("here some clue")
print("bull one digit is correct")
print("cow  no digit is correct ")
while True:
    secretnum=getsecretnum()
    print("i have thought up a number . you have %s guesses to get it." %(maxchance))
    numguesses=1
    while numguesses<=maxchance:
        guess=""
        print("guess",numguesses)
        guess=input("guess again")
        clue=getclue(guess,secretnum)
        print(clue)
        numguesses+=1
        if guess==secretnum:
            break
    print('you ran out of guess the answer was' +secretnum)
    print("do you want to play again yes or no")
    again=input("you want to paly again yes or no")
    if again =="no":
        break
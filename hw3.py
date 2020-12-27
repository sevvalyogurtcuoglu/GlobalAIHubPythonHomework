import random
name=input("please input name : ")
print("Welcome {} :))".format(name))

print("Rules --Z User will be given 8 turns")

words=["python","apple","banana","pear","orange","strawberry","pineapple",
"chocolate","coffee"]

print("Guess the word")
guesses =""
word = random.choice(words)
turns=8
fail=0
while turns>0:
    
    for i in word:
        if i in guesses:
            print(i)
        else:
            print("-")
            fail+=1
    if fail == 0:
        
        print("You Win") 
         
        print("The word is: ", word) 
        break  
          
    guess = input("guess a  character:")     
    guesses += guess 
    if guess==word:
        print("You  winn :) ")
        print("The word is: ", word) 

        break
    if guess not in word:
         
        turns -= 1
    
        print("Wrong")
         
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("You Loose")  
            print("The word is: ", word) 

            break     

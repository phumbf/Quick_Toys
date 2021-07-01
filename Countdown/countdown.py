'''
A fun little toy made while waiting for dinner and 
watching Channel 4's Countdown show.

https://www.channel4.com/programmes/countdown

The basic idea is that two contestants play letters and numbers games to 
rack up the highest score. Letters games involve building the longest word possible 
whilst numbers games involve the two players trying to equal the target number.

The game finishes with a conundrum round which is a 9 letter anagram.

I use a dictionary.txt file to validate words and a similar file to randomly select a conundrum!
'''

import sys
import random
from decimal import Decimal
import time
import simpleaudio as sa
import re
import copy

def checkScores(player1Score,player2Score,player1,player2):
    print("Scores so far:")
    print(player1, ", you have ", player1Score, " points")
    print(player2, ", you have ", player2Score, " points")

def playAudio():
    print("Are you ready?")
    time.sleep(3)
    print("Go!")
    time.sleep(1)
    wave_obj = sa.WaveObject.from_wave_file("countdown.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    print("Stop!")

def numbersScore(answer,nums,target):
    if answer == "N/A":
        print("Maybe next time!")
        return 0

    #make sure all numbers are ok.
    check = answer
    check = re.findall("(\d+)", check)
    print(check)
    Nums = copy.deepcopy(nums)
    for i in check:
        i = int(i)
        if i not in Nums:
            print("Sorry, ", i, " was not in your number list!")
            return 0
        else:
            Nums.remove(i)

    #Check solution
    solution = eval(answer)
    print("Your soluion is: ", solution)

    if(abs(solution-target) == 0):
        print("Congratulations -- 10 points!")
        return 10
    elif(abs(solution-target) <= 5):
        print("You were close! -- 7 points!")
        return 7
    elif(abs(solution-target) <= 10):
        print("Good effort! -- 5 points!")
        return 5
    else:
        print("Better luck next time!")
        return 0

def lettersScore(answer,letters):
  
    #First check that you used the correct letters
    check = copy.deepcopy(letters)
    answer = answer.upper()
    for i in answer:
        if i not in check:
            print('Sorry, you used some of the wrong letters!')
            return 0
        else:
            check.remove(i)

    # opening the text file 
    with open('dictionary.txt','r') as file: 
        for line in file: 
            for word in line.split():
                if word == answer:
                    print('Good word -- ', len(answer), 'points')
                    return len(answer)

    print('Sorry your word was not in the dictionary!')
    return 0

def Conundrum(player1,player2):
    
    #Get a random nine letter word from the dictionary
    randomNum = random.randint(0,29149)
    print(randomNum)

    conundrum = ''

    myfile = open('conundrums.txt')
    all_lines = myfile.readlines()
    conundrum = all_lines[randomNum]
    myfile.close()
    conundrum = conundrum.rstrip()
    anagram = ''.join(random.sample(conundrum,len(conundrum)))
    print("Your conundrum is",anagram)
    playAudio()
    
    player1Answer = input(player1+", what's your answer?")
    player2Answer = input(player2+", what's your answer?")
    player1Score =0
    player2Score =0
    if(player1Answer.upper() == conundrum):
        player1Score = 10
    if(player2Answer.upper() == conundrum):
        player2Score = 10
    
    print("The answer is:",conundrum)
    print(player1,"you get:",player1Score,"points!")
    print(player2,"you get:",player2Score,"points!")
    return player1Score,player2Score

def numbersGame(player1,player2,who):
    print("NUMBERS GAME! :D")
    largeNums = [25,50,75,100]
    smallNums = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
  
    print(who,"It's your numbers game!")
    numOk = False
    while numOk == False:
        numLarge = input("Please select how many large numbers: (4 or less) ")
        numLarge = int(numLarge)
        try:
           val = int(numLarge)
           if(val <= 4):
               numOk = True
        except ValueError:
            print("Need to enter an integer of 4 or less")
    
    #Pick six numbers - numLarge large numbers and the rest small numbers
    nums = []
    for i in range(numLarge):
        randomNum = random.randint(0,len(largeNums)-1)
        nums.append(largeNums[randomNum])
        largeNums.remove(largeNums[randomNum])
    
    numSmall = 6 - numLarge;
    
    for i in range(numSmall):
        randomNum = random.randint(0,len(smallNums)-1)
        nums.append(smallNums[randomNum])
        smallNums.remove(smallNums[randomNum])
    
    print("Your numbers are: ",nums)
    #Determine the number to get
    targetNum = random.randint(100,1000)
    print("Target number is: ",targetNum)
    playAudio()

    player1Answer = input(player1+", what's your solution? Enter N/A if not close: ")
    player1Score = numbersScore(player1Answer,nums,targetNum)
    player2Answer = input(player2+", what's your solution? Enter N/A if not close: ")
    player2Score = numbersScore(player2Answer,nums,targetNum)
    return player1Score, player2Score

#The available letters are selected to mimic the TV show!
def lettersGame(player1,player2,who):
    print("LETTERS GAME! :D:")
    vowels = ['E','E','E','E','E','E','E','E','E','E','E','E']
    vowels += ['A','A','A','A','A','A','A','A','A']
    vowels += ['I','I','I','I','I','I','I','I','I']
    vowels += ['O','O','O','O','O','O','O','O']
    vowels += ['U','U','U','U']

    consonants = ['N','N','N','N','N','N']
    consonants += ['R','R','R','R','R','R']
    consonants += ['T','T','T','T','T','T']
    consonants += ['L','L','L','L']
    consonants += ['S','S','S','S']
    consonants += ['D','D','D','D']
    consonants += ['G','G','G','V','V','W','W','Y','Y','K','J','X','Q','Z']
    consonants += ['B','B','C','C','M','M','P','P','F','F','H','H']

    letters = []
    vcount = 0
    ccount = 0 

    print(who,"It's your letters game")
    while len(letters) != 9:
        corv = input(" Consonant(c) or Vowel(v)?")
        if(corv != "c" and corv != "v"):
            print("Please enter either c or v")
            continue
        else:
            if(corv == "c"):
                randomNum = random.randint(0,len(consonants)-1)
                letters += consonants[randomNum]
                consonants.remove(consonants[randomNum])
                ccount +=1
            else:
                randomNum = random.randint(0,len(vowels)-1)
                letters += vowels[randomNum]
                vowels.remove(vowels[randomNum])
                vcount +=1
            print(letters)
    
    playAudio()
    player1Answer = input(player1+", what's your word?")
    player1Score = lettersScore(player1Answer,letters)
    player2Answer = input(player2+", what's your word?")
    player2Score = lettersScore(player2Answer,letters)
    return player1Score,player2Score

print("Countdown Toy")
player1 = input("Input player 1's name: ")
player2 = input("Input player 2's name: ")
print("Hello ",player1," and ", player2)
player1Score = 0
player2Score = 0

val1 = 0
val2 = 0

#This next part is not very graceful but only a quick toy and 
val1,val2 = lettersGame(player1,player2,player1)
player1Score += val1
player2Score += val2
print('\n\n\n')
val1,val2 = lettersGame(player1,player2,player2)
player1Score += val1
player2Score += val2

print('\n\n\n')
val1,val2 = numbersGame(player1,player2,player1)
player1Score += val1
player2Score += val2

print('\n\n\n')
val1,val2 = lettersGame(player1,player2,player2)
player1Score += val1
player2Score += val2

print('\n\n\n')
val1,val2 = lettersGame(player1,player2,player1)
player1Score += val1
player2Score += val2

print('\n\n\n')
val1,val2 = numbersGame(player1,player2,player2)
player1Score += val1
player2Score += val2

print('\n\n\n')
val1,val2 = Conundrum(player1,player2)
player1Score += val1
player2Score += val2

print('\n\n\n')
print("The final scores are:....")
print(player1,"you have:",player1Score,"points")
print(player2,"you have:",player2Score,"points")

if(player1Score > player2Score):
    print("Congratulations,",player1," you win! :) ")

elif(player2Score > player1Score):
    print("Congratulations,",player2," you win! :) ")
else:
    print("Wow! It's a draw!");

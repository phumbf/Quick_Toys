'''
A quick toy to help me learn Mandarin

I've put in two quick modes - one to be shown a character and one where I have to write a character 
(using the appropriate keyboard)

The list of characters is taken from the HSK level 2 list which I'm currently studying
https://my-hsk.com/hsk-2-level/

'''

import pandas as pd
import sys

def characters(data):

    dodgydata = data.copy()
    dodgydata = dodgydata.iloc[0:0]

    for row_index,row in data.iterrows():
        for val in row[['Character']].values:
            print('The character is: ',val,'\n\n\n')
            knowIt = input('Do you know what this character is? [y/n]: ')
            if(knowIt != 'y'):
                dodgydata = dodgydata.append(row,ignore_index=True)
                print('The answer was:', row.values,'\n\n\n')

    return dodgydata

def charactersTest(number,data):
    dodgydata = data.sample(number)
    while dodgydata.empty == False:
        dodgydata = characters(dodgydata)

def english(number,data):
    testSample = data.sample(number)

    for row_index,row in testSample.iterrows():
        Val = row[['English Translation']]
        Charac = row[['Character']]
        Piny = row[['Pinyin']]

        for val,charac,piny in zip(Val.values, Charac.values, Piny.values):
            print('The English is: ',val,'\n\n\n')
            answer = input('Do you know what the character should be? [Input a character]: ')
            if(answer == charac):
                print("CORRECT: ", piny, charac,'\n\n\n')
            else:
                print("INCORRECT, ANSWER WAS: ", charac, piny,'\n\n\n')



data = pd.read_csv('HSK-2-Vocabulary-list.txt',sep=',')
data.columns = ['Character', 'Pinyin', 'English Translation']
print('Welcome to HSK memoriser')

modeOk = False
while modeOk == False:
    mode = input('Would you like to be shown or have to write characters? [s/w]\n\n\n')
    if(mode != 's' and mode != 'w'):
        print('ERROR: Please enter either s or w \n\n\n')
    else:
        modeOk = True

numOk = False
while numOk == False:
    num = input('Please enter how many questions you would like (between 1 and 300): \n\n\n')
    try:
        num = int(num)
        if(num > 0 and num <= 300):
            numOk = True
    except ValueError:
        print('ERROR: Need to enter between 1 and 300\n\n\n')

if mode == 's':
    charactersTest(num,data)
else: 
    english(num,data)

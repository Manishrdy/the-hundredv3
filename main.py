# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:04:48 2021

@author: Manish Reddy.
"""

import random
import os
import glob
import time
import pandas as pd
import sys
import io
from tabulate import tabulate
import shutil

print('''
      $$\      $$\                     $$\           $$\       
      $$$\    $$$ |                    \__|          $$ |      
      $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\  $$$$$$$\ $$$$$$$\  
      $$\$$\$$ $$ | \____$$\ $$  __$$\ $$ |$$  _____|$$  __$$\ 
      $$ \$$$  $$ | $$$$$$$ |$$ |  $$ |$$ |\$$$$$$\  $$ |  $$ |
      $$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$ | \____$$\ $$ |  $$ |
      $$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |$$ |$$$$$$$  |$$ |  $$ |
      \__|     \__| \_______|\__|  \__|\__|\_______/ \__|  \__|
      ----Martian The Hundred | Planet Cricket - @Manish. -----
                                                               
                                                               
      '''.center(shutil.get_terminal_size().columns))

#Creating arrays for 4's and 6's
zeroComm = []
oneComm = []
twoComm = []
threeComm = []
fourComm = []
sixComm = []
outComm = []
batsmenScoreboard1 = []
batsmenScoreboard2 = []

file = io.open('./commentry/0.txt','r',encoding="utf8")
for i in file.readlines():
    zeroComm.append(i)

for i in range(len(zeroComm)):
    zeroComm[i] = zeroComm[i].replace('\n','')
    
file = io.open('./commentry/1.txt','r',encoding="utf8")
for i in file.readlines():
    oneComm.append(i)

for i in range(len(oneComm)):
    oneComm[i] = oneComm[i].replace('\n','')

file = io.open('./commentry/2.txt','r',encoding="utf8")
for i in file.readlines():
    twoComm.append(i)

for i in range(len(twoComm)):
    twoComm[i] = twoComm[i].replace('\n','')
    
file = io.open('./commentry/3.txt','r',encoding="utf8")
for i in file.readlines():
    threeComm.append(i)

for i in range(len(threeComm)):
    threeComm[i] = threeComm[i].replace('\n','')

file = io.open('./commentry/4.txt','r',encoding="utf8")
for i in file.readlines():
    fourComm.append(i)

for i in range(len(fourComm)):
    fourComm[i] = fourComm[i].replace('\n','')
    
file = io.open('./commentry/6.txt','r',encoding="utf8")
for i in file.readlines():
    sixComm.append(i)

for i in range(len(sixComm)):
    sixComm[i] = sixComm[i].replace('\n','')
    
file = io.open('./commentry/out.txt','r',encoding="utf8")
for i in file.readlines():
    outComm.append(i)

for i in range(len(outComm)):
    outComm[i] = outComm[i].replace('\n','')


#recursion steps
sys.setrecursionlimit(10**9)

#various outcomes
outcomes = [0, 1, 2, 3, 4, 6, 'Out', 'Wide', 'Leg Bye', 'No Ball']
outList = ['Stumped', 'Bowled', 'Caught', 'Run Out', 'Hit Wicket', 'Lbw']
gameRate = 0

oneIngBat = []
oneIngBowl = []

team1Stats = []
team2Stats = []
win1 = []


def checkWinner(team1, team2, target, totalWickets, totalScore, ball):
    
    team1, team2 = team2, team1
    team1Score = target - 1
    
    if totalScore == target or totalScore > target:
        wicketsWon = 10 - totalWickets
        win = '{} beat {} by {} wickets.'.format(team2, team1, wicketsWon)
        win1.append(win)
        print()
        print(win)
        print()
        return True
    
    elif ball == 100 and totalScore < target:
        runsWon = team1Score - totalScore
        win = '{} beat {} by {} runs.'.format(team1, team2, runsWon)
        win1.append(win)
        print()
        print(win)
        print()
    elif ball == 100 and totalScore == team1Score:
        draw = '{} draw with {}'.format(team1, team2)
        win1.append(draw)
        print()
        print(draw)
        print()
        
    elif totalScore < target and totalWickets == 10:
        runsWon = team1Score - totalScore
        win = '{} beat {} by {} runs.'.format(team1, team2, runsWon)
        win1.append(win)
        print()
        print(win)
        print()
    
    elif totalWickets == 10 and ball != 100:
        runsWon = team1Score - totalScore
        win = '{} beat {} by {} runs.'.format(team1, team2, runsWon)
        win1.append(win)
        print()
        print(win)
        print()
        
        
        
    
def printSummary():
    print()
    print()
    print('-------------------------------------------------------------------')
    print('Match Summary')
    print()
    print('{}     {}/{}    Balls {}'.format(team1Stats[0][0],team1Stats[0][1],team1Stats[0][2],
                                            team1Stats[0][3]))
    print('{}     {}/{}    Balls {}'.format(team2Stats[0][0],team2Stats[0][1],team2Stats[0][2],
                                            team2Stats[0][3]))
    print()
    print('{}'.format(win1[0]))
    
    

def prepInnings2(team1, team2, target):
    
    oneIngBat.clear()
    oneIngBowl.clear()
    
    flag = False
    
    team1Data = pd.read_csv(team1+'.csv')
    team2Data = pd.read_csv(team2+'.csv')
    
    team1BattingPlayers = team1Data['player']
    team1BattingPlayers = team1BattingPlayers.values.tolist()
    
    fielders = team2Data['player']
    fielders = fielders.values.tolist()
    
    team1BattingRatings = team1Data[['0s','1s','2s','3s','4s','6s','out','wide','leg bye','no ball']]
    team1BattingRatings = team1BattingRatings.values.tolist()
    
    team2Bowlers = team2Data[team2Data['role'] == 'Bowler']
    team2Bowlers = team2Bowlers[['player','bowling_action','bowling_points']]
    team2Bowlers = team2Bowlers.values.tolist()
    for i in team2Bowlers:
        i.extend([0])

    initialBalls = 0
    
    initialScore = 0
    totalScore = 0
    
    initialExtras = 0
    totalExtras = 0
    
    initialWickets = 0
    totalWickets = 0
    
    initialDots = 0
    totalDots = 0
    
    onStrikeRuns = 0
    onStrikeBalls = 0
    onStrikeFours = 0
    onStrikeSixes = 0
    
    offStrikeRuns = 0
    offStrikeBalls = 0
    offStrikeFours = 0
    offStrikeSixes = 0
    
    drs = 2
    
    checkBowlers = []
    
    onStrike = team1BattingPlayers[0]
    onStrikeRating = team1BattingRatings[0]
    
    offStrike = team1BattingPlayers[1]
    offStrikeRating = team1BattingRatings[1]
    
    team2Bowlers = sorted(team2Bowlers,key=lambda x: x[2], reverse=True)
    team2Bowlers = sorted(team2Bowlers,key=lambda x: x[1])

    bowlerPresent = team2Bowlers[0][0]
    bowlerPresentR = team2Bowlers[0][2]
    checkBowlers.append(bowlerPresent)
    
    keeper = team2Data[team2Data['role'] == 'Keeper']['player']
    keeper = keeper.values
    
    for i in team2Bowlers:
        oneIngBowl.append([i[0],0,0,0,0,0,0])

    def changeBowler(initialBalls):
        changeB = random.choice(team2Bowlers)
        bIndex = team2Bowlers.index(changeB)
        if changeB[0] != checkBowlers[-1] and team2Bowlers[bIndex][3] < 20:
            if initialBalls == 5:
                if team2Bowlers[bIndex][3] == 5 or team2Bowlers[bIndex][3] == 15 or team2Bowlers[bIndex][3] == 0 or team2Bowlers[bIndex][3] == 10:
                    return changeB
            if initialBalls == 10:
                if team2Bowlers[bIndex][3] == 0 or team2Bowlers[bIndex][3] == 5 or team2Bowlers[bIndex][3] == 10:
                    return changeB
                elif team2Bowlers[bIndex][3] == 15:
                    return changeBowler(initialBalls)
        return changeBowler(initialBalls)
    
    print('The new batsman is {}'.format(onStrike))
    print('The new batsman is {}'.format(offStrike))
    print('The new bowler is {}'.format(bowlerPresent))
    print()
    
    for ball in range(1,101):
        time.sleep(gameRate)
        def callBatsman1R():
           if bowlerPresentR in range(71, 76):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 3
               onStrikeRating[1] = onStrikeRating[1] - 3
               onStrikeRating[2] = onStrikeRating[2] - 1
               onStrikeRating[6] = onStrikeRating[6] - 0
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.3
               onStrikeRating[4] = onStrikeRating[4] + 1.3
               onStrikeRating[5] = onStrikeRating[5] + 0.7
           elif bowlerPresentR in range(76, 81):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 5
               onStrikeRating[1] = onStrikeRating[1] - 5
               onStrikeRating[2] = onStrikeRating[2] - 3
               onStrikeRating[6] = onStrikeRating[6] - 1
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.7
               onStrikeRating[4] = onStrikeRating[4] + 2
               onStrikeRating[5] = onStrikeRating[5] + 1.5
           elif bowlerPresentR in range(81, 86):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 6
               onStrikeRating[1] = onStrikeRating[1] - 6
               onStrikeRating[2] = onStrikeRating[2] - 4
               onStrikeRating[6] = onStrikeRating[6] - 2
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 1
               onStrikeRating[4] = onStrikeRating[4] + 3
               onStrikeRating[5] = onStrikeRating[5] + 2
           elif bowlerPresentR in range(86, 91):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 7
               onStrikeRating[1] = onStrikeRating[1] - 7
               onStrikeRating[2] = onStrikeRating[2] - 5
               onStrikeRating[6] = onStrikeRating[6] - 3
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 2
               onStrikeRating[4] = onStrikeRating[4] + 4
               onStrikeRating[5] = onStrikeRating[5] + 3
           elif bowlerPresentR in range(91, 96):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 8
               onStrikeRating[1] = onStrikeRating[1] - 8
               onStrikeRating[2] = onStrikeRating[2] - 6
               onStrikeRating[6] = onStrikeRating[6] - 7
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 3
               onStrikeRating[4] = onStrikeRating[4] + 5
               onStrikeRating[5] = onStrikeRating[5] + 4
           elif bowlerPresentR in range(0,55):
               #increase
               onStrikeRating[0] = onStrikeRating[0] + 25
               onStrikeRating[1] = onStrikeRating[1] - 15
               onStrikeRating[2] = onStrikeRating[2] - 15
               onStrikeRating[6] = onStrikeRating[6] + 7
               #decrease
               onStrikeRating[3] = onStrikeRating[3] - 3
               onStrikeRating[4] = onStrikeRating[4] - 6
               onStrikeRating[5] = onStrikeRating[5] - 6
           elif bowlerPresentR in range(55,61):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 0.5
               onStrikeRating[1] = onStrikeRating[1] - 0.5
               onStrikeRating[2] = onStrikeRating[2] - 0.5
               onStrikeRating[6] = onStrikeRating[6] - 0.5
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.5
               onStrikeRating[4] = onStrikeRating[4] + 0.5
               onStrikeRating[5] = onStrikeRating[5] + 0.5
           elif bowlerPresentR in range(61,66):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 1
               onStrikeRating[1] = onStrikeRating[1] - 1
               onStrikeRating[2] = onStrikeRating[2] - 1
               onStrikeRating[6] = onStrikeRating[6] - 1
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.5
               onStrikeRating[4] = onStrikeRating[4] + 0.5
               onStrikeRating[5] = onStrikeRating[5] + 0.5
           elif bowlerPresentR in range(66,71):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 2
               onStrikeRating[1] = onStrikeRating[1] - 2
               onStrikeRating[2] = onStrikeRating[2] - 2
               onStrikeRating[6] = onStrikeRating[6] - 2
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 1
               onStrikeRating[4] = onStrikeRating[4] + 1
               onStrikeRating[5] = onStrikeRating[5] + 1
        
        if bowlerPresentR in range(71, 76):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 3
            onStrikeRating[1] = onStrikeRating[1] + 3
            onStrikeRating[2] = onStrikeRating[2] + 1
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.3
            onStrikeRating[4] = onStrikeRating[4] - 1.3
            onStrikeRating[5] = onStrikeRating[5] - 0.7
        elif bowlerPresentR in range(76, 81):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 5
            onStrikeRating[1] = onStrikeRating[1] + 5
            onStrikeRating[2] = onStrikeRating[2] + 3
            onStrikeRating[6] = onStrikeRating[6] + 1
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.7
            onStrikeRating[4] = onStrikeRating[4] - 2
            onStrikeRating[5] = onStrikeRating[5] - 1.5
        elif bowlerPresentR in range(81, 86):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 6
            onStrikeRating[1] = onStrikeRating[1] + 6
            onStrikeRating[2] = onStrikeRating[2] + 4
            onStrikeRating[6] = onStrikeRating[6] + 2
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 1
            onStrikeRating[4] = onStrikeRating[4] - 3
            onStrikeRating[5] = onStrikeRating[5] - 2
        elif bowlerPresentR in range(86, 91):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 7
            onStrikeRating[1] = onStrikeRating[1] + 7
            onStrikeRating[2] = onStrikeRating[2] + 5
            onStrikeRating[6] = onStrikeRating[6] + 3
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 2
            onStrikeRating[4] = onStrikeRating[4] - 4
            onStrikeRating[5] = onStrikeRating[5] - 3
        elif bowlerPresentR in range(91, 96):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 8
            onStrikeRating[1] = onStrikeRating[1] + 8
            onStrikeRating[2] = onStrikeRating[2] + 6
            onStrikeRating[6] = onStrikeRating[6] + 7
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 3
            onStrikeRating[4] = onStrikeRating[4] - 5
            onStrikeRating[5] = onStrikeRating[5] - 4
        elif bowlerPresentR in range(0,55):
            #increase
            onStrikeRating[0] = onStrikeRating[0] - 25
            onStrikeRating[1] = onStrikeRating[1] + 15
            onStrikeRating[2] = onStrikeRating[2] + 15
            onStrikeRating[6] = onStrikeRating[6] - 7
            #decrease
            onStrikeRating[3] = onStrikeRating[3] + 3
            onStrikeRating[4] = onStrikeRating[4] + 6
            onStrikeRating[5] = onStrikeRating[5] + 6
        elif bowlerPresentR in range(55,61):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 0.5
            onStrikeRating[1] = onStrikeRating[1] + 0.5
            onStrikeRating[2] = onStrikeRating[2] + 0.5
            onStrikeRating[6] = onStrikeRating[6] + 0.5
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.5
            onStrikeRating[4] = onStrikeRating[4] - 0.5
            onStrikeRating[5] = onStrikeRating[5] - 0.5
        elif bowlerPresentR in range(61,66):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 1
            onStrikeRating[1] = onStrikeRating[1] + 1
            onStrikeRating[2] = onStrikeRating[2] + 1
            onStrikeRating[6] = onStrikeRating[6] + 1
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.5
            onStrikeRating[4] = onStrikeRating[4] - 0.5
            onStrikeRating[5] = onStrikeRating[5] - 0.5
        elif bowlerPresentR in range(66,71):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 2
            onStrikeRating[1] = onStrikeRating[1] + 2
            onStrikeRating[2] = onStrikeRating[2] + 2
            onStrikeRating[6] = onStrikeRating[6] + 2
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 1
            onStrikeRating[4] = onStrikeRating[4] - 1
            onStrikeRating[5] = onStrikeRating[5] - 1


        
        ballOutCome = random.choices(outcomes, weights=(onStrikeRating), k=1)
        callBatsman1R()
        
        if ballOutCome == [0]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 1
            totalDots = totalDots + 1
            initialScore = initialScore + 0
            totalScore = totalScore + 0
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, dot, {}'.format(ball,bowlerPresent,onStrike,random.choice(zeroComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
        elif ballOutCome == [1]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 1
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, One Run, {}'.format(ball,bowlerPresent,onStrike,random.choice(oneComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            else:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                
        elif ballOutCome == [2]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 2
            totalScore = totalScore + 2
            
            onStrikeRuns = onStrikeRuns + 2
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, Two Runs, {}'.format(ball,bowlerPresent,onStrike,random.choice(twoComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        elif ballOutCome == [3]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 3
            totalScore = totalScore + 3
            
            onStrikeRuns = onStrikeRuns + 3
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, Three Runs, {}'.format(ball,bowlerPresent,onStrike,random.choice(zeroComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            else:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
        elif ballOutCome == [4]:
            
            onStrikeFours = onStrikeFours + 1
            
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 4
            totalScore = totalScore + 4
            
            onStrikeRuns = onStrikeRuns + 4
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, FOUR runs, {}'.format(ball,bowlerPresent,onStrike,random.choice(fourComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        elif ballOutCome == [6]:
            
            onStrikeSixes = onStrikeSixes + 1
            
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 6
            totalScore = totalScore + 6
            
            onStrikeRuns = onStrikeRuns + 6
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, SIX !, {}'.format(ball,bowlerPresent,onStrike,random.choice(sixComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
       
        elif ballOutCome == ['Out']:
            
            # initialWickets = initialWickets + 1
            # totalWickets = totalWickets + 1
            initialDots = initialDots + 1
            totalDots = totalDots + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            initialBalls = initialBalls + 1
            
            outType = random.choices(outList, weights=(0.3,4,5,0.6,0.1,4.5), k=1)
            cPlayer = random.choice(fielders)
            
            if outType == ['Caught']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {} by {}, {}'.format(ball,bowlerPresent,onStrike,*outType,cPlayer,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     c. {}     b. {}     {}({}){} [{}x4 {}x6]'.format(cPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'c. ',cPlayer, bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print()
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                
            elif outType == ['Bowled']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {}, {}'.format(ball,bowlerPresent,onStrike,*outType,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'b. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
                   offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif outType == ['Stumped']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {} by {}, {}'.format(ball,bowlerPresent,onStrike,*outType,*keeper,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     st. {}     b. {}     {}({}){} [{}x4 {}x6]'.format(*keeper,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'st. ',*keeper, bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out',*keeper, '', offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif outType == ['Run Out']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                initialWickets = initialWickets - 1
                print('Ball {} - {} to {}, {} by {}, {}'.format(ball,bowlerPresent,onStrike,*outType,cPlayer,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     ro. {}     b. {}     {}({}){} [{}x4 {}x6]'.format(cPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'ro. ',cPlayer, bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out',cPlayer, "", offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif outType == ['Hit Wicket']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {}, {}'.format(ball,bowlerPresent,onStrike,*outType,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'hw. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                
            elif outType == ['Lbw']:
                print('Ball {} - {} to {}, {}, {}'.format(ball,bowlerPresent,onStrike,*outType,random.choice(outComm).replace('batsman', onStrike)))
                print()
                
                
                review = ['yes','no']
                reviewYN = random.choices(review, weights=(0.60,0.40), k=1)
                
                if drs == 2 or drs == 1:
                    reviewYN == ['yes']
                else:
                    reviewYN == ['no']
                
                if reviewYN == ['yes']:
                    print('Reviews available for team {} - {}'.format(team1,drs))
                    print('{} goes for a review...'.format(onStrike))
                    print('The umpire signals to the third umpire.')
    
                    umpireDecision = ['out','not out']
                    umpireNO = random.choices(umpireDecision, weights=(0.60,0.40), k=1)
                    if umpireNO == ['out']:
                        initialWickets = initialWickets + 1
                        totalWickets = totalWickets + 1
                        
                        drs = drs - 1
                        
                        print('The umpire gives OUT ! {} departs.'.format(onStrike))
                        print()
                        print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                        print()
                        sr = (onStrikeRuns * 100) // onStrikeBalls
                        oneIngBat.append([onStrike, 'lbw. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
                       onStrikeFours, onStrikeSixes, sr])
                        if totalWickets == 10:
                            sr = (offStrikeRuns * 100) // offStrikeBalls
                            oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
                       offStrikeFours, offStrikeSixes, sr])
                            break
                        else:
                            onStrike = team1BattingPlayers[totalWickets+1]
                            onStrikeRating = team1BattingRatings[totalWickets+1]
                            
                        onStrikeBalls = 0
                        onStrikeFours = 0
                        onStrikeRuns = 0
                        onStrikeSixes = 0
                        print('The new batsman is {}'.format(onStrike))
                        
                    elif umpireNO == ['not out']:
                        print('The umpire gives NOT OUT ! and the review remains !!!')
                        print()
                        initialBalls = initialBalls + 0

                        initialDots = initialDots + 1
                        totalDots = totalDots + 1
                        initialScore = initialScore + 0
                        totalScore = totalScore + 0
                        
                        onStrikeRuns = onStrikeRuns + 0
                        onStrikeBalls = onStrikeBalls + 0
                    
                elif reviewYN == ['no']:
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    sr = (onStrikeRuns * 100) // onStrikeBalls
                    oneIngBat.append([onStrike, 'lbw. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
                   onStrikeFours, onStrikeSixes, sr])
                    if totalWickets == 10:
                        sr = (offStrikeRuns * 100) // offStrikeBalls
                        oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
                   offStrikeFours, offStrikeSixes, sr])
                        break
                    else:
                        onStrike = team1BattingPlayers[totalWickets+1]
                        onStrikeRating = team1BattingRatings[totalWickets+1]
                    onStrikeBalls = 0
                    onStrikeFours = 0
                    onStrikeRuns = 0
                    onStrikeSixes = 0
                    print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes  
            
            
        elif ballOutCome == ['Wide']:
            
            initialBalls = initialBalls + 0
    
            initialDots = initialDots + 0
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 0
            
            initialExtras = initialExtras + 1
            totalExtras = totalExtras + 1
            
            print('Ball {} - {} to {}, Wide Ball'.format(ball,bowlerPresent,onStrike))
            o = [0,1,2]
            b = random.choice(o)
            if b == 1:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 1
                totalScore = totalScore + 1
                
                onStrikeRuns = onStrikeRuns + 1
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, One Run'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif b == 0:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 1
                totalDots = totalDots + 1
                initialScore = initialScore + 0
                totalScore = totalScore + 0
                
                onStrikeRuns = onStrikeRuns + 0
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, dot'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif b == 2:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 2
                totalScore = totalScore + 2
                
                onStrikeRuns = onStrikeRuns + 2
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, Two Runs'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        
        elif ballOutCome == ['Leg Bye']:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, Leg Bye'.format(ball,bowlerPresent,onStrike))
            
            if ball % 10 == 0:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            else:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
        elif ballOutCome == ['No Ball']:
            initialBalls = initialBalls + 0
    
            initialDots = initialDots + 0
            totalDots = totalDots + 1
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            initialExtras = initialExtras + 1
            totalExtras = totalExtras + 1
            
            print('Ball {} - {} to {}, No Ball, Free Hit coming up'.format(ball,bowlerPresent,onStrike))
            
            o = [0,1,2,4,6]
            b = random.choice(o)
            if b == 1:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 1
                totalScore = totalScore + 1
                
                onStrikeRuns = onStrikeRuns + 1
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, One Run'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif b == 0:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 1
                initialScore = initialScore + 0
                totalScore = totalScore + 0
                
                onStrikeRuns = onStrikeRuns + 0
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, dot'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif b == 2:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 2
                totalScore = totalScore + 2
                
                onStrikeRuns = onStrikeRuns + 2
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, Two Runs'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            elif b == 4:
                onStrikeFours = onStrikeFours + 1
            
                initialBalls = initialBalls + 1
        
                initialDots = initialDots + 0
                initialScore = initialScore + 4
                totalScore = totalScore + 4
                
                onStrikeRuns = onStrikeRuns + 4
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, FOUR runs'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif b == 6:
                onStrikeSixes = onStrikeSixes + 1
            
                initialBalls = initialBalls + 1
        
                initialDots = initialDots + 0
                initialScore = initialScore + 6
                totalScore = totalScore + 6
                
                onStrikeRuns = onStrikeRuns + 6
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, SIX !'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        
        if ball % 5 == 0 and ball % 10 != 0:

            chance = ['no','yes']
            chB = random.choices(chance, weights=(0.75,0.25), k=1)
            if chB == ['no']:
                pass
            elif chB == ['yes']:
                for i in oneIngBowl:
                    if bowlerPresent == i[0]:
                        bSIndex = oneIngBowl.index(i)
                        oneIngBowl[bSIndex][1] = oneIngBowl[bSIndex][1] + initialBalls
                        oneIngBowl[bSIndex][2] = oneIngBowl[bSIndex][2] + initialDots
                        oneIngBowl[bSIndex][3] = oneIngBowl[bSIndex][3] + initialScore
                        oneIngBowl[bSIndex][4] = oneIngBowl[bSIndex][4] + initialWickets
                        oneIngBowl[bSIndex][5] = round(oneIngBowl[bSIndex][3]/oneIngBowl[bSIndex][1],2)
                        oneIngBowl[bSIndex][6] = oneIngBowl[bSIndex][6] + initialExtras
                 
                for i in team2Bowlers:
                    if i[0] == bowlerPresent:
                        bIndex = team2Bowlers.index(i)
                        team2Bowlers[bIndex][3] = team2Bowlers[bIndex][3] + 5

                print()
                print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
                print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
                rr = totalScore / ball
                rrr = (target - totalScore) / (100-ball)
                print('     RR - {}     RRR- {}'.format(round(rr,2),round(rrr,2)))
                print()
                print('     {}     ({}){}  [{}x4, {}x6]'.format(onStrike,onStrikeRuns,
                                                              onStrikeBalls,onStrikeFours,onStrikeSixes))
                print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                            offStrikeBalls,offStrikeFours,offStrikeSixes))
                print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
                print()
                
                flag = True
                checkBowlers.append(bowlerPresent)
                changeB = changeBowler(5)
                
                initialBalls = 0
                initialDots = 0
                initialExtras = 0
                initialScore = 0
                initialWickets = 0
                
                
                bowlerPresent = changeB[0]
                bowlerPresentR = changeB[2]
                print()
                print('Change of bowler')
                print('The new bowler is {}'.format(changeB[0]))
                print()
                
        if ball % 10 == 0:
            for i in oneIngBowl:
                if bowlerPresent == i[0]:
                    bSIndex = oneIngBowl.index(i)
                    oneIngBowl[bSIndex][1] = oneIngBowl[bSIndex][1] + initialBalls
                    oneIngBowl[bSIndex][2] = oneIngBowl[bSIndex][2] + initialDots
                    oneIngBowl[bSIndex][3] = oneIngBowl[bSIndex][3] + initialScore
                    oneIngBowl[bSIndex][4] = oneIngBowl[bSIndex][4] + initialWickets
                    oneIngBowl[bSIndex][5] = round(oneIngBowl[bSIndex][3]/oneIngBowl[bSIndex][1],2)
                    oneIngBowl[bSIndex][6] = oneIngBowl[bSIndex][6] + initialExtras
                    
            print()
            print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
            print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
            rr = totalScore / ball
            if ball == 100:
                rrr = 0
            else:
                rrr = (target - totalScore) / (100-ball)
                
            print('     RR - {}     RRR - {}'.format(round(rr,2),round(rrr,2)))
            print()
            print('     {}     ({}){}  [{}x4, {}x6]'.format(onStrike,onStrikeRuns,
                                                             onStrikeBalls,onStrikeFours,onStrikeSixes))
            print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                            offStrikeBalls,offStrikeFours,offStrikeSixes))
            print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
            print()
            
            # print()
            for i in team2Bowlers:
                if i[0] == bowlerPresent:
                    bIndex = team2Bowlers.index(i)
                    if flag == True:
                        team2Bowlers[bIndex][3] = team2Bowlers[bIndex][3] + 5
                    elif flag == False:
                        team2Bowlers[bIndex][3] = team2Bowlers[bIndex][3] + 10
            
            checkBowlers.append(bowlerPresent)
            changeB = changeBowler(10)
            
            initialBalls = 0
            initialDots = 0
            initialExtras = 0
            initialScore = 0
            initialWickets = 0
            flag = False
            
            bowlerPresent = changeB[0]
            bowlerPresentR = changeB[2]
            if ball != 100:
                print()
                print('The new bowler is {}'.format(changeB[0]))
                print()
            
            if ball == 100 and totalWickets != 10:
                if onStrikeBalls == 0:
                    sr = 0
                else:
                    sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'Not Out','', '', onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if ball == 100 and ballOutCome == ['Out']:
                    offStrikeBalls = 1
                else:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
            offStrikeFours, offStrikeSixes, sr])
        
        cW = checkWinner(team1, team2, target, totalWickets, totalScore, ball)
        if cW == True:
            if totalWickets != 10:
                if onStrikeBalls == 0:
                    sr = 0
                else:
                    sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'Not Out','', '', onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                sr = (offStrikeRuns * 100) // offStrikeBalls
                oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
            offStrikeFours, offStrikeSixes, sr])
            
            if totalWickets == 10:
                sr = (offStrikeRuns * 100) // offStrikeBalls
                oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
            offStrikeFours, offStrikeSixes, sr])
                
                for i in oneIngBowl:
                    if bowlerPresent == i[0]:
                        bSIndex = oneIngBowl.index(i)
                        oneIngBowl[bSIndex][1] = oneIngBowl[bSIndex][1] + initialBalls
                        oneIngBowl[bSIndex][2] = oneIngBowl[bSIndex][2] + initialDots
                        oneIngBowl[bSIndex][3] = oneIngBowl[bSIndex][3] + initialScore
                        oneIngBowl[bSIndex][4] = oneIngBowl[bSIndex][4] + initialWickets
                        oneIngBowl[bSIndex][5] = round(oneIngBowl[bSIndex][3]/oneIngBowl[bSIndex][1],2)
                        oneIngBowl[bSIndex][6] = oneIngBowl[bSIndex][6] + initialExtras
                        
                
            
            if totalWickets != 10 and ball != 100:
                print()
                print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
                print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
                print()
                print('     {}     ({}){}  [{}x4, {}x6]'.format(onStrike,onStrikeRuns,
                                                                 onStrikeBalls,onStrikeFours,onStrikeSixes))
                print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                                offStrikeBalls,offStrikeFours,offStrikeSixes))
                print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
                print()
                
            if totalWickets == 10 and ball != 100:
                print()
                print('     End of innings')
                print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
                print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
                print()
                print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                                offStrikeBalls,offStrikeFours,offStrikeSixes))
                print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
                print()
                
            break
        
        if totalWickets == 10 and ball != 100:
                print()
                print('     End of innings')
                print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
                print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
                print()
                print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                                offStrikeBalls,offStrikeFours,offStrikeSixes))
                print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
                print()
        
    print('{} 2nd Innings'.format(team1))
    
    for i in range(len(team1BattingPlayers)):
        j = i
        while j < len(oneIngBat) and oneIngBat[j][0] != team1BattingPlayers[i]:
            j = j + 1
            if j < len(oneIngBat) and oneIngBat[j][0] == team1BattingPlayers[i]:
                oneIngBat[i],oneIngBat[j] = oneIngBat[j],oneIngBat[i]
    
    print()
    df = pd.DataFrame(oneIngBat, columns =['Batsman','','Fielder','Bowler','Runs','Balls','4s','6s','SR'])
    print(tabulate(df, showindex=False, headers=df.columns))
    dnb = df['Batsman'].to_list()
    dnb = list(set(team1BattingPlayers) - set(dnb))
    print()
    rr = totalScore / ball
    print('   Total:   {}/{}        Balls: {}        Run Rate: {}        Extras: {}'.format(totalScore,totalWickets,ball,round(rr,2),totalExtras))
    print()
    if len(dnb) == 0:
        print('DNB : Nil')
    else: 
        print('DNB : ',dnb)
    print()
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    bat = path+team1+'-batting'+timestr+'.csv'
    df.to_csv(bat)
    
    print('{} Bowling Scoreboard'.format(team2))
    print()
    df1 = pd.DataFrame(oneIngBowl,columns=['Bowler','Balls','Dots','Runs','Wickets','Economy','Extras'])
    print(tabulate(df1, showindex=False, headers=df1.columns))
    print()
    print('   Total:   {}/{}        Balls: {}        Run Rate: {}        Extras: {}'.format(totalScore,totalWickets,ball,round(rr,2),totalExtras))
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    ballP = path+team2+'-bowling'+timestr+'.csv'
    df1.to_csv(ballP)
    
    team2Stats.append([team1,totalScore,totalWickets,ball])
    
    printSummary()


def prepInnings(team1, team2):
    
    flag = False
    
    team1Data = pd.read_csv(team1+'.csv')
    team2Data = pd.read_csv(team2+'.csv')
    
    team1BattingPlayers = team1Data['player']
    team1BattingPlayers = team1BattingPlayers.values.tolist()
    
    fielders = team2Data['player']
    fielders = fielders.values.tolist()
    
    team1BattingRatings = team1Data[['0s','1s','2s','3s','4s','6s','out','wide','leg bye','no ball']]
    team1BattingRatings = team1BattingRatings.values.tolist()
    
    team2Bowlers = team2Data[team2Data['role'] == 'Bowler']
    team2Bowlers = team2Bowlers[['player','bowling_action','bowling_points']]
    team2Bowlers = team2Bowlers.values.tolist()
    for i in team2Bowlers:
        i.extend([0])
    
    initialBalls = 0
    
    initialScore = 0
    totalScore = 0
    
    initialExtras = 0
    totalExtras = 0
    
    initialWickets = 0
    totalWickets = 0
    
    initialDots = 0
    totalDots = 0
    
    onStrikeRuns = 0
    onStrikeBalls = 0
    onStrikeFours = 0
    onStrikeSixes = 0
    
    offStrikeRuns = 0
    offStrikeBalls = 0
    offStrikeFours = 0
    offStrikeSixes = 0
    
    drs = 2
    
    checkBowlers = []
    
    onStrike = team1BattingPlayers[0]
    onStrikeRating = team1BattingRatings[0]
    
    offStrike = team1BattingPlayers[1]
    offStrikeRating = team1BattingRatings[1]
    
    team2Bowlers = sorted(team2Bowlers,key=lambda x: x[2], reverse=True)
    team2Bowlers = sorted(team2Bowlers,key=lambda x: x[1])

    bowlerPresent = team2Bowlers[0][0]
    bowlerPresentR = team2Bowlers[0][2]
    checkBowlers.append(bowlerPresent)
    
    keeper = team2Data[team2Data['role'] == 'Keeper']['player']
    keeper = keeper.values
    
    for i in team2Bowlers:
        oneIngBowl.append([i[0],0,0,0,0,0,0])

    def changeBowler(initialBalls):
        changeB = random.choice(team2Bowlers)
        bIndex = team2Bowlers.index(changeB)
        if changeB[0] != checkBowlers[-1] and team2Bowlers[bIndex][3] < 20:
            if initialBalls == 5:
                if team2Bowlers[bIndex][3] == 5 or team2Bowlers[bIndex][3] == 15 or team2Bowlers[bIndex][3] == 0 or team2Bowlers[bIndex][3] == 10:
                    return changeB
            if initialBalls == 10:
                if team2Bowlers[bIndex][3] == 0 or team2Bowlers[bIndex][3] == 5 or team2Bowlers[bIndex][3] == 10:
                    return changeB
                elif team2Bowlers[bIndex][3] == 15:
                    return changeBowler(initialBalls)
        return changeBowler(initialBalls)
    
    print('The new batsman is {}'.format(onStrike))
    print('The new batsman is {}'.format(offStrike))
    print('The new bowler is {}'.format(bowlerPresent))
    print()
    
    for ball in range(1,101):
        time.sleep(gameRate)
        def callBatsman1R():
           if bowlerPresentR in range(71, 76):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 3
               onStrikeRating[1] = onStrikeRating[1] - 3
               onStrikeRating[2] = onStrikeRating[2] - 1
               onStrikeRating[6] = onStrikeRating[6] - 0
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.3
               onStrikeRating[4] = onStrikeRating[4] + 1.3
               onStrikeRating[5] = onStrikeRating[5] + 0.7
           elif bowlerPresentR in range(76, 81):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 5
               onStrikeRating[1] = onStrikeRating[1] - 5
               onStrikeRating[2] = onStrikeRating[2] - 3
               onStrikeRating[6] = onStrikeRating[6] - 1
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.7
               onStrikeRating[4] = onStrikeRating[4] + 2
               onStrikeRating[5] = onStrikeRating[5] + 1.5
           elif bowlerPresentR in range(81, 86):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 6
               onStrikeRating[1] = onStrikeRating[1] - 6
               onStrikeRating[2] = onStrikeRating[2] - 4
               onStrikeRating[6] = onStrikeRating[6] - 2
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 1
               onStrikeRating[4] = onStrikeRating[4] + 3
               onStrikeRating[5] = onStrikeRating[5] + 2
           elif bowlerPresentR in range(86, 91):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 7
               onStrikeRating[1] = onStrikeRating[1] - 7
               onStrikeRating[2] = onStrikeRating[2] - 5
               onStrikeRating[6] = onStrikeRating[6] - 3
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 2
               onStrikeRating[4] = onStrikeRating[4] + 4
               onStrikeRating[5] = onStrikeRating[5] + 3
           elif bowlerPresentR in range(91, 96):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 8
               onStrikeRating[1] = onStrikeRating[1] - 8
               onStrikeRating[2] = onStrikeRating[2] - 6
               onStrikeRating[6] = onStrikeRating[6] - 7
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 3
               onStrikeRating[4] = onStrikeRating[4] + 5
               onStrikeRating[5] = onStrikeRating[5] + 4
           elif bowlerPresentR in range(0,55):
               #increase
               onStrikeRating[0] = onStrikeRating[0] + 25
               onStrikeRating[1] = onStrikeRating[1] - 15
               onStrikeRating[2] = onStrikeRating[2] - 15
               onStrikeRating[6] = onStrikeRating[6] + 7
               #decrease
               onStrikeRating[3] = onStrikeRating[3] - 3
               onStrikeRating[4] = onStrikeRating[4] - 6
               onStrikeRating[5] = onStrikeRating[5] - 6
           elif bowlerPresentR in range(55,61):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 0.5
               onStrikeRating[1] = onStrikeRating[1] - 0.5
               onStrikeRating[2] = onStrikeRating[2] - 0.5
               onStrikeRating[6] = onStrikeRating[6] - 0.5
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.5
               onStrikeRating[4] = onStrikeRating[4] + 0.5
               onStrikeRating[5] = onStrikeRating[5] + 0.5
           elif bowlerPresentR in range(61,66):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 1
               onStrikeRating[1] = onStrikeRating[1] - 1
               onStrikeRating[2] = onStrikeRating[2] - 1
               onStrikeRating[6] = onStrikeRating[6] - 1
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 0.5
               onStrikeRating[4] = onStrikeRating[4] + 0.5
               onStrikeRating[5] = onStrikeRating[5] + 0.5
           elif bowlerPresentR in range(66,71):
               #increase
               onStrikeRating[0] = onStrikeRating[0] - 2
               onStrikeRating[1] = onStrikeRating[1] - 2
               onStrikeRating[2] = onStrikeRating[2] - 2
               onStrikeRating[6] = onStrikeRating[6] - 2
               #decrease
               onStrikeRating[3] = onStrikeRating[3] + 1
               onStrikeRating[4] = onStrikeRating[4] + 1
               onStrikeRating[5] = onStrikeRating[5] + 1
        
        if bowlerPresentR in range(71, 76):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 3
            onStrikeRating[1] = onStrikeRating[1] + 3
            onStrikeRating[2] = onStrikeRating[2] + 1
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.3
            onStrikeRating[4] = onStrikeRating[4] - 1.3
            onStrikeRating[5] = onStrikeRating[5] - 0.7
        elif bowlerPresentR in range(76, 81):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 5
            onStrikeRating[1] = onStrikeRating[1] + 5
            onStrikeRating[2] = onStrikeRating[2] + 3
            onStrikeRating[6] = onStrikeRating[6] + 1
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.7
            onStrikeRating[4] = onStrikeRating[4] - 2
            onStrikeRating[5] = onStrikeRating[5] - 1.5
        elif bowlerPresentR in range(81, 86):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 6
            onStrikeRating[1] = onStrikeRating[1] + 6
            onStrikeRating[2] = onStrikeRating[2] + 4
            onStrikeRating[6] = onStrikeRating[6] + 2
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 1
            onStrikeRating[4] = onStrikeRating[4] - 3
            onStrikeRating[5] = onStrikeRating[5] - 2
        elif bowlerPresentR in range(86, 91):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 7
            onStrikeRating[1] = onStrikeRating[1] + 7
            onStrikeRating[2] = onStrikeRating[2] + 5
            onStrikeRating[6] = onStrikeRating[6] + 3
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 2
            onStrikeRating[4] = onStrikeRating[4] - 4
            onStrikeRating[5] = onStrikeRating[5] - 3
        elif bowlerPresentR in range(91, 96):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 8
            onStrikeRating[1] = onStrikeRating[1] + 8
            onStrikeRating[2] = onStrikeRating[2] + 6
            onStrikeRating[6] = onStrikeRating[6] + 7
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 3
            onStrikeRating[4] = onStrikeRating[4] - 5
            onStrikeRating[5] = onStrikeRating[5] - 4
        elif bowlerPresentR in range(0,55):
            #increase
            onStrikeRating[0] = onStrikeRating[0] - 25
            onStrikeRating[1] = onStrikeRating[1] + 15
            onStrikeRating[2] = onStrikeRating[2] + 15
            onStrikeRating[6] = onStrikeRating[6] - 7
            #decrease
            onStrikeRating[3] = onStrikeRating[3] + 3
            onStrikeRating[4] = onStrikeRating[4] + 6
            onStrikeRating[5] = onStrikeRating[5] + 6
        elif bowlerPresentR in range(55,61):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 0.5
            onStrikeRating[1] = onStrikeRating[1] + 0.5
            onStrikeRating[2] = onStrikeRating[2] + 0.5
            onStrikeRating[6] = onStrikeRating[6] + 0.5
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.5
            onStrikeRating[4] = onStrikeRating[4] - 0.5
            onStrikeRating[5] = onStrikeRating[5] - 0.5
        elif bowlerPresentR in range(61,66):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 1
            onStrikeRating[1] = onStrikeRating[1] + 1
            onStrikeRating[2] = onStrikeRating[2] + 1
            onStrikeRating[6] = onStrikeRating[6] + 1
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 0.5
            onStrikeRating[4] = onStrikeRating[4] - 0.5
            onStrikeRating[5] = onStrikeRating[5] - 0.5
        elif bowlerPresentR in range(66,71):
            #increase
            onStrikeRating[0] = onStrikeRating[0] + 2
            onStrikeRating[1] = onStrikeRating[1] + 2
            onStrikeRating[2] = onStrikeRating[2] + 2
            onStrikeRating[6] = onStrikeRating[6] + 2
            #decrease
            onStrikeRating[3] = onStrikeRating[3] - 1
            onStrikeRating[4] = onStrikeRating[4] - 1
            onStrikeRating[5] = onStrikeRating[5] - 1


        
        ballOutCome = random.choices(outcomes, weights=(onStrikeRating), k=1)
        callBatsman1R()
        
        if ballOutCome == [0]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 1
            totalDots = totalDots + 1
            initialScore = initialScore + 0
            totalScore = totalScore + 0
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, dot, {}'.format(ball,bowlerPresent,onStrike,random.choice(zeroComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
        elif ballOutCome == [1]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 1
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, One Run, {}'.format(ball,bowlerPresent,onStrike,random.choice(oneComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            else:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                
        elif ballOutCome == [2]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 2
            totalScore = totalScore + 2
            
            onStrikeRuns = onStrikeRuns + 2
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, Two Runs, {}'.format(ball,bowlerPresent,onStrike,random.choice(twoComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        elif ballOutCome == [3]:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 3
            totalScore = totalScore + 3
            
            onStrikeRuns = onStrikeRuns + 3
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, Three Runs, {}'.format(ball,bowlerPresent,onStrike,random.choice(zeroComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            else:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
        elif ballOutCome == [4]:
            
            onStrikeFours = onStrikeFours + 1
            
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 4
            totalScore = totalScore + 4
            
            onStrikeRuns = onStrikeRuns + 4
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, FOUR runs, {}'.format(ball,bowlerPresent,onStrike,random.choice(fourComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        elif ballOutCome == [6]:
            
            onStrikeSixes = onStrikeSixes + 1
            
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 6
            totalScore = totalScore + 6
            
            onStrikeRuns = onStrikeRuns + 6
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, SIX !, {}'.format(ball,bowlerPresent,onStrike,random.choice(sixComm).replace('batsman', onStrike)))
            
            if ball % 10 == 0:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
            else:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
       
        elif ballOutCome == ['Out']:
            
            # initialWickets = initialWickets + 1
            # totalWickets = totalWickets + 1
            initialDots = initialDots + 1
            totalDots = totalDots + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            initialBalls = initialBalls + 1
            
            outType = random.choices(outList, weights=(0.3,4,5,0.6,0.1,4.5), k=1)
            cPlayer = random.choice(fielders)
            
            if outType == ['Caught']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {} by {}, {}'.format(ball,bowlerPresent,onStrike,*outType,cPlayer,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     c. {}     b. {}     {}({}){} [{}x4 {}x6]'.format(cPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'c. ',cPlayer, bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print()
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes 
                
            elif outType == ['Bowled']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {}, {}'.format(ball,bowlerPresent,onStrike,*outType,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'b. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
                   offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes 
                    
            elif outType == ['Stumped']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {} by {}, {}'.format(ball,bowlerPresent,onStrike,*outType,*keeper,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     st. {}     b. {}     {}({}){} [{}x4 {}x6]'.format(*keeper,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'st. ',*keeper, bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out',*keeper, '', offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes 
                    
            elif outType == ['Run Out']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                initialWickets = initialWickets - 1
                print('Ball {} - {} to {}, {} by {}, {}'.format(ball,bowlerPresent,onStrike,*outType,cPlayer,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     ro. {}     b. {}     {}({}){} [{}x4 {}x6]'.format(cPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'ro. ',cPlayer, bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out',cPlayer, "", offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes 
                    
            elif outType == ['Hit Wicket']:
                initialWickets = initialWickets + 1
                totalWickets = totalWickets + 1
                print('Ball {} - {} to {}, {}, {}'.format(ball,bowlerPresent,onStrike,*outType,random.choice(outComm).replace('batsman', onStrike)))
                print()
                print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                print()
                sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'hw. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                if totalWickets == 10:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                    oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
               offStrikeFours, offStrikeSixes, sr])
                    break
                else:
                    onStrike = team1BattingPlayers[totalWickets+1]
                    onStrikeRating = team1BattingRatings[totalWickets+1]
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes 
                    
            elif outType == ['Lbw']:
                print('Ball {} - {} to {}, {}, {}'.format(ball,bowlerPresent,onStrike,*outType,random.choice(outComm).replace('batsman', onStrike)))
                print()
                
                
                review = ['yes','no']
                reviewYN = random.choices(review, weights=(0.60,0.40), k=1)
                
                if drs == 2 or drs == 1:
                    reviewYN == ['yes']
                else:
                    reviewYN == ['no']
                
                if reviewYN == ['yes']:
                    print('Reviews available for team {} - {}'.format(team1,drs))
                    print('{} goes for a review...'.format(onStrike))
                    print('The umpire signals to the third umpire.')
  
                    umpireDecision = ['out','not out']
                    umpireNO = random.choices(umpireDecision, weights=(0.60,0.40), k=1)
                    if umpireNO == ['out']:
                        initialWickets = initialWickets + 1
                        totalWickets = totalWickets + 1
                        drs = drs - 1
                        
                        print('The umpire gives OUT ! {} departs.'.format(onStrike))
                        print()
                        print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                        print()
                        sr = (onStrikeRuns * 100) // onStrikeBalls
                        oneIngBat.append([onStrike, 'lbw. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
                       onStrikeFours, onStrikeSixes, sr])
                        if totalWickets == 10:
                            sr = (offStrikeRuns * 100) // offStrikeBalls
                            oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
                       offStrikeFours, offStrikeSixes, sr])
                            break
                        else:
                            onStrike = team1BattingPlayers[totalWickets+1]
                            onStrikeRating = team1BattingRatings[totalWickets+1]
                            
                        onStrikeBalls = 0
                        onStrikeFours = 0
                        onStrikeRuns = 0
                        onStrikeSixes = 0
                        print('The new batsman is {}'.format(onStrike))
                        
                    elif umpireNO == ['not out']:
                        print('The umpire gives NOT OUT ! and the review remains !!!')
                        print()
                        initialBalls = initialBalls + 0

                        initialDots = initialDots + 1
                        totalDots = totalDots + 1
                        initialScore = initialScore + 0
                        totalScore = totalScore + 0
                        
                        onStrikeRuns = onStrikeRuns + 0
                        onStrikeBalls = onStrikeBalls + 0
                    
                elif reviewYN == ['no']:
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    print('     b. {}     {}({}){} [{}x4 {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    sr = (onStrikeRuns * 100) // onStrikeBalls
                    oneIngBat.append([onStrike, 'lbw. ','', bowlerPresent, onStrikeRuns, onStrikeBalls, 
                   onStrikeFours, onStrikeSixes, sr])
                    if totalWickets == 10:
                        sr = (offStrikeRuns * 100) // offStrikeBalls
                        oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
                   offStrikeFours, offStrikeSixes, sr])
                        break
                    else:
                        onStrike = team1BattingPlayers[totalWickets+1]
                        onStrikeRating = team1BattingRatings[totalWickets+1]
                    onStrikeBalls = 0
                    onStrikeFours = 0
                    onStrikeRuns = 0
                    onStrikeSixes = 0
                    print('The new batsman is {}'.format(onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes   
            
            
        elif ballOutCome == ['Wide']:
            
            initialBalls = initialBalls + 0
    
            initialDots = initialDots + 0
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 0
            
            initialExtras = initialExtras + 1
            totalExtras = totalExtras + 1
            
            print('Ball {} - {} to {}, Wide Ball'.format(ball,bowlerPresent,onStrike))
            o = [0,1,2]
            b = random.choice(o)
            if b == 1:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 1
                totalScore = totalScore + 1
                
                onStrikeRuns = onStrikeRuns + 1
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, One Run'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif b == 0:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 1
                totalDots = totalDots + 1
                initialScore = initialScore + 0
                totalScore = totalScore + 0
                
                onStrikeRuns = onStrikeRuns + 0
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, dot'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif b == 2:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 2
                totalScore = totalScore + 2
                
                onStrikeRuns = onStrikeRuns + 2
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, Two Runs'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        
        elif ballOutCome == ['Leg Bye']:
            initialBalls = initialBalls + 1
    
            initialDots = initialDots + 0
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            print('Ball {} - {} to {}, Leg Bye'.format(ball,bowlerPresent,onStrike))
            
            if ball % 10 == 0:
                onStrike, offStrike = onStrike, offStrike
                onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                
                onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                
                onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            else:
                onStrike, offStrike = offStrike, onStrike
                onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                
                onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                
                onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
        elif ballOutCome == ['No Ball']:
            initialBalls = initialBalls + 0
    
            initialDots = initialDots + 0
            totalDots = totalDots + 1
            initialScore = initialScore + 1
            totalScore = totalScore + 1
            
            onStrikeRuns = onStrikeRuns + 0
            onStrikeBalls = onStrikeBalls + 1
            
            initialExtras = initialExtras + 1
            totalExtras = totalExtras + 1
            
            print('Ball {} - {} to {}, No Ball, Free Hit coming up'.format(ball,bowlerPresent,onStrike))
            
            o = [0,1,2,4,6]
            b = random.choice(o)
            if b == 1:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 1
                totalScore = totalScore + 1
                
                onStrikeRuns = onStrikeRuns + 1
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, One Run'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif b == 0:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 1
                initialScore = initialScore + 0
                totalScore = totalScore + 0
                
                onStrikeRuns = onStrikeRuns + 0
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, dot'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif b == 2:
                initialBalls = initialBalls + 1

                initialDots = initialDots + 0
                initialScore = initialScore + 2
                totalScore = totalScore + 2
                
                onStrikeRuns = onStrikeRuns + 2
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, Two Runs'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
            elif b == 4:
                onStrikeFours = onStrikeFours + 1
            
                initialBalls = initialBalls + 1
        
                initialDots = initialDots + 0
                initialScore = initialScore + 4
                totalScore = totalScore + 4
                
                onStrikeRuns = onStrikeRuns + 4
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, FOUR runs'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif b == 6:
                onStrikeSixes = onStrikeSixes + 1
            
                initialBalls = initialBalls + 1
        
                initialDots = initialDots + 0
                initialScore = initialScore + 6
                totalScore = totalScore + 6
                
                onStrikeRuns = onStrikeRuns + 6
                onStrikeBalls = onStrikeBalls + 1
                
                print('Ball {} - {} to {}, SIX !'.format(ball,bowlerPresent,onStrike))
                
                if ball % 10 == 0:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRating, offStrikeRating = offStrikeRating, onStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRating, offStrikeRating = onStrikeRating, offStrikeRating
                    
                    onStrikeRuns, offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
        
        if ball % 5 == 0 and ball % 10 != 0:

            chance = ['no','yes']
            chB = random.choices(chance, weights=(0.75,0.25), k=1)
            if chB == ['no']:
                pass
            elif chB == ['yes']:
                for i in oneIngBowl:
                    if bowlerPresent == i[0]:
                        bSIndex = oneIngBowl.index(i)
                        oneIngBowl[bSIndex][1] = oneIngBowl[bSIndex][1] + initialBalls
                        oneIngBowl[bSIndex][2] = oneIngBowl[bSIndex][2] + initialDots
                        oneIngBowl[bSIndex][3] = oneIngBowl[bSIndex][3] + initialScore
                        oneIngBowl[bSIndex][4] = oneIngBowl[bSIndex][4] + initialWickets
                        oneIngBowl[bSIndex][5] = round(oneIngBowl[bSIndex][3]/oneIngBowl[bSIndex][1],2)
                        oneIngBowl[bSIndex][6] = oneIngBowl[bSIndex][6] + initialExtras
                 
                for i in team2Bowlers:
                    if i[0] == bowlerPresent:
                        bIndex = team2Bowlers.index(i)
                        team2Bowlers[bIndex][3] = team2Bowlers[bIndex][3] + 5

                print()
                print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
                print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
                rr = totalScore / ball
                print('     RR - {}'.format(round(rr,2)))
                print()
                print('     {}     ({}){}  [{}x4, {}x6]'.format(onStrike,onStrikeRuns,
                                                              onStrikeBalls,onStrikeFours,onStrikeSixes))
                print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                            offStrikeBalls,offStrikeFours,offStrikeSixes))
                print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
                print()
                
                flag = True
                checkBowlers.append(bowlerPresent)
                changeB = changeBowler(5)
                
                initialBalls = 0
                initialDots = 0
                initialExtras = 0
                initialScore = 0
                initialWickets = 0
                
                
                bowlerPresent = changeB[0]
                bowlerPresentR = changeB[2]
                print()
                print('Change of bowler')
                print('The new bowler is {}'.format(changeB[0]))
                print()
                
        if ball % 10 == 0:
            for i in oneIngBowl:
                if bowlerPresent == i[0]:
                    bSIndex = oneIngBowl.index(i)
                    oneIngBowl[bSIndex][1] = oneIngBowl[bSIndex][1] + initialBalls
                    oneIngBowl[bSIndex][2] = oneIngBowl[bSIndex][2] + initialDots
                    oneIngBowl[bSIndex][3] = oneIngBowl[bSIndex][3] + initialScore
                    oneIngBowl[bSIndex][4] = oneIngBowl[bSIndex][4] + initialWickets
                    oneIngBowl[bSIndex][5] = round(oneIngBowl[bSIndex][3]/oneIngBowl[bSIndex][1],2)
                    oneIngBowl[bSIndex][6] = oneIngBowl[bSIndex][6] + initialExtras
                    
            print()
            print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
            print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
            rr = totalScore / ball
            print('     RR - {}'.format(round(rr,2)))
            print()
            print('     {}     ({}){}  [{}x4, {}x6]'.format(onStrike,onStrikeRuns,
                                                             onStrikeBalls,onStrikeFours,onStrikeSixes))
            print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                            offStrikeBalls,offStrikeFours,offStrikeSixes))
            print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
            print()
            
            # print()
            for i in team2Bowlers:
                if i[0] == bowlerPresent:
                    bIndex = team2Bowlers.index(i)
                    if flag == True:
                        team2Bowlers[bIndex][3] = team2Bowlers[bIndex][3] + 5
                    elif flag == False:
                        team2Bowlers[bIndex][3] = team2Bowlers[bIndex][3] + 10
            
            checkBowlers.append(bowlerPresent)
            changeB = changeBowler(10)
            
            initialBalls = 0
            initialDots = 0
            initialExtras = 0
            initialScore = 0
            initialWickets = 0
            flag = False
            
            bowlerPresent = changeB[0]
            bowlerPresentR = changeB[2]
            if ball != 100:
                print()
                print('The new bowler is {}'.format(changeB[0]))
                print()
            
            if ball == 100 and totalWickets != 10:
                if onStrikeBalls == 0:
                    sr = 0
                else:
                    sr = (onStrikeRuns * 100) // onStrikeBalls
                oneIngBat.append([onStrike, 'Not Out','', '', onStrikeRuns, onStrikeBalls, 
               onStrikeFours, onStrikeSixes, sr])
                
                if ball == 100 and ballOutCome == ['Out']:
                    offStrikeBalls = offStrikeBalls + 1
                else:
                    sr = (offStrikeRuns * 100) // offStrikeBalls
                
                oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
            offStrikeFours, offStrikeSixes, sr])
                
                
            if totalWickets == 10:
                
                sr = (offStrikeRuns * 100) // offStrikeBalls
                oneIngBat.append([offStrike, 'Not Out','', '', offStrikeRuns, offStrikeBalls, 
            offStrikeFours, offStrikeSixes, sr])
                
                for i in oneIngBowl:
                    if bowlerPresent == i[0]:
                        bSIndex = oneIngBowl.index(i)
                        oneIngBowl[bSIndex][1] = oneIngBowl[bSIndex][1] + initialBalls
                        oneIngBowl[bSIndex][2] = oneIngBowl[bSIndex][2] + initialDots
                        oneIngBowl[bSIndex][3] = oneIngBowl[bSIndex][3] + initialScore
                        oneIngBowl[bSIndex][4] = oneIngBowl[bSIndex][4] + initialWickets
                        oneIngBowl[bSIndex][5] = round(oneIngBowl[bSIndex][3]/oneIngBowl[bSIndex][1],2)
                        oneIngBowl[bSIndex][6] = oneIngBowl[bSIndex][6] + initialExtras
    
        if totalWickets == 10 and ball != 100:
                    print()
                    print('     End of innings')
                    print('     End of {} balls - {} runs'.format(initialBalls,initialScore))
                    print('     {}     {}-{}'.format(team1,totalScore,totalWickets))
                    print()
                    print('     {}     ({}){}  [{}x4, {}x6]'.format(offStrike,offStrikeRuns,
                                                                    offStrikeBalls,offStrikeFours,offStrikeSixes))
                    print('     {}     {}-{}-{}-{}'.format(bowlerPresent, oneIngBowl[bSIndex][1], oneIngBowl[bSIndex][2], oneIngBowl[bSIndex][3], oneIngBowl[bSIndex][4]))
                    print()
    
    print('{} 1st Innings'.format(team1))
    
    for i in range(len(team1BattingPlayers)):
        j = i
        while j < len(oneIngBat) and oneIngBat[j][0] != team1BattingPlayers[i]:
            j = j + 1
            if j < len(oneIngBat) and oneIngBat[j][0] == team1BattingPlayers[i]:
                oneIngBat[i],oneIngBat[j] = oneIngBat[j],oneIngBat[i]
    
    print()
    df = pd.DataFrame(oneIngBat, columns =['Batsman','','Fielder','Bowler','Runs','Balls','4s','6s','SR'])
    print(tabulate(df, showindex=False, headers=df.columns))
    dnb = df['Batsman'].to_list()
    dnb = list(set(team1BattingPlayers) - set(dnb))
    print()
    rr = totalScore / ball
    print('   Total:   {}/{}        Balls: {}        Run Rate: {}        Extras: {}'.format(totalScore,totalWickets,ball,round(rr,2),totalExtras))
    print()
    if len(dnb) == 0:
        print('DNB : Nil')
    else: 
        print('DNB : ',dnb)
    print()
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    bat = path+team1+'-batting'+timestr+'.csv'
    df.to_csv(bat)
    
    print('{} Bowling Scoreboard'.format(team2))
    print()
    df1 = pd.DataFrame(oneIngBowl,columns=['Bowler','Balls','Dots','Runs','Wickets','Economy','Extras'])
    print(tabulate(df1, showindex=False, headers=df1.columns))
    print()
    print('   Total:   {}/{}        Balls: {}        Run Rate: {}        Extras: {}'.format(totalScore,totalWickets,ball,round(rr,2),totalExtras))
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    ballP = path+team2+'-bowling'+timestr+'.csv'
    df1.to_csv(ballP)
    
    target = totalScore + 1
    rrr = target / 100
    print()
    print()
    # print(team2+' need '+str(target)+' runs in 100 balls at '+str(round(rrr,2))+' run/s per ball.')
    print('{} need {} runs in 100 balls at {} run/s per ball !'.format(team2,target,round(rrr,2)))
    print()
    print()
    
    team1Stats.append([team1,totalScore,totalWickets,ball])
    
    team1, team2 = team2, team1
    prepInnings2(team1, team2, target)
    
#Checking for teams data
os.chdir('./')
result = glob.glob( '*.csv' )
print('Avaliable teams: ',result)

for i in range(1):
    team1 = int(input("Enter team 1 index: "))
    team1 = result[team1 - 1].replace('.csv', '')
    team2 = int(input("Enter team 2 index: "))
    team2 = result[team2 - 1].replace('.csv', '')

#saving output to file opening
parent_dir = "./"
timestr = time.strftime("%Y%m%d-%H%M%S")
directory = team1+' vs '+team2+'-'+timestr
path = os.path.join(parent_dir, directory) 
os.mkdir(path)
 
# stdoutOrigin = sys.stdout
path = './'+path+'/'
filename = team1+' vs '+team2+'-'+timestr+'.log' 

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(path+filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

print()
print('{}  vs {}'.format(team1, team2))
print()

#toss options
toss = ['Heads','Tails']
tossChoice = random.choice(toss)

#2nd team toss call and generating random option (Away team choice)
#Dhoni spins the coin "Williamson choose tails".
tossCall = ['Heads', 'Tails']
team2Call = random.choice(tossCall)

#Generating toss
print('- x -')
print()
print('{} spins the coin'.format(team1))
print('{} - {} is the call. And its {}'.format(team2, team2Call, tossChoice))
# print(team1+" spins the coin \n"+team2+" - "+team2Call+" is the call. And it's "+tossChoice)

#Setting up who wont the toss and what they want to choose first.
firstChoice = ['Bat','Bowl']
firstChoiceCall = random.choice(firstChoice)
#Checking if team 2 toss call is same with coin toss or not
if team2Call == tossChoice:
    # print(team2+' won the toss and choose to '+firstChoiceCall+' first !')
    print('{} won the toss and choose to {} first !'.format(team2,firstChoiceCall))
    print()
    print('- x -')
    print()
    if firstChoiceCall == 'Bowl':
        team1, team2 = team1, team2
        prepInnings(team1, team2)

    elif firstChoiceCall == 'Bat':
        team1, team2 = team2, team1
        prepInnings(team1, team2)    
else:
    # print(team1+' won the toss and choose to '+firstChoiceCall+' first !')
    print('{} won the toss and choose to {} first !'.format(team1,firstChoiceCall))
    print()
    print('- x -')
    print()
    if firstChoiceCall == 'Bowl':
        team1, team2 = team2, team1
        prepInnings(team1, team2)

    elif firstChoiceCall == 'Bat':
        team1, team2 = team1, team2
        prepInnings(team1, team2)
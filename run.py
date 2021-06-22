'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file is the run engine of our game. It has two modes: a play mode and a normal mode.
'''
import time
from game import Game
import os
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Memory,
    Teleport,
    LetterFragment
)

def play_mode(commands):
    lvl = '=====================\n' \
        '====== LEVEL {} ======\n' \
        '=====================\n'.format(game.level)
    invalid = Wall()

    X = Start()
    X.starting(game)

    print('\n' + lvl)
    print(game.gridstr())

    while True:
        move = input('Input a move: ').lower()

        if move not in game.conditions:
            os.system('clear')
            print(lvl)
            print(game.gridstr())
            print('❗️Please enter a valid move (w, a, s, d, e, q).❗️\n')
        
        elif move == 'c':
            os.system('clear')
            print(lvl)
            print(game.gridstr())
            print(commands)
        
        elif move == 'q':
            print('\nBye!')
            exit()
        
        else:
            os.system('clear')
            print(lvl)
            game.game_move(move)
            
            if not game.IsValid():
                invalid.step(game)

            else:
                if game.grid[game.player.row][game.player.col].step(game) == True:
                    if game.level == 6:
                        game.player.display = "🙎🏻‍♀️"
                        
                        for i in range(2):
                            game.game_move('s')
                    break

intro_disp = '===================\n' \
            '====== INTRO ======\n' \
            '==================='   
intro = "\nTyler is currently lost, and Seletti has been tasked to find him. Seletti knows Tyler left her a letter, but it is scatter within a forest. " \
        "So, she tasks Bunny to find the letter. Bunny walks in to find the letter torn to pieces due to a terrible storm that occurred, leaving parts of the forest " \
        "on fire. Pillow has left Tyler's memory fragments of Sel scattered throughout the forest which will instantly put out the fires.\n"

task = "❗️Your Task❗️" \
       "\nCollect all memory fragments (💖) to put out the fires (🔥) which are blocking the exit (🏁) to the next part of forest! " \
        "However, remember to collect parts of Tyler's letter (📝), as it will help Seletti find him!\n"

commands = "🎮 The Commands 🎮\n" \
           "\t🕹 w = Move up\n" \
           "\t🕹 s = Move down\n" \
           "\t🕹 a = Move left\n" \
           "\t🕹 d = Move right\n" \
           "\t🕹 e = Wait on the spot\n\n" \
           "\t❗️c = Prints out the commands\n" \
           "\t❗️q = Quits the game\n" \

print(intro_disp)
time.sleep(1)
print(intro)
time.sleep(5)
print(task)
time.sleep(5)
print(commands)
time.sleep(5)

level = 0
while level < 6:
    filename = "level{}.txt".format(level + 1)
    game = Game(filename, level + 1)

    play_mode(commands)
    os.system('clear')

    level += 1

    if (level < 6):
        disp = '==================================\n' \
               '====== ADVANCING TO LEVEL {} ======\n' \
               '=================================='.format(level + 1) 
        
        print(disp)

    else:
        print("⭐️ Bunny has found all letter fragments! He pieces it together and gives it to Seletti. She begins to read. ⭐️\n")
    
    time.sleep(1)

intro_disp = '====================\n' \
             '====== LETTER ======\n' \
             '===================='   
        
with open("letter.txt", 'r') as letter:
    txt = letter.readlines()
    print(''.join(txt))

print('') 
for row in range(6):  
    for col in range(7):  
        if (row==0 and col %3 !=0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):  
            print("💖",end=" ")  
        else:  
            print(end=" ")  
    print() 
print("\nHappy six months Sel! 👩‍❤️‍💋‍👨")
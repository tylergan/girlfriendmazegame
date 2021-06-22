'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: Store all my classes in this file which will be used to create my objects in my maze.

Note: Each Class has a solve() and a ValidStep() instance method; this is specific to my BFS/DFS algorithm.
    • solve() --> used to determine whether the move is valid.
    • ValidStep() --> used to conduct a VALID instance method within the game.
'''

class Start:
    def __init__(self):
        self.display = '💮'

    def step(self, game):
        print(game.gridstr()) #only prints the board

    def starting(self, game):
        '''Finds the starting coordinates of where the player should START in respect to X
        
        Returns:
            • Starting player coordinates
        '''

        i = 0
        while i < len(game.grid):
            j = 0
            while j < len(game.grid[i]):
                if game.grid[i][j].display == self.display: #we will update our player's coordinates to match the starting coordinates
                    game.player.row = i
                    game.player.col = j
                    break

                j += 1
        
            i += 1
    
class End:
    def __init__(self):
        self.display = '🏁'

    def step(self, game):
        '''If we are able to reach this object (Y), we win the game and end the game. 
        
        Returns:
            • A congratulatory message with a history of the moves we have made and the number of moves we have made.
        '''

        print(game.gridstr())

        if game.player.have_letter == False:
            print("❗️ You need to collect the fragments of Tyler's letter (📝) before finishing the level! ❗️\n")

        return game.player.have_letter

class Air:
    def __init__(self):
        self.display = '  '

    def step(self, game):

        print(game.gridstr())


class Wall:
    def __init__(self):
        self.display = '🌲'

    def step(self, game):
        '''This ensures we cannot move through walls.
        '''

        if game.moves[-1] == 'w':
            game.player.move('s')

        elif game.moves[-1] == 's':
            game.player.move('w')

        elif game.moves[-1] == 'a':
            game.player.move('d')
            
        elif game.moves[-1] == 'd':
            game.player.move('a')
        
        del game.moves[-1]

        print(game.gridstr())
    
class Fire:
    def __init__(self):
        self.display = '🔥'

    def step(self, game):
        '''This will determine two things: whether you lose the game or whether you extinguish a fire.

        You may only extinguish a fire if you have one or more water buckets. Otherwise, you lose.
        '''
        invalid = Wall()
        invalid.step(game)
        print("❗️ You need to collect all of Tyler's memory fragments (💖)! ❗️\n")


class Memory:
    def __init__(self):
        self.display = '💖'

    def step(self, game):
        '''Things I love about Seletti.
        '''
        game.player.memory_fragments += 1

        game.grid[game.player.row][game.player.col] = Air()

        if (game.player.memory_fragments == game.level):
            i = 0
            while i < len(game.grid):
                j = 0
                while j < len(game.grid[i]):
                    if (game.grid[i][j].display == '🔥'):
                        game.grid[i][j] = Air()
                    
                    j += 1

                i += 1

        print(game.gridstr()) 

        print('========================\n' \
            '====== MEMORY LOG ======\n' \
            '========================\n' )
        if (game.level == 1):
            if (game.player.memory_fragments == 1):
                print("Perhaps the boldest, yet best decision I ever made was to approach the pretty girl cleaning her dishes on the sixth floor. " \
                      "I remember the time I gave her my keycard to wake me up. When it was time to wake me up, she tried to scare me by turning her alarm on near me. " \
                      "Little did she know that I was well aware she of what she was up to, but from that moment on, I knew this girl was special...\n")
        
        elif (game.level == 2):
            if (game.player.memory_fragments == 1):
                print("I remember when she gave me those sticky notes. I love them all, but my favourite is the bunny as it reminds me of her... and Bunny.\n" \
                      "And how could I forget about the message she wrote for my on the first coffee drink she ever got me. The message still sticks with me to this day:" \
                      "'Never forget to smile!' 😁\n")
            else:
                print("I remember when we went to Ume Bar near Surry Hills. You ordered the regular burger with the alcoholic plum drink and lotus plum chips. " \
                      "I ordered a regular katsu burger with french fries. Our first monthly celebration! 🍔\n")
        
        elif (game.level == 3):
            if (game.player.memory_fragments == 1):
                print("I remember the first time we went to IKEA to get my lamp together. We went there initially thinking of getting something to eat, but the restaurant was closed. " \
                      "So, we went to the cafe which was just after the cashier... I wonder if she remembers what she ordered... 🌭🍦\n")
            elif (game.player.memory_fragments == 2):
                print("And I really enjoyed us muchking around at Decathalon. We played with the bicycles, soccer and rugby balls. I tried to show off, but maybe I was too full " \
                      "from all the hotdogs we ordered at IKEA to impress her with my sporting skills... not that I'm any good... ⚽️🏉\n")
            else:
                print("For our third month celebration, we went to Mamak's village. I ordered the beef rendang and vegetables while Sel ordered the satay sticks. Note to self: " \
                      "Do not bring her there again! She did not like the food! 🤢 However, we did go to a BBQ celebration with all my friends, where we shared our first alcoholic beverage together.\n")
        
        elif (game.level == 4):
            if (game.player.memory_fragments == 1):
                print("The fourth month was a special month. During COVID, I got sick which made everyone worried that I had contracted the virus, influencing a lot of people to stay away " \
                      "from me. However, the one person that always remained by my side was Sel. She showed me a level of care and love that only my family would give me.\n\n" \
                      "I truly felt at home. 💗]\n")
            elif (game.player.memory_fragments == 2):
                print("Does Sel also remember the first time we went to get scones together at Tea Cosy? I am so grateful that I was able to share my favourite scone place with someone, but I am " \
                      "even more grateful that 'someone' was Sel. I even have the photos of us there!\n")
            elif (game.player.memory_fragments == 3):
                print("We also went to Manly beach together. There, she introduced me to Betty's Burgers, which has to be my favourite burgers in Sydney... given the cheapness of the burger. " \
                      "We also hiked to the top of a rock, where we both got to enjoy the view of the ocean. 🌊\n")
            else:
                print("I will never forget when Sel wrote me that exam timetable with a sidenote saying, 'goodluck babe!'. She makes me feel so special, and I hope I make her feel special too.\n")
        
        elif (game.level == 5):
            if (game.player.memory_fragments == 1):
                print("I remember going out, late at night, with Josh to go and eat Pancakes. I really wanted Sel to come, so I invited her. Little did I know that she was drunk out of her " \
                      "mind. Both Josh and I were worried given how she could not walk straight and how she began puking as we walked to The Rocks. However, that night was a pivotal shift in my life. " \
                      "Never before did I properly take care of someone with great levels of concern and emotion. It had struck my that I was becoming more loving and caring... all thanks to Sel.\n")
            elif (game.player.memory_fragments == 2):
                print("I am so grateful that we went to Canberra together. When we went to the War Memorial, Parliament and Thredbo, the most important thing was that I had Sel " \
                      "by my side. It made that trip just that more special... 💖\n")
            elif (game.player.memory_fragments == 3):
                print("I remember when we had that big argument with each other. The old Sel would have stopped talking to me for days. Yet, right after the argument, Sel willingly went to " \
                      "Centennial Park with me. I got to experience such a beautiful environment with the most beautiful girl by my side. " \
                      "After Centennial Park, Sel took me to Spciy Joint. She ordered cold chicken and noodles, pork, rice and delicious steam buns with custard. It is one of my favourite " \
                      "restaurants here in Sydney, and I got to enjoy it with my favourite person.\n")
            elif (game.player.memory_fragments == 4):
                print("I also remember when I picked Sel up from Redfern station after coming back from Hunter Valley. It was like picking up a child from school as she dressed like nine-year old. " \
                      "However, I was so happy to see her, and it made me realise that not having her by my side made me miss her that much more. " \
                      "By not having her by my side, I am incomeplete. But, with her by my side, she makes me whole. 💓\n")
            else:
                print("How could I forget Coogee beach. I prepared two chicken sandwiches, while Sel brought a mat, frisbee and premium Cider from Hunter Valley. Once we arrived, we ate our food, " \
                      "had our drinks and played a bit of frisbee. However, the most memorable part for me was holding Sel in my embrace as we watched the beautiful sky turn from blue to shades of " \
                      "pink, purple and blue. The sky was beautiful, but it was not nearly as beautful as Sel...\n")
        
        elif (game.level == 6):
            if (game.player.memory_fragments == 1):
                print("And so here we are... Six months of dating. We have been through a lot over the past few months of dating. We have had a lot of ups and downs in this relationship.\n")
            elif (game.player.memory_fragments == 2):
                print("Thanks to Sel, I have grown up to be a different person. The most important thing Sel taught me is to love and care for others, and that is something I can never take away from her.\n")
            elif (game.player.memory_fragments == 3):
                print("I can see that Sel is making some truly remarkable changes in her life in order to continue loving me for who I am as a person. I know I am not the easiest person to be with, " \
                      "but the fact that you have stayed with me for so long when so many other people would have walked out shows that you are truly someone I would not want to lose.\n")
            elif (game.player.memory_fragments == 4):
                print("Six months may seem long, but we still have such a long way to go. However, I would not have it any other way than to spend the good and the bad with you.\n")
            elif (game.player.memory_fragments == 5):
                print("You are my kind, loving, pew pew in crime, and I would not have spent my last six months, and I cannot wait for the adventures we have ahead of ourselves.\n")
            else:
                print("You truly are a 'once in a blue moon' individual.\n\n I love you, Sel.\n")
            
        print('========================\n' \
            '====== END MEMORY ======\n' \
            '========================\n' )
        
        if (game.player.memory_fragments == game.level):
            print('❗️ You have collected all memory fragments. The flames have been extinguised! 💦\n')

class LetterFragment:
    def __init__(self):
        self.display = "📝"

    def step(self, game): 
        game.player.have_letter = True
        game.grid[game.player.row][game.player.col] = Air()
        print(game.gridstr()) 

        print('=============================\n' \
            '====== LETTER FRAGMENT ======\n' \
            '=============================\n' )

        if (game.level == 1):
            print("... Do I need to remind you that there is a 1/562 chance of falling in love with someone on any given day?\n")      
        elif (game.level == 2):
            print("... However, I want to divert away from the standard ‘recall the past’ component and get straight into something very special...\n")  
        elif (game.level == 3):
            print("... no matter how much I tried to push you away, you never seemed to stop caring for me...\n")  
        elif (game.level == 4):
            print("... The moment you took care of me when I was sick when very few people were willing to look after me touched me emotionally...\n")  
        elif (game.level == 5):
            print("... You may not know this, but my parents said that if there is one thing they have noticed after I started dating you... \n")  
        elif (game.level == 6):
            print("It is not you versus me. It is ’us’ versus the world, and I would not have it any other way...\n")
        
        print('========================\n' \
            '====== LETTER END ======\n' \
            '========================\n' )

        if (game.level < 6):
            print("⭐️ Parts of the letter are missing. Looks like bunny needs to collect the remaining fragments to let Seletti read herself. ⭐️\n")
            print("❗️ You have collected a fragment of Tyler's letter! You may enter the portal to the next realm! ❗️\n") 
        else:
            print("❗️ You have collected ALL the fragments of Tyler's letter! You should quickly give it to Sel! ❗️\n") 
        

class Teleport:
    def __init__(self):
        self.display = 0

    def step(self, game):
        '''An instance method that will teleport a player from a particular teleporter location to another teleporter location
        '''

        #starting indexes to conduct the "brute force" method and find the mathcing number of that pair in the matrix
        i = game.player.row 
        j = game.player.col + 1 

        while i < len(game.grid):

            while j < len(game.grid[i]):
                if game.grid[i][j].display == game.grid[game.player.row][game.player.col].display: 
                    game.player.row = i
                    game.player.col = j
                    
                    print(game.gridstr())
                    print('⭐️ Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time. ⭐️\n')
                    
                    return (game.player.row, game.player.col)

                j += 1
            
            j = 0 #reset j to 0
            i += 1

            if i == len(game.grid) - 1: #we want to reset the coordinate to 0 to start from the top of the matrix again to search for our matching element.
                i = 0
from game import *

while True:
    x_input = input("Please choose the player type for 'X':\n1. Human\n2. CPU\n")
    if x_input == 1:
        x_player = HumanPlayer()
        break
        
    elif x_input == 2:
        while True:
            x_ai_input = input("Please choose the AI type for 'X':\n1. Perfect\n2. Random\n")
            if x_ai_input == 1:
                x_ai = PerfectAI()
                break
            elif x_ai_input == 2:
                x_ai = RandomAI()
                break
            else:
                print "Invalid input. Please try again."
        x_player = CPUPlayer(x_ai)
        break
        
    else:
        print "Invalid input. Please try again."
        
while True:
    o_input = input("Please choose the player type for 'O':\n1. Human\n2. CPU\n")
    if o_input == 1:
        o_player = HumanPlayer()
        break
        
    elif o_input == 2:
        while True:
            o_ai_input = input("Please choose the AI type for 'O':\n1. Perfect\n2. Random\n")
            if o_ai_input == 1:
                o_ai = PerfectAI()
                break
            elif o_ai_input == 2:
                o_ai = RandomAI()
                break
            else:
                print "Invalid input. Please try again."
        o_player = CPUPlayer(o_ai)
        break
        
    else:
        print "Invalid input. Please try again."

print 'Instructions:'
print 'Click to perform a move as a human player or click to tell an AI player to perform a move.'
print 'Note: A perfect CPU AI may require several seconds to compute the next move.'
Game(x_player, o_player)


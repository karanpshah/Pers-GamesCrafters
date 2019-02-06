#Coin Game: Game Code and Solver
#Print facility at bottom for values of all game positions

def do_move(posn, adv):
    return posn - adv

def game_over(posn):
    if posn > 0 and posn <= 10:
        return False
    else:
        return True

def generate_moves(posn):
    if posn == 1:
        return [1]
    else:
        return [1,2]

def solve(posn):

    if not (game_over(posn)):

        if (posn == 1) or (posn == 2):
            return 'W'

        else:
            moves_lst = generate_moves(posn)
            outcomes_lst = [solve(do_move(posn, move)) for move in moves_lst]

            lst_len = len(outcomes_lst)
            index = 0
            L_present = False

            while index < lst_len:

                if (outcomes_lst[index] == 'L'):
                    # Can send opponent to losing position
                    L_present = True

                index+= 1;

            if (L_present == True):
                # If can send opponent to losing position,
                # this is a winning position. Ret. 'W'
                return 'W'
            else:
                return 'L'


# Call to Value for Printing All Positions
print("Game Call To Value on All Positions\n\n")
i = 10
while i > 0:
    print("Solve({0}): {1}".format(i, solve(i)))
    i -= 1

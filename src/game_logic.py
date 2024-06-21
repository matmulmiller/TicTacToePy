def draw(b):
    print( '   |   |   ')
    print(f' {b[1]} | {b[2]} | {b[3]}  ')
    print( '---+---+---')
    print( '   |   |   ')
    print(f' {b[4]} | {b[5]} | {b[6]} ')
    print( '   |   |   ')
    print( '---+---+---')
    print(f' {b[7]} | {b[8]} | {b[9]} ')
    print( '   |   |   ')


def check_win(b):
    if b[1] == b[2] == b[3]==('x' or 'o'):
        game_over = True

    elif b[4] == b[5] == b[6]==('x' or 'o'):
        game_over = True

    elif b[7] == b[8] == b[9]==('x' or 'o'):
        game_over = True
    
    elif b[1] == b[5] == b[9]==('x' or 'o'):
        game_over = True

    elif b[3] == b[5] == b[7]==('x' or 'o'):
        game_over = True

    elif b[1] == b[4] == b[7]==('x' or 'o'):
        game_over = True

    elif b[2] == b[5] == b[8]==('x' or 'o'):
        game_over = True

    elif b[3] == b[6] == b[9]==('x' or 'o'):
        game_over = True

    else:
        game_over = False

    return game_over

def player_move(b):
    loc = input("Enter board location: ")
    b[int(loc)] = 'x'
    return b

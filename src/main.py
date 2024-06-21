from game_logic import draw, player_move, check_win 

def main():
    board  = {1: 'x', 2: ' ', 3: 'o',
              4: 'x', 5: 'o', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}
    win = False

    while not win:

        draw(board)
        board = player_move(board)
        win = check_win(board)
        if win:
            draw(board)
            print("You Won! Bitch.")

    

if __name__ == '__main__':
    main()

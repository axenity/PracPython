import curses

def main(stdscr):
    curses.curs_set(0) # hide cursor
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        draw_board(stdscr, board)
        x, y = get_move(stdscr, board)
        if not (0 <= x < 3 and 0 <= y < 3) or board[x][y] != ' ':
            continue
        board[x][y] = player
        if check_win(board, player):
            draw_board(stdscr, board)
            stdscr.addstr(5, 2, f'Player {player} wins!')
            stdscr.getch()
            break
        player = 'O' if player == 'X' else 'X'

def draw_board(stdscr, board):
    for i in range(3):
        for j in range(3):
            symbol = board[i][j]
            color = 0
            if symbol == 'X':
                color = 2
            elif symbol == 'O':
                color = 3
            stdscr.addstr(i*2, j*2, symbol, curses.color_pair(color))
    stdscr.refresh()

def get_move(stdscr, board):
    stdscr.move(3, 0)
    stdscr.addstr(3, 0, 'Enter move (x y): ', curses.color_pair(1))
    stdscr.refresh()
    while True:
        try:
            move = stdscr.getstr(3, 18, 2).decode()
            x, y = map(int, move.split())
            return x, y
        except:
            pass

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

curses.wrapper(main)
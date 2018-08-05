
def get_avaiable_moves(board_state):
    '''get all possibles moves on the state of the board'''
    moves = []
    for colume in range(7):
        if board_state[0][colume] == 0:
            moves.append(colume)
    return moves

    avaiable_moves = []
    for i in range(7):
        if int(board[0][i]) == 0:
            avaiable_moves.append(i)
    return avaiable_moves

def row_check(board, col):
    for row in range(5, -1, -1):  # check from bottom up
        if int(board[row][col]) == 0:
            return row
    if int(board[0][col]) != 0:
        return -1  # -1 flag to trigger a call

def win_check(board, move, tile):
    #vertical
    counter = 0
    row = move[0]
    col = move[1]
    for r in range(3):
        if (board[r][col] == tile) and (board[r+1][col] == tile) and (board[r+2][col]== tile) and (board [r+3][col] == tile):
            return True
    # horizontal check
    for c in range(4):
        if (board[row][c]==tile) and (board[row][c+1] == tile) and (board[row][c+2]== tile) and (board[row][c+3] == tile):
            return True

    # positive slope diagonal checks
    temp_r = row
    temp_c = col
    while (temp_r >=0 and temp_c <= 6):
        if(board[temp_r][temp_c]== tile):
            counter +=1
            temp_r -=1
            temp_c +=1
        else:
            break
    #reset
    temp_r = row
    temp_c = col
    while (temp_r <= 5 and temp_c >= 0):
        if(board[temp_r][temp_c]==tile):
            counter +=1
            temp_r += 1
            temp_c -=1
        else:
            break

    if counter >=5:
        return True

##############################################################
    # negative slope diagonal checks
    counter =0
    temp_r = row
    temp_c = col
    while(temp_r >= 0 and temp_c >=0):
        if(board[temp_r][temp_c]==tile):
            counter +=1
            temp_r -=1
            temp_c -=1
        else:
            break

    temp_r = row
    temp_c = col
    while(temp_r <= 5 and temp_c <=6 ):
        if(board[temp_r][temp_c]==tile):
            counter += 1
            temp_r += 1
            temp_c += 1
        else:
            break

    if counter >=5:
        return True

    return False

def three_check(board, move, tile):
    score =0
    row= move[0]
    col = move[1]
    counter =0
    # vertical threes
    for r in range(4):
        if (board[r][col] == tile) and (board[r+1][col] == tile) and (board[r+2][col] == tile):
            score += 10
    # horizontal threes
    for c in range(5):
        if (board[row][c] == tile) and (board[row][c+1] == tile) and (board[row][c+2] == tile):
            score +=10

        # positive slope diagonal checks
    temp_r = row
    temp_c = col
    while (temp_r >= 0 and temp_c <= 6):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r -= 1
            temp_c += 1
        else:
            break
    # reset
    temp_r = row
    temp_c = col
    while (temp_r <= 5 and temp_c >= 0):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r += 1
            temp_c -= 1
        else:
            break

    if counter >= 4:
        score += 10

        ##############################################################
    # negative slope diagonal checks
    counter = 0
    temp_r = row
    temp_c = col
    while (temp_r >= 0 and temp_c >= 0):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r -= 1
            temp_c -= 1
        else:
            break

    temp_r = row
    temp_c = col
    while (temp_r <= 5 and temp_c <= 6):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r += 1
            temp_c += 1
        else:
            break

    if counter >= 4:
        score += 10

    return score

def disjointed_set(board, move, tile):
    '''checks for certain patterns and ETC'''
    row = move[0]
    col = move[1]
    points = 0
   #for three in a rows with empty space on both sides:
    for c in range(3):
        if board[row][c] == 0 and board[row][c+1] == tile and board[row][c+2] == tile and board[row][c+3] == tile and board[row][c+4]==0:
            points += 500

    #for[1][1][0][1] type connections

    for c in range (4):
        if board[row][c] == 1 and board[row][c+1]==1 and board[row][c+2] == 0 and board[row][c+3]==1:
            points +=50

    #for[1][0][1][1] type connections

    for c in range(4):
        if board[row][c] == 1 and board[row][c + 1] == 0 and board[row][c + 2] == 1 and board[row][c + 3] == 1:
            points += 50

    #for mid column row(gives most possiblilties
    if (col) == 3:
        points += 10

    return points

def two_check(board, move, tile):
    score = 0
    row = move[0]
    col = move[1]
    counter = 0
    # vertical threes
    for r in range(5):
        if (board[r][col] == tile) and (board[r + 1][col] == tile):
            score += 5
    # horizontal threes
    for c in range(6):
        if (board[row][c] == tile) and (board[row][c + 1] == tile):
            score += 5

            # positive slope diagonal checks
    temp_r = row
    temp_c = col
    while (temp_r >= 0 and temp_c <= 6):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r -= 1
            temp_c += 1
        else:
            break
    # reset
    temp_r = row
    temp_c = col
    while (temp_r <= 5 and temp_c >= 0):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r += 1
            temp_c -= 1
        else:
            break

    if counter >= 3:
        score += 5

        ##############################################################
    # negative slope diagonal checks
    counter = 0
    temp_r = row
    temp_c = col
    while (temp_r >= 0 and temp_c >= 0):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r -= 1
            temp_c -= 1
        else:
            break

    temp_r = row
    temp_c = col
    while (temp_r <= 5 and temp_c <= 6):
        if (board[temp_r][temp_c] == tile):
            counter += 1
            temp_r += 1
            temp_c += 1
        else:
            break

    if counter >= 3:
        score += 5

    return score

def simulate_board(board,col,player):
    '''This function will return a board with the move played'''
    row = row_check(board, col)
    board[row][col] = player
    return board, (row, col)

def evaluate(board,move,player):
    '''This function will score a move base on "connections".
        It takes in 3 variables: board[a numpy matrix], move(a list)->[row, col], and player[turn #]  '''

    points = two_check(board, move, player)+ three_check(board, move, player) + disjointed_set(board, move, player) # add score
    if player == 1: # maximizing player (call evaluate from min_play())
        return -(points)
    elif player == 2: # min player (calling evaluate from max_play())
        return points

def minimax(board, depth, P):
    '''The minimax algorithm consists of 3 functions: minimax(), minplay, and maxplay()'''
    possible_moves = get_avaiable_moves(board) # possible moves are columns
    best_move = 0
    best_score = -100000
    player = P

    # goes through all possibles moves and get the min values
    for moves in possible_moves:
        sim_board = board.copy()
        leaf,move = simulate_board(sim_board, moves, player) #this function should return the state of the simulated board
        score = min_play(leaf,move,player, depth)

        if score > best_score:
            best_move =moves
            best_score = score

    return best_move

def min_play(leaf, move, player, depth):
    '''Part of minimax(). Min_play() simulates the opposition's move '''
    if win_check(leaf, move, player):   #if winning move, return the score of the
        return 1000 # calculate and return the score of the move
    elif (depth == 0):
        return evaluate(leaf, move, player)
    player =1
    depth = depth - 1
    possible_moves = get_avaiable_moves(leaf)
    best_score = 900
    best_move = 0

    for moves in possible_moves:
        sim_leaf = leaf.copy()
        leaf2, move = simulate_board(sim_leaf, moves, player)

        score = max_play(leaf2,move,player,depth)
        if score < best_score:
            best_move = moves
            best_score =score

    return best_score

def max_play(leaf, move, player, depth):
    '''Part of minimax(). Max_play() simulates the own move'''
    if win_check(leaf, move, player):   #if winning move, return the score of the
        return -1000 # calculate and return the score of the move
    elif (depth == 0):
        return evaluate(leaf, move, player)

    player = 2
    depth = depth -1
    possible_moves = get_avaiable_moves(leaf)
    best_score = -900
    best_move = 0
    for moves in possible_moves:
        sim_leaf = leaf.copy()
        leaf2,move = simulate_board(sim_leaf, moves, player)
        score = min_play(leaf2, move, player, depth)
        if score >best_score:
            best_score = score
            best_move = moves
    return best_score


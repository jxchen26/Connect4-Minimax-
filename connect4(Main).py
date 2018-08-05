import numpy as np
import pygame as pg
import math
import sys
from Minimax import *

board = np.zeros((6,7))
Game_mode = input("please select a game mode ( 1 = Player vs.Player, 2 = Player v Computers ): ")
print (type(Game_mode))
player = 1

Royal_Blue = (65,105,225)
Black = (0,0,0)
Red = (229,66,66)
Yellow = (249,249,66)

def drop_piece(board, row ,col,turn):
    if turn == 1:
        board [row][col] = 1
    if turn == 2:
        board [row][col] = 2

# check for empty row slot
def row_check(board, col):
    for row in range(5, -1, -1): # check from bottom up
        if int(board[row][col]) == 0:
            return row
    if int(board[0][col]) != 0:
        return -1

#check weather a move has won the game
def win_check(board, row, col, tile):
    #vertical
    counter = 0

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

def draw_board(board):
    for c in range(7):
        for r in range(6):
            pg.draw.rect(screen,Royal_Blue,(c*100, r*100+100, 100, 100),0)
            if board[r][c] == 0:
                pg.draw.circle(screen, Black, (int(c*100+100/2),int(r*100+100+100/2)),42)
            elif board[r][c] == 1:
                pg.draw.circle(screen, Red, (int(c*100+100/2),int(r*100+100+100/2)),42)
            elif board[r][c]==2:
                pg.draw.circle(screen, Yellow, (int(c*100+100/2),int(r*100+100+100/2)),42)

pg.init()
size = (700, 700)
screen = pg.display.set_mode(size)
draw_board(board)
pg.display.update()

#game modes
while Game_mode == "1":
    draw_board(board)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:  # for the 'X' window button
            sys.exit()
    # player1
    # will only execute if this remains true through out the code
        if player == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                colume = int(math.floor(posx / 100))
                row = row_check(board,colume)
                if row < 0:
                    player = 1
                    print('Colume ' + str(colume)+' has been filled, please select another colume')
                else:
                    drop_piece(board, row, colume, player)
                    draw_board(board)

                    print(board)
                    print('')
                    if win_check(board, row, colume, player):

                        print ("Player 1 has Won!")
                        Game_mode = 'Game_Over'
                    player = 2

    # player 2 turn
        elif player == 2:
            if event.type == pg.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                colume = int(math.floor(posx / 100))
                row = row_check(board, colume)
                if row < 0:
                    player = 2
                    print('Colume ' + str(colume)+' has been filled, please select another colume')

                else:
                    drop_piece(board, row, colume, player) # drop piece edits the board
                    draw_board(board)

                    print(board)
                    print('')
                    if(win_check(board, row, colume, player)):

                        print("Player 2 has Won!")
                        Game_mode = 'Game_Over'
                    player = 1

    pg.display.update()

while Game_mode == '2':
    draw_board(board)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            # player1 will only execute if this remains true through out the code
        elif player == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                colume = int(math.floor(posx / 100))
                row = row_check(board, colume)
                if row < 0:
                    player = 1
                    print('Colume ' + str(colume) + ' has been filled, please select another colume')
                else:
                    drop_piece(board, row, colume, player)
                    draw_board(board)
                    print('Imhere')
                    print(board)
                    print('')
                    if win_check(board, row, colume, player):
                        print("Player 1 has Won!")
                        Game_mode = 'Game_Over'
                    player = 2

                    # player 2 turn
        elif player == 2:
            print('player2s turn')
            colume = minimax(board,4,2)
            row = row_check(board, colume)
            drop_piece(board, row, colume, player)
            draw_board(board)
            print(board)
            print('')
            if (win_check(board, row, colume, player)):
                print("Player 2 has Won!")
                Game_mode = 'Game_Over'
            player = 1

    pg.display.update()

while Game_mode == 'Game_Over':
    draw_board(board)
    exit()

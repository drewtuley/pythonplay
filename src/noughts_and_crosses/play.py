#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="andrew.tuley"
__date__ ="$24-Jul-2015 16:06:48$"

from Players import Player1, Player2, Player3, Player4, Player5, Player6
import random

def show_line(board, idx):
    print ('{0}|{1}|{2}'.format(board[0+idx],board[1+idx],board[2+idx]))
    
def show_board(board):
    show_line(board,0)    
    show_line(board,3)
    show_line(board,6)
    print ('')

def is_draw(board):
    idx=0
    draw=True
    while idx < 9 and draw == True:
        if board[idx] == ' ':
            draw = False
        idx += 1
    return draw

def add_to_score(player, score_add):
    if player in scores.keys():
        score = scores[player]
        scores[player] = score+score_add
    else:
        scores[player] = score_add
    
if __name__ == "__main__":
    players=[Player1('player1'), Player2('player2'), Player3('player3'), Player4('player4'), Player5('player5'), Player6('player6')]

    game=0
    scores={}
    while game < 500:
        player1 = random.choice(players).__class__('p1')
        player2 = random.choice(players).__class__('p2')

        player1.set_piece('X')
        player2.set_piece('O')

        print ('Pitting {0} against {1}'.format(player1, player2))

        winner = None
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player=player1
        while winner == None:
            board = player.play(board)
            if player.has_won(board, player.piece):
                winner = player

            if is_draw(board):
                winner = 'draw'

            show_board(board)
            if winner == None:
                if player == player1:
                    player = player2
                else:
                    player = player1

        if winner == 'draw':
            print('draw')
            add_to_score(player1.description, 0.5)
            add_to_score(player2.description, 0.5)
        else:
            print ('Winner is {0}'.format(winner))
            add_to_score(winner.description, 1)

            
        game += 1
    for jouist in scores:
        print ('Player {0} scored {1}'.format(jouist, scores[jouist]))
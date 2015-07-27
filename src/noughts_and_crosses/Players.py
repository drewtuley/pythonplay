# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="andrew.tuley"
__date__ ="$24-Jul-2015 16:09:40$"

import random
import copy

winning_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
corners = [0,2,6,8]
centre_edges = [1,3,6,7]

def gen_idx():
    idx=0
    while idx<9:
        yield idx
        idx += 1
        
        
class Player(object):
    def __init__(self, name):
        self.name = name
        self.description = '(boring)'
        
    def __str__(self):
        return self.name+' '+self.description+' plays:'+self.piece
    
    def set_piece(self, piece):
        self.piece = piece;

    def play(self, board):
        position = self.choose_position(board)
        if position >=0 and position <9:
            board[position] = self.piece
        
        return board
        
    def choose_position(self, board):
        # simply choose the next free space
        idx=0
        while idx < 9 and board[idx] != ' ':
            idx += 1
            
        return idx
        
    def has_won(self, board, piece):
        won = False
        idx=0
        while idx < len(winning_combos) and won == False:
            combo=winning_combos[idx]
            if board[combo[0]] == piece and board[combo[1]] == piece and board[combo[2]] == piece:
                won = True
            idx += 1
            
        return won
    
    
    
    
class Player1(Player):
    pass

class Player2(Player):
    def __init__(self, name):
        self.name = name
        self.description = '(random)'
        
    def choose_position(self, board):
        return self.choose_random_position(board)
    
    def choose_random_position(self, board):
        pos = random.choice([0,1,2,3,4,5,6,7,8])
        attempt=0
        while attempt<3:
            if board[pos] == ' ':
                return pos
            attempt += 1
        # had 3 goes to find a random slot
        idx=0
        while idx <9:
            if board[idx] == ' ':
                return idx
            idx += 1
            
class Player3(Player2):
    def __init__(self, name):
        self.name = name
        self.description = '(random plus)'
        
    def can_win_in_one(self, board, piece):
        """ Can I win in one move """
        win_idx = -1
        for idx in gen_idx():
            if win_idx == -1 and board[idx] == ' ':
                brd=copy.deepcopy(board)
                brd[idx] = piece
                if self.has_won(brd, piece):
                    win_idx = idx
            
        return win_idx
    
    def choose_position(self, board):
        win = self.can_win_in_one(board, self.piece)
        if win > -1:
            return win
        else:
            return self.choose_random_position(board)
       
class Player4(Player3):
    def __init__(self, name):
        self.name = name
        self.description = '(random double plus)'
        
    def can_other_win(self, board):
        if self.piece == 'X':
            otherpiece = 'O'
        else:
            otherpiece = 'X'
            
        return self.can_win_in_one(board, otherpiece)
    
    def choose_position(self, board):
        win = self.can_win_in_one(board, self.piece)
        if win > -1:
            return win
        otherwin = self.can_other_win(board)
        if otherwin > -1:
            return otherwin
        else:
            return self.choose_random_position(board)

class Player5(Player4):
    def __init__(self, name):
        self.name = name
        self.description = '(centre starter, then corners)'
    
    def choose_position(self, board):
        if board[4] == ' ':
            return 4
        
        win = self.can_win_in_one(board, self.piece)
        if win > -1:
            return win
        
        otherwin = self.can_other_win(board)
        if otherwin > -1:
            return otherwin
        
        for corner in corners:
            if board[corner] == ' ':
                return corner
        
        return self.choose_random_position(board)
    
class Player6(Player4):
    def __init__(self, name):
        self.name = name
        self.description = '(centre starter, then edges)'
    
    def choose_position(self, board):
        if board[4] == ' ':
            return 4
        
        win = self.can_win_in_one(board, self.piece)
        if win > -1:
            return win
        
        otherwin = self.can_other_win(board)
        if otherwin > -1:
            return otherwin
        
        for edge in centre_edges:
            if board[edge] == ' ':
                return edge
        
        return self.choose_random_position(board)
    
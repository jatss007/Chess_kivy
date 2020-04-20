# -*- coding: utf-8 -*-
import copy

class check_mate:
    
    def __init__(self, turn,old_position,position_dic, new_pos_chess, new_piece_that_moved):
        '''
        Gets the Position of the King
        '''
        
        self.turn=turn
        if self.turn == "W":
            king_ID = "White King"
            self.check_for_pawns = "Up"
        else:
            king_ID = "Black King"
	
            self.check_for_pawns = "Down"
            
        
        print("Welcome to Check_mate")
        
        self.new_dic=copy.deepcopy(position_dic)
        
        self.new_dic[old_position]="None"
        self.new_dic[new_pos_chess]=new_piece_that_moved
        
        print("old vs new")
        print(turn,position_dic,self.new_dic)
        
    
    def in_check_mate():
        
        
        f = open("Data_Conversion/saved_valid_input.txt", "r")
        data=(str)(f.read().split("/")[2])
        print(type(data))
        
        
        
        k2=k1.end_game(self.turn,old_position, position_dic, new_pos_chess, piece_that_moved,square_occupied)
        if(k2.in_check(false)==True):
            print("valid_moveyes")
        
        check_c=True
        
    
        
        
        
    
        
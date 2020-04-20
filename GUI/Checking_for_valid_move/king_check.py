from Data_Conversion.position_of_pieces import position_dic

from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
from Data_Conversion.difference_for_letter import dictionar_of_numbers_to_letters
import copy


from Data_Conversion.attacked_square import attack_dic
import Checking_for_valid_move.check_mate1 as checkmate

'''
Check to see if the king is currently in check
	if yes, at the end of every move check again
		if still in check, return FALSE and repeat loop

		if not in check, end loop and return TRUE


How to check if in check:

ROOK:

Check to the left/right
Check up/down

BISHOP:

Check up/down/left/right

KNIGHT:

    CHECK THE FOUR SPOTS IT COULD BE

QUEEN:
CHECK FoR A BISHOP AND A rook



the King is the origin POint
    CHECK each squre for each peice:
        if another piece 'pops up' before the direction, end the
            process because that means it is blocked


'''

class end_game():

    def __init__(self, turn,chess_position_numerical, position_piece, pos_chess, piece_that_moved,square_occupied):
        '''
        Gets the Position of the King
        '''
        #Checks to see what player's turn it is, and decides the king's ID based on that Data
        #print(turn)
        self.turn=turn
        if self.turn == "W":
            king_ID = "White King"
            #What way the pawns are deadly to the king
            self.check_for_pawns = "Up"
        else:
            king_ID = "Black King"
	
            #What way the pawns are deadly to the king
            self.check_for_pawns = "Down"

        #Iterates through the board to determine where the king is
        
        #print(self.king_position)
        self.new_chess_position_numerical=chess_position_numerical
        self.new_position_piece=copy.deepcopy(position_piece)
        self.new_pos_chess=pos_chess
        self.new_piece_that_moved=piece_that_moved
        
        
        
        if square_occupied == "True":
                
            self.new_position_piece[str(self.new_chess_position_numerical)] = 'None'
            self.new_position_piece[str(self.new_pos_chess)] = str(self.new_piece_that_moved)

        elif square_occupied == "True, Captured":
            
            self.new_position_piece[str(self.new_chess_position_numerical)] = 'None'
            self.new_position_piece[str(self.new_pos_chess)] = str(self.new_piece_that_moved)
        
        print("chess Position",self.new_chess_position_numerical,self.new_pos_chess,self.new_piece_that_moved)
         
        #print(king_ID,self.new_position_piece)
        print("New dict",self.new_position_piece)
        for key, value in self.new_position_piece.items():
            if str(value) == king_ID:
                #Assigns this variable to the square where the king is present
                self.king_position = str(key)
                print("king position",self.king_position)
    
        
        
        
        #print("Old DIc",position_piece)
        
        #print("chess Position",self.new_chess_position_numerical,self.new_position_piece,self.new_pos_chess,self.new_piece_that_moved)
                    
        self.number_positive = int(self.king_position[1]) + 1
        self.number_negative = int(self.king_position[1]) - 1
        self.player_turn = turn
        self.numeric_value=int(dictionar_of_letters_to_numbers[self.king_position[0]])
        self.numeric_value_positive = str(self.numeric_value + 1)
        self.numeric_value_negative = str(self.numeric_value - 1)
        
        
        #if(self.new_chess_position_numerical=="f2" and self.new_pos_chess=="f3"):
        #    print(self.number_positive,self.number_negative,self.player_turn,self.numeric_value_positive,self.numeric_value_negative)
        self.number = self.king_position[1]
        self.letter = self.king_position[0]
    
    
    
    def checkCord(num):
        if(num>=1 and num<=8):
            return True
        return False;
    
    def updatePiece(self):
        
        attack_dic_copy=copy.deepcopy(attack_dic)
        for key in self.new_position_piece:
            
            current=key
            piece=self.new_position_piece[key]

            
            first=int(dictionar_of_letters_to_numbers[current[0]])
            second=int(current[1])
            
            
            c=end_game
            if("Pawn" in piece):
                if("White" in piece):
                    
                    if(c.checkCord(second+1)):
                        fir=str(second+1)
                        #pos_attacked=[]
                        if(c.checkCord(first+1)):
                            sec=str(dictionar_of_numbers_to_letters[(first+1)])+fir
                            attack_dic_copy[sec].append(piece)
                        if(c.checkCord(first-1)):
                            sec=str(dictionar_of_numbers_to_letters[(first-1)])+fir
                            attack_dic_copy[sec].append(piece)
                            
                else:
                    if(c.checkCord(second-1)):
                        fir=str(second-1)
                        #pos_attacked=[]
                        if(c.checkCord(first+1)):
                            sec=str(dictionar_of_numbers_to_letters[first+1])+fir
                            attack_dic_copy[sec].append(piece)
                        if(c.checkCord(first-1)):
                            sec=str(dictionar_of_numbers_to_letters[first-1])+fir
                            attack_dic_copy[sec].append(piece)
          
                
            if("Rook" in piece):
                f=first;
                s=second+1;
                isWhite="White" in piece
                while(s<=8):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None"):
                        attack_dic_copy[sec].append(piece)
                    elif(isPositionWhite != isWhite):
                        
                        attack_dic_copy[sec].append(piece)
                        break;
                    else:
                        break
                    s+=1
                f=first
                s=second-1
                while(s>=1):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None" ):
                        attack_dic_copy[sec].append(piece)
                    elif isPositionWhite != isWhite:

                        attack_dic_copy[sec].append(piece)
                        break;
                    else:
                        break
                    s-=1
                    
                f=first+1
                s=second
                while(f<=8):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None"):
                        attack_dic_copy[sec].append(piece)
                    elif isPositionWhite != isWhite:

                        attack_dic_copy[sec].append(piece)
                        break
                    else:
                        break
                    f+=1
                    
                f=first-1
                s=second
                while(f>=1):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None"):
                        attack_dic_copy[sec].append(piece)
                    elif(isPositionWhite != isWhite):

                        attack_dic_copy[sec].append(piece)
                        break;
                    else:
                        break
                    f-=1
                
                            
            if("Bishop" in piece):
                f=first+1;
                s=second+1;
                isWhite="White" in piece
                while(s<=8 and f<=8):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None"):
                        attack_dic_copy[sec].append(piece)
                    elif(isPositionWhite != isWhite):
                        
                        attack_dic_copy[sec].append(piece)
                        break;
                    else:
                        break
                    s+=1
                    f+=1
                f=first-1
                s=second-1
                while(s>=1 and f>=1):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None" ):
                        attack_dic_copy[sec].append(piece)
                    elif isPositionWhite != isWhite:

                        attack_dic_copy[sec].append(piece)
                        break;
                    else:
                        break
                    s-=1
                    f-=1
                f=first+1
                s=second-1
                while(f<=8 and s>=1):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None"):
                        attack_dic_copy[sec].append(piece)
                    elif isPositionWhite != isWhite:

                        attack_dic_copy[sec].append(piece)
                        break
                    else:
                        break
                    f+=1
                    s-=1
                    
                f=first-1
                s=second+1
                while(f>=1 and s<=8):
                    sec=str(dictionar_of_numbers_to_letters[f])+""+(str)(s)
                    isPositionWhite="White" in self.new_position_piece[sec]
                    if(self.new_position_piece[sec]=="None"):
                        attack_dic_copy[sec].append(piece)
                    elif(isPositionWhite != isWhite):

                        attack_dic_copy[sec].append(piece)
                        break;
                    else:
                        break
                    f-=1
                    s+=1
                
                
            if("Knight" in piece):
                
                isWhite="White" in piece
                x1=[1,1,-1,-1,-2,-2,2,2]
                y1=[-2,2,2,-2,1,-1,1,-1]
                x=first
                y=second
                for i in range(8):
                    x2=x+x1[i]
                    y2=y+y1[i]
                    if c.checkCord(x2) and c.checkCord(y2):
                        sec=str(dictionar_of_numbers_to_letters[x2])+""+(str)(y2)
                        isPositionWhite="White" in self.new_position_piece[sec]
                        if(self.new_position_piece[sec]=="None" or isPositionWhite != isWhite):
                            attack_dic_copy[sec].append(piece)
                           
            
            if("Queen" in piece):
                
            
        

    def knight(self):
        
        x1=[1,1,-1,-1,-2,-2,2,2]
        y1=[-2,2,2,-2,1,-1,1,-1]
        x=int(self.numeric_value)
        y=int(self.king_position[1])
        for i in range(8):
            x2=x+x1[i]
            y2=y+y1[i]
            if x2<1 or x2>8 or y2<1 or y2>8 :
                continue
            for key, value in dictionar_of_letters_to_numbers.items():
                if int(value) == x2:
                    letter = str(key)
            
            check_at=str(letter) + str(y2)
            val=self.new_position_piece[check_at]
            if self.player_turn == 'W':
                if  val== "Left Black Knight" or val == "Right Black Knight":
                    return "False"
            else:
                if val == "Left White Knight" or val == "Right White Knight":
                    return "False"
        
    
    def bishop(self):
        
        #print(x,y,self.player_turn)
        x1=[1,1,-1,-1]
        y1=[-1,1,1,-1]
        
        
        for i in range(4):
            x=int(self.numeric_value)
            y=int(self.king_position[1])
        
            while (int(x)+int(x1[i]))>0 and (int(x)+int(x1[i]))<9 and (int(y)+int(y1[i]))>0 and (int(y)+int(y1[i]))<9:                
                
                
                x2=int(x)+int(x1[i])
                y2=int(y)+int(y1[i])
                   
                for key, value in dictionar_of_letters_to_numbers.items():
                    if int(value) == x2:
                        letter = str(key)
                check_at=str(letter) + str(y2)
                #print("check at",check_at)
                val=str(self.new_position_piece[check_at])
                if(val!="None"):
                    #print("val,check, ",val,check_at)
                    if self.player_turn == 'W':
                        if  val== "Left Black Bishop" or val == "Right Black Bishop" or val=="Black Queen":
                            return "False"
                        else:
                            break
                    else:
                        if val == "Left White Bishop" or val == "Right White Bishop" or val=="White Queen":
                            return "False"
                        else:
                            break
                x=x+x1[i]
                y=y+y1[i]
    
    
        
    
    def rook(self):
        
        '''
        Check if to the left/right wall
        check if to the top/bottom wall
        '''
        
        
        
        if self.numeric_value_negative != '0':
            
            numberic = int(self.numeric_value_negative)
            
            endpoint = 'a' + str(self.number)
            
            
            for key, value in dictionar_of_letters_to_numbers.items():
                if int(value) == numberic:
                    letter = str(key)
            
            while self.new_position_piece[str(letter) + str(self.number) ] == 'None' and numberic>1:
            
                numberic -= 1
                
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == numberic:
                        letter = str(key)
            
            if self.player_turn == 'W':
                check_at=str(letter) + str(self.number)
                val=self.new_position_piece[check_at] 
                if val == "Left Black Rook" or val == "Right Black Rook" or val=="Black Queen":
                    return "False" 
            else:
                check_at=str(letter) + str(self.number)
                val=self.new_position_piece[check_at]
                if val == "Left White Rook" or val == "Right White Rook" or val=="White Queen":
                    return "False"
           


        if self.numeric_value_positive != '9':
            
            endpoint = 'h' + str(self.number)
            #print(endpoint)
            
            numberic = int(self.numeric_value_positive)
            
            for key, value in dictionar_of_letters_to_numbers.items():
                if int(value) == numberic:
                    letter = str(key)
                    
            while self.new_position_piece[str(letter) + str(self.number) ] == 'None' and numberic<8:
                numberic += 1
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == numberic:
                        letter = str(key)
                        
            if self.player_turn == 'W':
                check_at=str(letter) + str(self.number)
                val=self.new_position_piece[check_at]
                if val == "Left Black Rook" or val == "Right Black Rook"or val=="Black Queen":
                    return "False"
            else:
                check_at=str(letter) + str(self.number)
                val=self.new_position_piece[check_at]
                if val == "Left White Rook" or val == "Right White Rook" or val=="White Queen":
                    return "False"
            
            '''
            CHECK to thE RIGHt
            '''
            
        if self.number_positive != 9:
           
            endpoint = self.letter + '8'
            #print(endpoint)
            
            numberic = int(self.number_positive)
            
            while numberic<8 and self.new_position_piece[str(self.letter) + str(numberic) ] == 'None':
                numberic+=1
                        
            if self.player_turn == 'W':
                check_at=str(self.letter) + str(numberic)
                val=self.new_position_piece[check_at]
                if val == "Left Black Rook" or val == "Right Black Rook" or val=="Black Queen":
                    return "False"
            else:
                check_at=str(self.letter) + str(numberic)
                val=self.new_position_piece[check_at]
                if val == "Left White Rook" or val == "Right White Rook" or val=="White Queen":
                    return "False"
            
            
            '''
            CHeck going DOWN
            '''
            
        if self.number_negative != 0:
            
            endpoint = self.letter + '1'
            
            
            numberic = int(self.number_negative)
            
            
            while self.new_position_piece[str(self.letter) + str(numberic) ] == 'None' and numberic>2: #or str(self.letter) + str(numberic) == endpoint:
                    numberic-=1
            
            if self.player_turn == 'W':
                check_at=str(self.letter) + str(numberic)
                val=self.new_position_piece[check_at]
                
                if val == "Left Black Rook" or val == "Right Black Rook" or val=="Black Queen":
                    return "False"
            else:
                check_at=str(self.letter) + str(numberic)
                val=self.new_position_piece[check_at]
                if val == "Left White Rook" or val == "Right White Rook" or val=="White Queen":
                    return "False"
            
            '''
            Check going up
            '''
            


    

    def pawn(self):

        if self.check_for_pawns == "Up":
            '''
            If White
            '''
            if self.numeric_value_negative != '0':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_negative:
                        letter = str(key)
                square = str(letter) + str(self.number_positive)

            if self.numeric_value_positive != '9':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_positive:
                        letter = str(key)
                square = str(letter) + str(self.number_positive)

            if str(self.new_position_piece[square][0]) == "B" and str(self.new_position_piece[square][6]) == 'P':
                #A Pawn is in that location
                return "False"


        if self.check_for_pawns == "Down":
            '''
            If black
            '''
            
            #print(self.new_position_piece)
            if self.numeric_value_negative != '0':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_negative:
                        letter = str(key)
                square = str(letter) + str(self.number_negative)
                
                #print(square)
            if self.numeric_value_positive != '9':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_positive:
                        letter = str(key)
                square = str(letter) + str(self.number_negative)
                #print(square)
            
            if str(self.new_position_piece[square][0]) == "W" and str(self.new_position_piece[square][6]) == 'P':
                #A Pawn is in that location
                #print("false")
                return "False"
            



    def in_check(self,val=True):
        check = end_game
        
        #If it is getting check from the below peices
        
        
        pawn=check.pawn(self)
        
        rook=check.rook(self)
                
        bishop=check.bishop(self)
        
        knight=check.knight(self)
        
        check.updatePiece(self)
        
        
        if pawn == "False" or rook =="False" or bishop=="False" or knight=="False":
            
            #if val:
            #    check=checkmate.check_mate(self.turn,self.new_chess_position_numerical,position_dic,self.new_pos_chess,self.new_piece_that_moved)
                #if(check.in_check_mate()==True):
                    #print("checkmate")
            
            return True
            

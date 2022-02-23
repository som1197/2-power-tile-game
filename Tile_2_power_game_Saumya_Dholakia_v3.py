# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:56:18 2022

@author: Saumya Dholakia
"""

import numpy as np
import pandas as pd
from pynput import keyboard
import sys
        
class game_functions(object):
    
    def __init__(self):
        self.game_matrix = np.zeros((4,4))
        self.game_status = False
        self.move_status = False
        self.quit_key = False
        self.score = 0
        
    def set_initial_game_matrix(self):
        rand_matrix = np.random.randint(4, size = 4)
        self.game_matrix[rand_matrix[0]][rand_matrix[1]] = 2
        self.game_matrix[rand_matrix[2]][rand_matrix[3]] = 2
        self.print_game_matrix('Initial Game map:')
           
    def set_user_input(self):
        self.user_input = int(input('Enter the target for winning the game : '))
        
    def print_game_matrix(self,matrix_name):
        df = pd.DataFrame(self.game_matrix,columns=['','','',''],index=['','','',''],dtype=int)
        print(matrix_name,df)

    def set_updated_game_matrix(self):
        if np.any(self.game_matrix == self.user_input):
            print("YOU WON THE GAME")
            self.game_status = True
        elif self.quit_key == True:
            sys.exit('Qutting the game....')
            self.game_status = True 
        else:
            zero_rows = np.where(self.game_matrix == 0)[0]
            zero_cols = np.where(self.game_matrix == 0)[1]
            index_loc = np.random.randint(len(zero_rows), size = 1)[0]
            new_value = np.random.choice([2,4], p=[0.9,0.1])
            if self.move_status == True and len(zero_rows) != 0:
                self.game_matrix[zero_rows[index_loc]][zero_cols[index_loc]] = new_value
                self.game_status = False
                self.print_game_matrix('New Game map:')
            elif self.move_status == True and len(zero_rows) == 0:
                self.game_status = True
                print('YOU LOST THE GAME')
            
    def set_flipped_game_matrix_left_key(self):
        board_left = self.game_matrix.copy()
        for row_index,row_vectors in enumerate(board_left):
            zero_index = np.where(row_vectors == 0)[0]
            non_zero_index = np.where(row_vectors != 0)[0]
            board_left[row_index][:] = np.append(board_left[row_index][non_zero_index],\
                                                 board_left[row_index][zero_index])
        self.game_matrix = board_left.copy()
            
    def set_merged_game_matrix_left_key(self):
        board_left = self.game_matrix.copy()
        temp_score = 0
        for row_index in range(board_left.shape[0]):
            for col_index in range(len(board_left[row_index][:])-1):
                if board_left[row_index][col_index] == board_left[row_index][col_index+1]:
                    dbl_sum = (board_left[row_index][col_index]*2)
                    if dbl_sum > 0:
                        temp_score = dbl_sum
                    board_left[row_index][col_index] = dbl_sum
                    board_left[row_index][col_index+1] = 0
        self.score += temp_score
        self.game_matrix = board_left.copy()
        
    def set_flipped_game_matrix_right_key(self):
        board_right = self.game_matrix.copy()
        for row_index,row_vectors in enumerate(board_right):
            zero_index = np.where(row_vectors == 0)[0]
            non_zero_index = np.where(row_vectors != 0)[0]
            board_right[row_index][:] = np.append(board_right[row_index][zero_index],\
                                                  board_right[row_index][non_zero_index])       
        self.game_matrix = board_right.copy()
            
    def set_merged_game_matrix_right_key(self):
        board_right = self.game_matrix.copy()
        temp_score = 0
        for row_index in range(board_right.shape[0]):
            for col_index in range(len(board_right[row_index][:])-1):
                if board_right[row_index][col_index] == board_right[row_index][col_index+1]:
                    dbl_sum = board_right[row_index][col_index]*2
                    if dbl_sum > 0:
                        temp_score = dbl_sum
                    board_right[row_index][col_index+1] = dbl_sum
                    board_right[row_index][col_index] = 0
        self.score += temp_score
        self.game_matrix = board_right.copy()
    
    def set_flipped_game_matrix_top_key_1(self):
        game_matrix_transposed = self.game_matrix.transpose().copy()
        board_top = self.game_matrix.transpose().copy()
        for row_index,row_vectors in enumerate(game_matrix_transposed):
            zero_index = np.where(row_vectors == 0)[0]
            non_zero_index = np.where(row_vectors != 0)[0]
            board_top[row_index][:] = np.append(game_matrix_transposed[row_index][non_zero_index],\
                                                 game_matrix_transposed[row_index][zero_index])
        self.game_matrix = board_top.copy()
        
    def set_flipped_game_matrix_top_key_2(self):
        board_top = self.game_matrix.copy()
        for row_index,row_vectors in enumerate(board_top):
            zero_index = np.where(row_vectors == 0)[0]
            non_zero_index = np.where(row_vectors != 0)[0]
            board_top[row_index][:] = np.append(board_top[row_index][non_zero_index],\
                                                 board_top[row_index][zero_index])
        self.game_matrix = board_top.copy()
    
    def set_merged_game_matrix_top_key(self):
        board_top = self.game_matrix.copy()
        temp_score = 0
        for row_index in range(board_top.shape[0]):
            for col_index in range(len(board_top[row_index][:])-1):
                if board_top[row_index][col_index] == board_top[row_index][col_index+1]:
                    dbl_sum = board_top[row_index][col_index]*2
                    if dbl_sum > 0:
                        temp_score = dbl_sum
                    board_top[row_index][col_index] = dbl_sum
                    board_top[row_index][col_index+1] = 0
        self.score += temp_score
        self.game_matrix = board_top.copy()
        
    def set_flipped_game_matrix_bottom_key_1(self):
        game_matrix_transposed = self.game_matrix.transpose().copy()
        board_bottom = self.game_matrix.transpose().copy()
        for row_index,row_vectors in enumerate(game_matrix_transposed):
            zero_index = np.where(row_vectors == 0)[0]
            non_zero_index = np.where(row_vectors != 0)[0]
            board_bottom[row_index][:] = np.append(game_matrix_transposed[row_index][zero_index],\
                                                 game_matrix_transposed[row_index][non_zero_index])
        self.game_matrix = board_bottom.copy()
        
    def set_flipped_game_matrix_bottom_key_2(self):
        board_bottom = self.game_matrix.copy()
        for row_index,row_vectors in enumerate(board_bottom):
            zero_index = np.where(row_vectors == 0)[0]
            non_zero_index = np.where(row_vectors != 0)[0]
            board_bottom[row_index][:] = np.append(board_bottom[row_index][zero_index],\
                                                 board_bottom[row_index][non_zero_index])
        self.game_matrix = board_bottom.copy()
    
    def set_merged_game_matrix_bottom_key(self):
        board_bottom = self.game_matrix.copy()
        temp_score = 0
        for row_index in range(board_bottom.shape[0]):
            for col_index in range(len(board_bottom[row_index][:])-1):
                if board_bottom[row_index][col_index] == board_bottom[row_index][col_index+1]:
                    dbl_sum = board_bottom[row_index][col_index]*2
                    if dbl_sum > 0:
                        temp_score = dbl_sum
                    board_bottom[row_index][col_index+1] = dbl_sum
                    board_bottom[row_index][col_index] = 0
        self.score += temp_score
        self.game_matrix = board_bottom.copy()

    def move_left(self):
        self.set_flipped_game_matrix_left_key()
        self.set_merged_game_matrix_left_key()
        self.set_flipped_game_matrix_left_key()
        self.move_status = True
        self.print_game_matrix('After Left side operation:')
        print('Your current score is:%d' %self.score)
    
    def move_right(self):
        self.set_flipped_game_matrix_right_key()
        self.set_merged_game_matrix_right_key()
        self.set_flipped_game_matrix_right_key()
        self.move_status = True
        self.print_game_matrix('After Right side operation:')
        print('Your current score is:%d' %self.score)
    
    def move_up(self):
        self.set_flipped_game_matrix_top_key_1()
        self.set_merged_game_matrix_top_key()
        self.set_flipped_game_matrix_top_key_2()
        self.move_status = True
        self.game_matrix = self.game_matrix.transpose().copy()
        self.print_game_matrix('After Up side operation:')
        print('Your current score is:%d' %self.score)
    
    def move_down(self):
        self.set_flipped_game_matrix_bottom_key_1()
        self.set_merged_game_matrix_bottom_key()
        self.set_flipped_game_matrix_bottom_key_2()
        self.move_status = True
        self.game_matrix = self.game_matrix.transpose().copy()
        self.print_game_matrix('After Down side operation:')
        print('Your current score is:%d' %self.score)
            
    def on_press(self,key):
        if key == keyboard.Key.up:
            print('Upper arrow key pressed')
            self.move_up()
        elif key == keyboard.Key.down:
            print('Down arrow key pressed')
            self.move_down()
        elif key == keyboard.Key.left:
            print('Left arrow key pressed')
            self.move_left()
        elif key == keyboard.Key.right:
            print('Right arrow key is pressed')
            self.move_right()
        elif key == keyboard.Key.esc:
            print('Quitting the game, Esc key pressed')
        else:
            print("Invalid key pressed, enter one of the arrow keys")
        
    def on_release(self,key):
        if key == keyboard.Key.up:
            return False
        elif key == keyboard.Key.down:
            return False
        elif key == keyboard.Key.left:
            return False
        elif key == keyboard.Key.right:
            return False
        elif key == keyboard.Key.esc:
            self.quit_key = True
            return False
        else:
            return False
            
    def game_events(self):
        with keyboard.Listener(self.on_press,self.on_release) as listener:
            listener.join()
            
    def run_game(self):
        self.set_initial_game_matrix()
        self.set_user_input()
        print('Now enter the arrow keys')
        while self.game_status == False:
            self.game_events()
            self.set_updated_game_matrix()
                    
if __name__ == '__main__':
    game_tiles = game_functions()
    game_tiles.run_game()
  
                    


    
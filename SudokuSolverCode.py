
class Sudo:
        def __init__(self,board):
                self.board=board
                self.row=0
                self.col=0
        #a function to move next 
        #usage:--- self.row,self.col=instance.move_next(self.row,self.col)
        #same for move_back
        def move_next(self,r,c):

                if c<8:
                        return r,c+1
                elif c==8:
                        return r+1,0        
                                                                                                                                                                          #a function to move back 
        def move_back(self,r,c):
                if c>0:
                         return r,c-1
                elif c==0:
                         return r-1,8
        #a function to extract grid values
        #usage:-- gridvalues=instance.grid_values(self.row,self.col)
        def grid_values(self,r,c):
                         start_row=(r//3)*3
                         start_col=(c//3)*3
                         gridvalues=[int(self.board[x][z])  if isinstance(self.board[x][z],str) else self.board[x][z] for x in range(start_row,start_row+3) for z in range(start_col,start_col+3)]
                         return gridvalues
        #a function to extarct rowvalues
        #usage :-- rowvalues=instance.row_values(self.row,self.col)
        def row_values(self,r,c):
                         values=[int(self.board[x][c]) if isinstance(self.board[x][c],str) else self.board[x][c] for x in range(0,9)]
                         return values
        #a function to extarct dolumn values
        #usage :--columnvalues=instance.col_Values(self.row,self.col)
        def col_values(self,r,c):
                         values=[int(self.board[r][x]) if isinstance(self.board[r][x],str) else self.board[r][x] for x in range(0,9)]
                         return values
        
        #a function to print the board nicely
        def Prints(self):
                        vatotal_val = [int(x) if isinstance(x, str) else x for row in self.board for x in row] 
                        for i in range(8, 81, 9):  # Start from index 8, jump 9 steps each time
                                        print(vatotal_val[i - 8 : i + 1])  # Print each row of 9 elements
                          
        
        #function to solve the game
        #this function has tries dictionary false management 
        
        def solve(self):
                self.row,self.col=0,0
                tries=dict()
                while True:
                        #checking that that current cell is fixed or not 
                        if isinstance(self.board[self.row][self.col],str):#fixed cell
                                self.row,self.col=self.move_next(self.row,self.col)
                                if self.row==9:
                                        return self.board
                                
                        #non fixed cell             
                        else:
                                total_val=[x for x in range(1,10)]
                                used_val=[]
                                self.board[self.row][self.col]=0
                                used_val.extend(self.grid_values(self.row,self.col))
                                used_val.extend(self.row_values(self.row,self.col))
                                used_val.extend(self.col_values(self.row,self.col))
                                used_val=[x for x in used_val if x!=0]
                                possible_val=[x for x in total_val if x not in used_val]#a list of possible values for current cell (checked)
                                if possible_val:#if possible_val have values 
                                        if(str(self.row))+(str(self.col))  not in tries.keys():#not have previously tried values 
                                                self.board[self.row][self.col]=possible_val[0]#put first value for it                           
                                                if self.row==8 and self.col==8:
                                                        return self.board 
                                                self.row,self.col=self.move_next(self.row,self.col)#move next
                                        elif (str(self.row)+str(self.col)) in tries.keys():
                                                if (tries[(str(self.row))+(str(self.col))])>=(len(possible_val)):# if len of possible_val is less than or equal to tried values number
                                                        self.board[self.row][self.col] = 0#current cell=0
                                                        while True:#move back to non fixed cell 
                                                                self.row, self.col = self.move_back(self.row, self.col)
                                                                if self.row < 0:  # No solution case
                                                                        print("No solution exists")
                                                                        return
                                        
                                                                if not isinstance(self.board[self.row][self.col], str):
                                                                        self.row,self.col=self.row,self.col
                                                                        break  # Found a non-fixed cell to change
                                                        if (str((self.row))+(str(self.col))) not in tries.keys():#update tries for current cell backtracking 
                                                                tries.update({(str(self.row)+str(self.col)):0})
                                                        else:##update tries for current cell backtracking
                                                                tries.update({(str(self.row)+str(self.col)):(tries[(str(self.row)+str(self.col))])+1})
                                                        # Clear tries for all cells forward from this one
                                                                for key in list(tries.keys()):                                                                        
                                                                        if int(key) > int(str(self.row) + str(self.col)):
                                                                                del tries[key]
                                                                
                                                else:
                                                        #print(possible_val)
                                                        #print(tries[(str(self.row))+(str(self.col))]+1)
                                                        self.board[self.row][self.col]=possible_val[(tries[(str(self.row))+(str(self.col))])]
                                                        if self.row==8 and self.col==8:
                                                                return self.board
                                                        self.row,self.col=self.move_next(self.row,self.col)
                                                        
                                                        
                                                                
                                        
                                else:
                                        self.board[self.row][self.col] = 0
                                
                                        while True:
                                                self.row, self.col = self.move_back(self.row, self.col)
                                                if self.row < 0:  # No solution case
                                                        print("No solution exists")
                                                        return
                                                
                                                if not isinstance(self.board[self.row][self.col], str):
                                                        self.row,self.col=self.row,self.col
                                                        break  # Found a non-fixed cell to change
                                        if (str((self.row))+(str(self.col))) not in tries.keys():
                                                tries.update({(str(self.row)+str(self.col)):1})
                                        else:
                                                tries.update({(str(self.row)+str(self.col)):(tries[(str(self.row)+str(self.col))])+1})                   
                                        # Clear tries for all cells forward from this one
                                        for key in list(tries.keys()):
                                                if int(key) > int(str(self.row) + str(self.col)):
                                                        del tries[key]
                                                            
                 

sud= [
    [ 0 ,  0 , "3",  0 , "2",  0 , "6",  0 ,  0 ],
    ["9",  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , "1"],
    [ 0 ,  0 , "1", "8",  0 , "6", "4",  0 ,  0 ],
    [ 0 ,  0 , "8", "1",  0 , "2", "9",  0 ,  0 ],
    ["7",  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , "8"],
    [ 0 ,  0 , "6", "7",  0 , "8", "2",  0 ,  0 ],
    [ 0 ,  0 , "2", "6",  0 , "9", "5",  0 ,  0 ],
    ["8",  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , "9"],
    [ 0 ,  0 , "5",  0 , "1",  0 , "3",  0 ,  0 ]
]
'''
sud = [
    ['5', '3', 0, 0, '7', 0, 0, 0, 0],
    ['6', 0, 0, '1', '9', '5', 0, 0, 0],
    [0, '9', '8', 0, 0, 0, 0,  '6', 0],
    ['8', 0, 0, 0, '6', 0, 0, 0, '3'],
    ['4', 0, 0, '8', 0, '3', 0, 0, '1'],
    ['7', 0, 0, 0, '2', 0, 0, 0, '6'],
    [0, '6', 0, 0, 0, 0, '2', '8', 0],
    [0, 0, 0, '4', '1', '9', 0, 0, '5'],
    [0, 0, 0, 0, '8', 0, 0, '7', '9']
    ]   '''
if __name__=="__main__":
        sdoku=Sudo(sud) 
        import time 
        st=time.time()
        sdoku.solve()
        st1=time.time()
        print(st1-st)
        sdoku.Prints()
        print(sdoku.col_values(7,0))   
from tkinter import *
from tkinter import messagebox
import random

class Board:
    # A dictionary to store the Background color for every cell
    bg_color = {
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }

    # A dictionary to store the Foreground color for every cell
    color = {
        '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.n=4
        self.window=Tk()
        #self.window.titlle('Phucs 2048 Game')
        self.gameArea=Frame(self.window, bg='azure3')

        self.board=[]

        # Build 4x4 board
        self.gridCell=[[0]*4 for i in range(4)]

        self.compress=False

        self.merge=False

        self.moved=False

        self.score=0

        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(self.gameArea, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
                l.grid(row=i, column=j, padx=7, pady=7)

                rows.append(l)

            self.board.append(rows)
        self.gameArea.grid()

    # Function to reverse the grid
    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while (i<j):
                self.gridCell[ind][i], self.gridCell[ind][j]=self.gridCell[ind][j], self.gridCell[ind][i]
                i+=1
                j-=1

    # Function to transform rows to columns and vice versa.
    # zip is used to combine elements from 2 or more iterables together, element-wise, into tuples.
    # '*' is the unpacking operator, which takes a list and unpacks its elements as if they were individual arguments to a function
    def transpose(self):
        self.gridCell=[list(t) for t in zip(*self.gridCell)]

    # Function to check if the grid has been compressed and then compress it
    def compressGrid(self):
        self.compress=False
        # Create a clone grid
        temp=[[0]*4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                # If encountering a non-zero element, move this element to the leftmost position in the new grid
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]

                    # If the element is moved from its original position
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        # Set the compressed grid cell to gridCell
        self.gridCell=temp

    # Function to merge grid
    def mergeGrid(self):
        self.merge=False
        for i in range(4):
            for j in range(3):
                # If found 2 equal elements and they are non-zeroes
                if self.gridCell[i][j]==self.gridCell[i][j+1] and self.gridCell[i][j]!=0:
                    self.gridCell[i][j]*=2
                    self.gridCell[i][j+1]=0
                    self.score+=self.gridCell[i][j]
                    self.merge=True

    # Function to pick a random cell
    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                # Get list of empty cells
                if self.gridCell[i][j]==0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]=2

    # Function to check if can merge horizontally or vertically (left to right and top to bottom)
    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j]==self.gridCell[i][j+1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j]==self.gridCell[i][j]:
                    return True

        return False

    def transpose(self):
        self.gridCell=[list(t) for t in zip(*self.gridCell)]

    # Function to paint the grid
    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='', bg='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                        bg=self.bg_color.get(str(self.gridCell[i][j])),
                        fg=self.color.get(str(self.gridCell[i][j])))

class Game:
    def __init__(self, gamePannel):
        self.gamePannel = gamePannel
        self.end = False
        self.won = False

    def start(self):
        self.gamePannel.random_cell()
        self.gamePannel.random_cell()
        self.gamePannel.paintGrid()
        self.gamePannel.window.bind('<Key', self.link_keys)
        self.gamePannel.window.mainloop()

    def link_keys(self, event):
        if self.end or self.won:
            return

        self.gamePannel.compress = False
        self.gamePannel.merge = False
        self.gamePannel.moved = False

        presed_key = event.keysym

        if presed_key == 'Up':
            self.gamePannel.tranpose()
            self.gamePannel.compressGrid()
            self.gamePannel.mergeGrid()
            self.gamePannel.moved=self.gamePannel.compress or self.gamePannel
            self.gamePannel.compressGrid()
            self.gamePannel.tranpose()

        elif presed_key == 'Down':
            self.gamepanel.transpose()

            # Reverse the grid
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

            # Reverse the grid back
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif presed_key=='Left':
            self.gamePannel.compressGrid()
            self.gamePannel.mergeGrid()
            self.gamePannel.moved=self.gamePannel.compress or self.gamePannel.merge
            self.gamePannel.compressGrid()

        elif presed_key == 'Right':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()

        else:
            pass

        self.gamePannel.paintGrid()
        print(self.gamePannel.score)

        flag=0
        # Check if the player reached 2048
        for i in range(4):
            for j in range(4):
                if (self.gamePannel.gridCell[i][j]==2048):
                    flag=1
                    break

        if (flag==1):
            self.won=True
            messagebox.showinfo('2048', message='You won!!!!')
            print('Won')
            return

        for i in range(4):
            for j in range(4):
                if (self.gamePannel.gridCell[i][j]==0):
                    flag=1
                    break

        if not(flag or self.gamePannel.can_merge()):
            self.end=True
            messagebox.showinfo('2048', 'Game over!!!')
            print("Game over!!")

        if self.gamePannel.moved:
            self.gamePannel.random_cell()

        self.gamePannel.paintGrid()

gamePannel=Board()
game2048=Game(gamePannel)
game2048.start()

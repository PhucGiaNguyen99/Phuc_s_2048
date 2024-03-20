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






    def transpose(self):
        self.gridCell=[list(t) for t in zip(*self.gridCell)]


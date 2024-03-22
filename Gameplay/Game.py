import Board
class Game:
    def __init__(self, gamePannel):
        self.gamePannel=gamePannel
        self.end=False
        self.won=False

    def start(self):
        self.gamePannel.random_cell()
        self.gamePannel.random_cell()
        self.gamePannel.paintGrid()
        self.gamePannel.window.bind('<Key', self.link_keys)
        self.gamePannel.window.mainloop()

    def link_keys(self, event):
        if self.end or self.won:
            return

        self.gamePannel.compress=False
        self.gamePannel.merge=False
        self.gamePannel.moved=False

        presed_key=event.keysym

        if presed_key=='Up':
            self.gamePannel.tranpose()
            self.gamePannel.compressGrid()

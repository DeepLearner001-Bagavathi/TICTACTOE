import os

class TICTACTOE:
    
    def __init__(self):
        self.usr_input=[["1","2","3"],["4","5","6"],["7","8","9"]]
    
    def Startingscreen(self):
        #The following commad only work in linux if you install figlet
        os.system("figlet 'TIC TAC TOE' ")
        print()
        print("START GAME TYPE NUMBER INSIDE IN GRID")
        print()
        print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")
    
    def game_loop(self):
        for index in range(1,10):
            curr_player = "X" if index%2==1 else "O"
            self.get_usr_input(curr_player)
            self.display_current_state()
            if index >=6:
                win =  self.winner()
                if win:
                    print(f"PLAYER {win} WON THE GAME")
                    return
        print("TIE")

    def get_usr_input(self,player):
        while True:
            curr = input(f"Enter a {player} player position : ")
            if curr.isnumeric() and int(curr) >=1 and int(curr) <= 9 :
                curr = int(curr)
                col = curr%3 - 1 if curr%3 else 2
                if self.usr_input[(curr-1)//3][col] not in "XO":   
                    self.usr_input[(curr-1)//3][col] = player
                    break
                else:
                    print("ENTER A VALID POSITION IT IS ALREADY OCCUPIED")
            else:
                print("INVALID INPUT")
            
    def display_current_state(self):
        for i in range(3):
            for j in range(3):
                print(f" {self.usr_input[i][j]} ",end="")
                if j < 2:
                    print("|",end = "")
            print()
            if i < 2:
                print("-"*11)
                
    def is_winner(self,curr):
        return "".join(curr) in ("XXX","OOO")

    def winner(self):
        #Check row wise
        for i in range(3):
            if self.is_winner(self.usr_input[i]):
                return self.usr_input[i][0]
            
        #Check col wise
        for i in range(3):
            curr = []
            for j in range(3):
                curr.append(self.usr_input[j][i])
            if self.is_winner(curr):
                return curr[0]
        
        #Check Diagnol wise
        lead_dig,sec_dig = [],[]
        i = 2
        for j in range(3):
            lead_dig.append(self.usr_input[i][i])
            sec_dig.append(self.usr_input[j][i])
            i -= 1
        if self.is_winner(lead_dig):
            return lead_dig[0]
        if self.is_winner(sec_dig):
            return sec_dig[0]
        return False

START = True
while START:
    obj = TICTACTOE()
    obj.Startingscreen()
    obj.game_loop()
    game = input("TO CONINUE GAME PRESS 1 OR QUIT PRESS ANY :")
    if game != "1":
        print("BYE")
        START = False
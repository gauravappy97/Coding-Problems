board = {}
n =  int(input("How many queens?"))
def initialize(board,n):
    for key in ['queen','row','col','nwtose','swtone']:
        board[key] = {}
        for i in range(n):
            board['queen'][i] = -1
            board['row'][i] = 0
            board['col'][i] = 0
        for i in range(-(n-1),n):
            board['nwtose'][i] = 0
        for i in range(2*n-1):
            board['swtone'][i] = 0
initialize(board,n)
def placequeen(i,board):
    n = len(board[queen].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i,j,board)
            if i==n-1:
                return(Ture)
            else:
                extendsoln = placement[i+1,board]
            if extendsoln:
                return(True)
            else:
                undoqueen(i,j,board)
        else:
            return(False)
if placequeen(0,board):
    def printboard(board):
        for row in sorted(board['queen'].keys()):
            print((row,board['queen'][row]))
            print(" ")
    printboard(board)
    

def free(i,j,board):
    return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-1]==0 and board['swtone'][j+1]==0)

def addqueen(i,j,board):
    board['queen'][i]==j
    board['row'][i]==1
    board['col'][j]==1
    board['nwtose'][j-1]==1
    board['swtone'][j+1]==1

def undoqueen(i,board):
    board['queen'][i]==-1
    board['row'][i]==0
    board['col'][j]==0
    board['nwtose'][j-1]==0
    board['swtone'][j+1]==0

           
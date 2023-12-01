import math
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


def fac(n):
    n=int(input())
    f=1
    s=0
    for i in range (1, n+1):
        f = f * i
        s = f + s
    print(s)

# deistvie=input()
# match deistvie:
#     case 'pow':
#         ch=int(input())
#         s=int(input())
#         print(pow(ch,s))
#     case 'fibanachi':
#         N=int(input())
#         print(fib(N))
#     case 'factorial':
#         d=int(input())
#         print(fac(d))
#     case 'sin':
#         zn_ch=int(input())
#         s = {30: 0.5, 45:'√2/2', 60:'√3/2', 90: 1, 270: -1, 360 or 0 or 180: 0}
#         print(s[zn_ch])
#     case 'cos':
#         zn_ch = int(input())
#         c = {60: 0.5, 45:'√2/2', 30:'√3/2', 0 or 360: 1, 180: -1, 270 or 90: 0}
#         print(c[zn_ch])
#     case 'tg':
#         zn_ch = int(input())
#         t = {60: '√3', 45: 1, 30: '√3/3', 0 or 360 or 180: 0, }
#         print(t[zn_ch])
#     case 'ctg':
#         zn_ch = int(input())
#         ct = {60: 0.5, 45: '√2/2', 30: '√3/2', 0 or 360: 1, 180: -1, 270 or 90: 0}
#         print(ct[zn_ch])
#     case '+':
#         a=int(input())
#         b=int(input())
#         print(a+b)
#     case '-':
#         a = int(input())
#         b = int(input())
#         print(a-b)
#     case '*':
#         a = int(input())
#         b = int(input())
#         print(a*b)
#     case '/':
#         a = int(input())
#         b = int(input())
#         print(a/b)

def ris_board(board):
    print('-------------')
    for i in board:
        print('|',"|".join(i), '|')
        print('-------------')
def win(board, person):
    for i in range (3):
        if all (board[i][j] == person for j in range(3)) or all(board[j][i] == person for j in range(3)):
            return True
        if all (board[i][i] == person for i in range(3)) or all(board[i][2-i] == person for i in range(3)):
            return True
    return False
def full(board):
    return all(all(cell!=' ' for cell in row) for row in board)
def tictactoe(board):
    board=[[' ' for _ in range(3)] for _ in range(3)]
    persons=['X','O']
    currentperson=0
    print('********** Игра Крестики-нолики для двух игроков **********')
    ris_board(board)
    while True:
        move=int(input(f'Куда поставим {persons[currentperson]}?'))-1
        row, col =divmod(move,3)
        if board[row][col] == ' ':
            board[row][col]=persons[currentperson]
            ris_board(board)
            if win(board, persons[currentperson]):
                print(f'{persons[currentperson]} выйграл!')
                break
            elif full(board):
                print('Nichya!')
                break
            currentperson = 1- currentperson
        else:
            print('Эта ячейка занята!')
if __name__ == '__main__':
    tictactoe()
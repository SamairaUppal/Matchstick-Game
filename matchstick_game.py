print('Enter the number of matches: ')
n = int(input())
print('Enter the maximum number of matches a player can pick:')
m = int(input())
currentPlayer = 1
while True:
    print('Number of remaining matches:', n)
    for i in range(n):
        print('*', end = ' ')
    print()
    for i in range(n):
        print('|',end = ' ')
    print()
    print('Player '+str(currentPlayer)+f': How many matches do you want to pick? (1,2, ..., {m})')
    num = int(input())
    if 1<=num<=m and n-num>=0 and isinstance(num, int) == True:
        n -=num
    else:
        print('Invalid move!')
        continue
    
    if n == 0:
        print('Player '+str(currentPlayer)+ ' won the game!')
        break
        
    else:
        currentPlayer = 3- currentPlayer
        continue
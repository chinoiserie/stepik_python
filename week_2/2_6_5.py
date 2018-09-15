# Выведите таблицу размером n×n, заполненную числами от 1 до n ** 2 по спирали, выходящей из левого верхнего угла и закрученной 
# по часовой стрелке. 

n = int(input())
m = [[0] * n for i in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, c = 0, -1, 1
for i in range(n + n - 1):
    for j in range((n + n - i) // 2):
        x += dx[i % 4]
        y += dy[i % 4]
        m[x][y] = c
        c += 1
for i in range(n):
    print(*m[i])

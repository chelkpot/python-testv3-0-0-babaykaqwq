# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    z=int(input())
    s=z//100+(z//10)%10+z%10
    print(s)

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
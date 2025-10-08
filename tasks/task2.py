# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    o=int(input())
    o=o%1440
    chasi=o//60
    minuti=o%60
    print(chasi,minuti)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
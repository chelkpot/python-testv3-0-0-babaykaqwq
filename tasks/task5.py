# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    x=int(input())
    hours=x//3600%24
    minutes=(x//60)%60
    seconds=x%60
    print(hours,":",minutes//10,minutes%10,":", seconds//10,seconds%10,sep="")

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
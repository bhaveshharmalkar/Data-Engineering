if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
my_list = list(arr)
my_list.sort()

n = []

for a in my_list:
    if a in n:
        pass
    else:
        n.append(a)
        
print(n[-2])

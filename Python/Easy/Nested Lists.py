dc = {}

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dc[name] = score

# find the second lowest score
scores = sorted(set(dc.values()))
second_lowest = scores[1]

# collect names with that score
result = [name for name, score in dc.items() if score == second_lowest]

# sort names alphabetically
result.sort()

# print them
for name in result:
    print(name)

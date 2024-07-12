user = input("Enter a sentence: ")
lis = input("Enter keyword: ")
first = 0 
last = 0
n = len(user)
nl = len(lis)
for i in range(n-1):
    if user[i:i+nl] == lis:
        first += i
        last += i+nl-1
        break

print(f"The word {lis} is from {user} is in index {first} until {last}")
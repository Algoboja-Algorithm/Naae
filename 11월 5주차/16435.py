

n ,length = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in arr :
	if i <= length:
		length +=1
	else:
		break
print(length)


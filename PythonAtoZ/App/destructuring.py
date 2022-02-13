peopel = {1:11,2:22,3:32}
head,*tails = [1,2,3,4,5]
*heads,tail = [1,2,3,4,5]

for people,val in peopel.items():
    print(val)

print(head,tails)
# 1 [2, 3, 4, 5]
print(heads,tail)
# [1, 2, 3, 4] 5


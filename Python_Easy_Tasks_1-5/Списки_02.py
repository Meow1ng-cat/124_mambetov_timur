import random

List_1 = []
List_2 = []
Result = []

for i in range(random.randint(50, 100)):
    List_1.append(random.randint(0, 9999))
for i in range(random.randint(50, 100)):
    List_2.append(random.randint(0, 9999))

for num in List_1:
    if num in List_2:
        Result.append(num)

print(len(List_1), len(List_2), len(Result))
print(List_1)
print(List_2)
print(Result)
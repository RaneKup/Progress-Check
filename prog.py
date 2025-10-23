#уровень B
#Зайцев Егор ии-72

import random

nums = []

for i in range(6):
    nums.append(random.randint(1,24))

count = 0
for i in nums:
    if i % 3 == 0:
        count += 1
print(count)

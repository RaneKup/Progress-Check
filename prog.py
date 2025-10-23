#уровень B
#Зайцев Егор ии-72

import random

nums = []

random1 = random.randint(1, 24)
random2 = random.randint(1, 24)
random3 = random.randint(1, 24)
random4 = random.randint(1, 24)
random5 = random.randint(1, 24)
random6 = random.randint(1, 24)

nums.append(random1)
nums.append(random2)
nums.append(random3)
nums.append(random4)
nums.append(random5)
nums.append(random6)

count = 0
for i in nums:
    if i % 3 == 0:
        count += 1
print(count)
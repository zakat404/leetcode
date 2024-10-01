def two_sum(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]

num = [1,2,3,4,5,6,7,8]
target = 9
print(two_sum(num, target))

a = 2
b = 2
print(a + b)
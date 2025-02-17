"""
{
    4:6,
    5:8,....
}
"""

lst = [4, 5, 1, 3, 4, 5, 5, 5, 3, 5, 6, 4, 6, 5, 5, 5, 4, 1, 3, 4, 4]
n = len(lst)

# freq={}
freq = dict()


# for i in range(0, n):
#     if lst[i] in freq:
#         freq[lst[i]] += 1
#     else:
#         freq[lst[i]] = 1

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)

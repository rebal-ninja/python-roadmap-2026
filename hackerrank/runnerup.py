scores = [2,3,3,5,4,4,6]

# highest = float("-inf")
# second = float("-inf")

# for i in scores:
#     if i > highest:
#         second = highest
#         highest = i
        
#     else:
#         if i < highest and i > second:
#          second = i

# print(second)


# or

# set = list(set(scores))
# set.sort()
# runner_up = set[-2]
# print(runner_up)


scores = [2,3,6,6,5]

remove_duplicates = list(set(scores))
sort = remove_duplicates.sort()
runner_up = sort[-2]
print(runner_up)
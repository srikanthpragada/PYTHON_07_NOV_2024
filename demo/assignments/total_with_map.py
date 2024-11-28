data = ["10", "20", "15", "abc", "5"]

# total = 0
# for n in map(int, data):
#     total += n
#
# print(total)

# print(sum(map(int, data)))

valid_data = filter(str.isdigit, data)
print(sum(map(int, valid_data)))

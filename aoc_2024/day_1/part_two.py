def read_lines(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split("   ") for line in file.readlines()]


list_right = []
list_left = []

for line in read_lines("./day_1/input.txt"):
    list_right.append(int(line[0]))
    list_left.append(int(line[1]))
list_right.sort()
list_left.sort()


sum = 0
for i in range(len(list_left)):
    count = 0
    for j in range(len(list_right)):
        if list_left[i] == list_right[j]:
            count += 1
            sum += (list_left[i] * count)
    

print(sum)

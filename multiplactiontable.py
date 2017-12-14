table = []
for num1 in range(1,2**10):
	table.append([])
	for num2 in range(1,2**10):
		table[num1-1].append(num1 * num2)


print(table)



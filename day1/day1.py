# read in data
with open("day1Input.txt", "r") as fyle:
	data = fyle.read()
# split on empty newlines
staging = data.split("\n\n")
processed = []
for item in staging:
	try:
		processed.append(sum([int(x) for x in item.split("\n")]))
	except ValueError:
		continue

print(f"Most calories is {max(processed)}")

# get top three elf calorie counts, sum
processed.sort(reverse=True)
print(f"Top three calorie-carriers together: {sum(processed[:3])}")
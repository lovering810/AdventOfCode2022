def get_letter_val(letter:str):
	start_value = ord(letter.lower()) - 96
	if letter.lower() == letter:
		return start_value
	else:
		return start_value + 26
	

def get_shared_items(row) -> int:
	# split in half
	halfway = int(len(row) / 2)
	a, b = row[:halfway], row[halfway:]
	# get intersection of items
	overlap = set(a).intersection(set(b))

	return overlap

def score_row(row) -> int:

	overlap = get_shared_items(row=row)

	return sum(map(get_letter_val,list(overlap)))

def inventory():

	with open("day3_data.txt", "r") as fyle:
		data = fyle.readlines()
	
	total = []
	for row in data:
		total.append(score_row(row=row))
	
	print(f"Priority sum over all items: {sum(total)}")

	elf_groups = [data[i:i+3] for i in range(0, len(data), 3)]
	total_badges = []
	for group in elf_groups:
		a, b, c = group
		shared = set(a.strip()).intersection(set(b.strip())).intersection(set(c.strip()))
		if len(shared) > 1:
			print(f"too many badges: {shared}")
			continue
		total_badges.append(get_letter_val(list(shared)[0]))
	
	print(f"Badge totals: {sum(total_badges)}")

if __name__ == "__main__":
	inventory()
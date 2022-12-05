import re

def _unpack_range(range_string: str):
	a, b = range_string.split("-")
	range_set = list(range(int(a),int(b)+1))
	return range_set

def make_comparable(row: str):
	# explode ranges
	a, b = [_unpack_range(x) for x in row.strip().split(",")]
	return a, b

def detect_proper_subset(a, b) -> bool:
	# compare ranges
	if set(a) <= set(b):
		# print(f"first set of row {row} is a proper subset of the second set.")
		result = True
	elif set(b) <= set(a):
		# print(f"Second set of row {row} is fully contained in the first set.")
		result = True
	else:
		# print(f"Sets in row {row} are fully or partially discrete.")
		result = False
	return result

def detect_overlap(a, b) -> bool:
	overlap = set(a).intersection(set(b))
	return overlap != set()

def compare_row_ranges(row: str, func: callable) -> bool:
	row=row.strip()
	a, b = make_comparable(row=row)
	return func(a, b)

def part1(data):
	return sum([compare_row_ranges(row, detect_proper_subset) for row in data])

def part2(data):
	return sum([compare_row_ranges(row, detect_overlap) for row in data])

def main():

	with open("day4data.txt", "r") as fyle:
		data = fyle.readlines()

	print(f"Total pairs with proper subset: {part1(data)}")
	print(f"Total pairs with any overlap: {part2(data)}")

if __name__ == "__main__":
	main()
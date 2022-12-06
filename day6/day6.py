# detect key
def detect_key(candidate_key: str) -> bool:
	return len(candidate_key) == len(set(candidate_key))
# set of four characters different from one another, moving window of four characters
def parse_buffer(buffer: str, key_length: int = 4) -> int:
	for i in range(len(buffer)):
		candidate_key = buffer[i:i+key_length]
		if detect_key(candidate_key=candidate_key):
			# identify in buffer where key ends
			return i+key_length
		else:
			continue

def part1(data: str):
	result = parse_buffer(buffer=data)
	return result

def part2(data: str):
	result = parse_buffer(buffer=data, key_length=14)
	return result

if __name__ == "__main__":
	with open("day6_data.txt", "r") as fyle:
		data = fyle.read()
	p1 = part1(data=data)
	p2 = part2(data=data)

	print(f"Buffer must be parsed to the {p1}th character for key, {p2}th character for message")
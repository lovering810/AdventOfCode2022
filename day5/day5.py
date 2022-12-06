from collections import defaultdict, deque
import re


with open("day5_data.txt","r") as fyle:
	data = fyle.readlines()

starting_config = data[:9]
instructions = data[10:]

# parse starting_config, three chars per column w spaces between
starting_config_grid = [[line.strip()[i:i+4] for i in range(0, len(line.strip()), 4)] for line in starting_config[:-1]]

# flip 'em, get rid of empties
STACKS = defaultdict(list)
for column_index in range(len(starting_config_grid[0])):
    STACKS[str(column_index+1)] += [x[column_index].strip() for x in starting_config_grid if x[column_index] != '    ']


# get the args to the function
def parse_instruction(instruction) -> tuple:
	pattern = r"move (\d*) from (\d) to (\d)"
	results=re.findall(pattern, instruction)
	return results[0]


# move crates based on instruction
def move_crates(stacks: dict, instructions: list, new_model: bool):
	for instruction in instructions:
		# get specs
		num, origin, destination = parse_instruction(instruction=instruction)
		# grab the crates
		grabbed = [stacks[origin].pop() for i in range(int(num))]
		# apply to destination
		if new_model:
			stacks[destination].extend(list(reversed(grabbed)))
		else:
			for item in grabbed:
				stacks[destination].append(item)
	return stacks


def part1():
	stacks = {key:list(reversed(stack)) for (key, stack) in STACKS.items()}
	result = move_crates(stacks=stacks, instructions=instructions, new_model=False)
	keystring = ""
	for key in result:
		keystring += result[key][-1]
	print(f'keystring: {"".join([k for k in keystring if k not in ["[", "]"]])}')


def part2():
	stacks = {key:list(reversed(stack)) for (key, stack) in STACKS.items()}
	result = move_crates(stacks=stacks, instructions=instructions, new_model=True)
	keystring = ""
	for key in result:
		keystring += result[key][-1]
	print(f'keystring: {"".join([k for k in keystring if k not in ["[", "]"]])}')


if __name__ == "__main__":
	part1()
	part2()
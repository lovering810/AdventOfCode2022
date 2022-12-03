# FIRST HALF

player1 = ["A", "B", "C"]
player2 = ["X", "Y", "Z"]
conditions = {"loss":0, "win": 6, "draw": 3}


# def one_round(p1: int, p2: int) -> str:

# 	diff = p2 - p1
# 	# if diff is none, return "draw"
# 	if diff == 0:
# 		outcome = "draw"
# 	# if diff is two, or -1, winner is p1
# 	elif diff == 2 or diff == -1:
# 		outcome = "loss"
# 	# if diff between is one, the victor is p2
# 	else:
# 		outcome = "win"
# 	return outcome

# def play(p1: str, p2: str) -> int:

# 	p1 = player1.index(p1) + 1
# 	p2 = player2.index(p2) + 1
# 	result = conditions[one_round(p1, p2)]
# 	score = p2 + result
# 	return score

# def game(data):
# 	# get score for each pair
# 	total = []
# 	for hand in data:
# 		score = play(*hand)
# 		total.append(score)

# 	print(f"Total score: {sum(total)}")


# SECOND PART (direct invocation broken, use grid)

def loss(p1: int) -> int:
	if p1 == 1:
		p2 = 3
	elif p1 == 2:
		p2 = 1
	else:
		p2 = 2
	return p2

def draw(p1: int) -> int:
	return player1.index(p1) + 1

def win(p1: int) -> int:
	if p1 == 1:
		p2 = 2
	elif p1 == 2:
		p2 = 3
	else:
		p2 = 1
	return p2

moves = {"X":loss, "Y":draw, "Z":win}

# GRID REFACTOR

#     1    |    2    |    3 
# 1 "draw" |  "p1"   |  "p2"
# 2 "p2"   |  "draw" |  "p1"
# 3 "p1"   |  "p2"   | "draw"

move_grid = [
	["draw", "win", "loss"],
	["loss", "draw", "win"],
	["win", "loss", "draw"]
	]

def playval(p1, p2)->int:
	p1 = player1.index(p1)
	p2 = player2.index(p2)
	result = move_grid[p1][p2]
	# print(f"p1: {p1}, p2: {p2}, result: {result}")
	return p2 + conditions[result] + 1

def playmove(p1: str, p2: str) -> int:
	p1 = player1.index(p1)
	row = move_grid[p1]
	result = moves[p2].__name__
	move = row.index(result)
	return move + conditions[result] + 1

def playgrid(data):
	totval = []
	totmove = []
	for hand in data:
		totval.append(playval(*hand))
		totmove.append(playmove(*hand))
	
	print(f"Total score by value interpretation: {sum(totval)}; total by move: {sum(totmove)}")


if __name__ == "__main__":
	# get pairs from input
	with open("day2_input.txt", "r") as fyle:
		data = [item.split() for item in fyle.readlines()]

	game(data)
	# simonsays(data)
	playgrid(data)
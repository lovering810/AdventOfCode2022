from day2 import day2
import pytest

def test_round():

	output = day2.one_round(1,2)
	assert output == "win"

	output = day2.one_round(2,1)
	assert output == "loss"

	output = day2.one_round(2,2)
	assert output == "draw"

	funky = day2.one_round(1,3)
	assert funky == "loss"

	funk2 = day2.one_round(3,1)
	assert funk2 == "win"

def test_win():
	assert day2.win(1) == 2
	assert day2.win(2) == 3
	assert day2.win(3) == 1

def test_loss():
	assert day2.loss(1) == 3
	assert day2.loss(2) == 1
	assert day2.loss(3) == 2

@pytest.mark.parametrize(
    "p1,expected",
    [
        (1, 3,),
        (2, 1,),
        (3, 2,),
    ],
)
def test_losses(p1, expected):
	command = "X"

	assert day2.follow(p1, command) == expected

@pytest.mark.parametrize(
    "p1,expected",
    [
        (1, 8),
        (2, 9),
        (3, 7),
    ],
)
def test_wins(p1, expected):
	command = "Z"
	assert day2.follow(p1, command) == expected

def test_grid_val():

	draw1 = day2.playval("A", "X")
	assert draw1 == 4

	win1 = day2.playval("A", "Y")
	assert win1 == 2 + 6

	lose2 = day2.playval("C", "Y")
	assert lose2 == 2 + 0



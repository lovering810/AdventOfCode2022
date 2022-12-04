from day3 import day3 as d

def test_val():
	a = d.get_letter_val(letter="a")
	assert a == 1

	A = d.get_letter_val(letter="A")
	assert A == 27
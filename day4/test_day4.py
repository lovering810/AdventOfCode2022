from day4 import day4 as d

def test_unpack_range():

	range_string = "4-6"
	result = d._unpack_range(range_string)
	assert result == [4, 5, 6]

def test_make_comparable():
	row = "26-54,26-30"
	a, b = d.make_comparable(row=row)
	assert a == [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
	assert b == [26, 27, 28, 29, 30]


def test_comprow():
	row = "26-54,26-30"
	result = d.compare_row_ranges(row=row, func=d.detect_proper_subset)
	assert result

	row = '38-86,38-86'
	result = d.compare_row_ranges(row=row, func=d.detect_proper_subset)
	assert result
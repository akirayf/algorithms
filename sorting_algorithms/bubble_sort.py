"""

Implement bubble sort algorithm to sory numbers in ascending/descending order

"""

def bubble_sort(sort_type=1, elems=[]):
	elemLen = len(elems)
	if elemLen <= 1:
		print "No need to sort elem list, then return directly."
		return elems
	
	unsortedLen = elemLen
	while unsortedLen != 1:
		for i in range(0, unsortedLen-1):
			if (sort_type == 1 and elems[i] > elems[i+1]) or (sort_type == 0 and elems[i] < elems[i+1]):
				tmp = elems[i]
				elems[i] = elems[i+1]
				elems[i+1] = tmp
		unsortedLen = unsortedLen - 1
	return elems

if __name__ == '__main__':
	bubble_sort()
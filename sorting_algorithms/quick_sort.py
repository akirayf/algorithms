"""

Implement quick sort algorithm to sory numbers in ascending/descending order

"""

def quick_sort(sort_type=1, elems=[]):
	elemLen = len(elems)
	if elemLen <= 1:
		return elems

	pivotIndex = 0
	pivot = elems[pivotIndex]

	headIndex  = 0
	tailIndex = elemLen - 1
	isRightSide = True
	while headIndex <= tailIndex:
		if isRightSide:
			if (sort_type == 1 and pivot > elems[tailIndex]) or (sort_type == 0 and pivot < elems[tailIndex]):
				elems[pivotIndex] = elems[tailIndex]
				pivotIndex = tailIndex
				isRightSide = False
			tailIndex = tailIndex - 1
		else:
			if (sort_type == 1 and pivot < elems[headIndex]) or (sort_type == 0 and pivot > elems[headIndex]):
				elems[pivotIndex] = elems[headIndex]
				pivotIndex = headIndex
				isRightSide = True
			headIndex = headIndex + 1

	if pivotIndex == elemLen - 1:
		return quick_sort(sort_type, elems[0:pivotIndex]) + [pivot]
	elif pivotIndex == 0:
		return [pivot] + quick_sort(sort_type, elems[1:])
	else:
		return quick_sort(sort_type, elems[0:pivotIndex]) + [pivot] + quick_sort(sort_type, elems[(pivotIndex + 1):])

if __name__ == '__main__':
	quick_sort()
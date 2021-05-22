import unittest

def swap(target, arr):
	if len(arr) != len(target):
	    return False

	mapper = {}
	string = ""
	length = len(set(target))
	count = -1

	for i in range(len(arr)):
	    if arr[i] not in mapper:
			mapper[arr[i]] = target[i]
			count += 1
	    if length == count:
			return False
	    string += mapper[arr[i]]
	return string == target

def findAndReplacePattern(words, pattern):
	match = []

	for testCase in words:
	    if swap(pattern, testCase) == True:
		match.append(testCase)

	return match

class TestPattern(unittest.TestCase):

	def test_pattern_one(self):
		self.assertEqual(findAndReplacePattern(["a", "b", "c"], "a"), ["a", "b", "c"])
	
	def test_pattern_two(self):
		self.assertEqual(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"), ["mee", "aqq"])
		
if __name__ == '__main__':
    unittest.main()

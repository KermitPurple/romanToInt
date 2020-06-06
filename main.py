import unittest

def romanToInt(s: str) -> int:
    dct = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    lst = split_and_convert(s, dct)
    prev = lst[0]
    total = prev
    for num in lst[1:]:
        if num > prev:
            total -= 2 * prev
        total += num
        prev = num
    return total

def split_and_convert(s: str, dct: dict) -> list:
    return [dct[char] for char in s]

class testRomanToInt(unittest.TestCase):
    def test5(self):
        self.assertEqual(romanToInt("V"), 5)
    def test20(self):
        self.assertEqual(romanToInt("XX"), 20)
    def test2012(self):
        self.assertEqual(romanToInt("MMXII"), 2012)

if __name__ == "__main__":
    unittest.main()

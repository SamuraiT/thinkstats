import Pmf
import mode
import unittest

class TestMode(unittest.TestCase):

    def test_mode(self):
        """exercise 2-3 page 19"""
        hist = Pmf.MakeHistFromList([1,2,2,3,5])
        mode_val = mode.Mode(hist)
        self.assertEqual(mode_val, [2])

    def test_mode_multimodal(self):
        hist = Pmf.MakeHistFromList([1,2,2,3,3,5])
        mode_val = sorted(mode.Mode(hist))
        self.assertEqual(mode_val, [2,3])

if __name__ == '__main__':
    unittest.main()

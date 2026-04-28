import unittest
from contrived_func import contrived_func

class Test(unittest.TestCase):
    
    def test_1(self):
        contrived_func(0)

    def test_2(self):
        contrived_func(-1) 

    def test_3(self):
        contrived_func(17)

    def test_4(self):
        contrived_func(100)

    def test_5(self):
        contrived_func(24)

    def test_6(self):
        contrived_func(42)

    def test_7(self):
        contrived_func(99)
    
    def test_8(self):
        contrived_func(1)



if __name__ == '__main__':
    unittest.main()

#-*- coding:utf-8 -*- 
import unittest
from src.conjectura_collatz import decompoe_numero, execute

class TestConjecturaCollatz(unittest.TestCase):

    def test_decompoe_numero_even(self):
        self.assertEquals(2, decompoe_numero(2))

    def test_decompoe_numero_odd(self):
        self.assertEquals(8, decompoe_numero(3))        
    
if __name__ == "__main__":
    unittest.main()
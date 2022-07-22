import unittest
from client3 import *


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],
                             quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

# ------------ Add more unit tests ------------ """

    def test_getRatio_resultEqualToInfinity(self):
        price_a = 119.2
        price_b = 0

        self.assertIsNone(getRatio(price_a, price_b), None)

    def test_getRatio_resultEqualToZero(self):
        price_a = 0
        price_b = 120.48

        self.assertEqual(getRatio(price_a, price_b), 0)

    def test_getRatio_resultGreaterThan1(self):
        price_a = 123
        price_b = 8.001

        self.assertGreater(getRatio(price_a, price_b), 1)

    def test_getRatio_resultLessThan1(self):
        price_a = 37.0
        price_b = 117.87

        self.assertLess(getRatio(price_a, price_b), 1)

    def test_getRatio_resultEqualTo1(self):
        price_a = 120.48
        price_b = 120.48

        self.assertEqual(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()

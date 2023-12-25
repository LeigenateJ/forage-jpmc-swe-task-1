import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_priceBIsZero(self):
    self.assertIsNone(getRatio(1, 0))


  def test_getRatio_normalCondition(self):
    self.assertEqual(getRatio(1, 2), 0.5)


  def test_getRatio_negativePrice(self):
    self.assertEqual(getRatio(-1, 2), -0.5)
    self.assertEqual(getRatio(1, -2), -0.5)
    self.assertEqual(getRatio(-1, -2), 0.5)


  def test_getDataPoint_missingField(self):
    quote = {'top_ask': {'size': 36}, 'timestamp': '2019-02-11', 'top_bid': {'price': 120.48, 'size': 109},
             'id': '0.109974697771', 'stock': 'ABC'}
    with self.assertRaises(KeyError):
      getDataPoint(quote)


  def test_getDataPoint_emptyQuote(self):
    quote = {}
    with self.assertRaises(KeyError):
      getDataPoint(quote)


if __name__ == '__main__':
    unittest.main()

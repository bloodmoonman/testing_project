import surfshop
import unittest
import datetime

class SurfShopTest(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
    message = self.cart.add_surfboards(quantity=1)
    self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

  def test_apply_locals(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def test_add_surfboards(self):
    for num in range(2, 5): 
      with self.subTest(num):
        message = self.cart.add_surfboards(num)
        self.assertEqual(message, f"Successfully added {num} surfboards to cart!")
        self.cart = surfshop.ShoppingCart() 
    
  def test_add_invalid_checkout_date(self):
        date = datetime.datetime.now()
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)
    

unittest.main()

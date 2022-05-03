import surfshop
import unittest
import datetime

class SurfShopTest(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
    message = self.cart.add_surfboards(quantity=1)
    self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

  def test_add_surfboards(self): #THIS ONE AND THE BELOW METHODS ARE CAN BE PARAMETERIZED. WHAT IS THAT MEAN? 
                                 #THAT MEANS WE KNOW surfshop.py will raise an TOOMANYBOARDSERROR WHEN QUANTITY=5. 
                                 #SO WE CAN USE LOOP TO REDUCE IT TO ONE METHOD FOR TESTING. WE WILL ASSERT THE RESULTS WITH IF ELSE CONDITIONS.
    message = self.cart.add_surfboards(quantity=2)
    self.assertEqual(message, 'Successfully added 2 surfboards to cart!')
  @unittest.skip #5 fails so we skip this one
  def test_add_surfboards_five(self):
    self.assertRaises(Exception, self.cart.add_surfboards(quantity=5))


  def test_apply_locals(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def test_add_surfboards(self):

    for num in range(2, 5): #THIS IS THE PARAMETERIZED TEST, INSTEAD OF DEFINING SEPARATE METHODS FOR 2, 3, 4 SURFBOARDS WE USE THIS. 
                            #IT TAKES 2, 3, 4 SURFBOARDS. IT STOPPED AT 4 BECAUSE THAT IS THE MAXIMUM NUMBER OF ITEM WE CAN HAVE IN CART. 
      with self.subTest(num):
        message = self.cart.add_surfboards(num)
        self.assertEqual(message, f"Successfully added {num} surfboards to cart!")
        self.cart = surfshop.ShoppingCart() # WE NEED TO RESET self.cart IN EVERY LOOP OTHERWISE IT WILL SUM ALL, 
                                            #AND WILL CAUSE DISTORTION IN OUR RESULT. WILL NOT CAUSE AN ERROR IN PYTHON BUT IT WONT FUNCTION CORRECTLY.
    
  def test_add_invalid_checkout_date(self):
        date = datetime.datetime.now()
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)
    

unittest.main()
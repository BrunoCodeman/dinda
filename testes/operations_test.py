import unittest
from operations import Operations


class OperationsTest(unittest.TestCase):

    def test_must_add_value_on_credit(self):
    	op = Operations("accounts.csv")
    	op.accounts = {"1":2359415, "2":335498, "3": -5579741} #mocking data
    	original_value = op.accounts["1"]
    	op.make_operation("1", 100)
    	self.assertEquals(op.accounts["1"], long(original_value + 100))
    	
    def test_must_subtract_value_on_debit(self):
    	op = Operations("accounts.csv")
    	op.accounts = {"1":2359415, "2":335498, "3": -5579741} #mocking data
    	original_value = op.accounts["2"]
    	op.make_operation("2", -200)
    	self.assertEquals(op.accounts["2"], long(original_value - 200))

    def test_must_apply_tax_on_negative_account(self):
    	op = Operations("accounts.csv")
    	op.accounts = {"1":2359415, "2":335498, "3": -5579741} #mocking data
    	original_value = op.accounts["3"]
    	op.make_operation("3", -300)
    	self.assertEquals(op.accounts["3"], long(original_value -800))

if __name__ == '__main__':
    unittest.main()

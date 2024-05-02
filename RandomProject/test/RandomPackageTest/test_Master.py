from unittest import TestCase;
from RandomPackage.Master import Master;

class TestMaster(TestCase):

    def setUp(self):
        self.masterObj = Master();

    def test_add(self):
        self.assertEqual(self.masterObj.add(20,10), 30);

    def test_subtract(self):
        self.assertEqual(self.masterObj.subtract(20, 10), 10);

    def test_product(self):
        self.assertEqual(self.masterObj.product(20, 10), 200);

    def test_divider(self):
        self.assertEqual(self.masterObj.divider(20, 10), 2.0);

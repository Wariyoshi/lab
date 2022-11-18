from pytest import *
from account import *
class Test:
    def setup_method(self):
        self.a1 = Account('Joe')

    def test_init(self):
        assert self.a1.get_name() == 'Joe'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(30) is True
        assert self.a1.get_balance() == 30
        assert self.a1.deposit(-30) is False
        assert self.a1.get_balance() == 30
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 30
        assert self.a1.deposit(0.1) is True
        assert self.a1.get_balance() == approx(30.1, abs=0.01)


    def test_withdraw(self):
        assert self.a1.deposit(30) is True
        assert self.a1.withdraw(15) is True
        assert self.a1.get_balance() == 15
        assert self.a1.withdraw(-1) == False
        assert self.a1.get_balance() == 15
        assert self.a1.withdraw(0) == False
        assert self.a1.get_balance() == 15
        assert self.a1.withdraw(0.1) == True
        assert self.a1.get_balance() == approx(14.9, abs=0.01)

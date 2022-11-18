class Account:
    def __init__(self, name: str) -> None:
        '''
        Function to establish the account name and set the account balance to zero.
        :param name: Name on the account.
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Function to add the amount to the account balance as long as it is positive.
        :param amount: Amount of money to be deposited into the account.
        :return: True if the amount is positive and False if the amount is zero of negative.
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        Function to subtract the amount from the account balance as long as it is positive and
        less than the account's current balance.
        :param amount: Amount of money to be withdrawn from the account.
        :return: True if the amount is positive/less than the account balance and False if not.
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        Function to retrieve the account balance.
        :return: Retrieves __account_balance.
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Function to retrieve the account name.
        :return: Retrieves __account_name.
        '''
        return self.__account_name

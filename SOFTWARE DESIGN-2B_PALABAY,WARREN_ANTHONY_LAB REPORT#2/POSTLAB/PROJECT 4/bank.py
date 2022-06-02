import pickle

# Implementation of SavingsAccount class
class SavingsAccount(object):
    '''This class represents a savings account
    with the owner's name, PIN, and balance.'''

    RATE = 0.02

    # Implementation of __init__
    def __init__(self, name, pin, balance=0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    # Implementation of __str__ method
    def __str__(self):
        result = 'Name: ' + self._name + '\n'
        result += 'PIN: ' + self._pin + '\n'
        result += 'Balance: ' + str(self._balance)
        return result

    # Implementation of getBalance method
    def getBalance(self):
        return self._balance

    # Implementation of getName method
    def getName(self):
        return self._name

    # Implementation of getName method
    def getPin(self):
        return self._pin

    # Implementation of deposit method
    def deposit(self, amount):
        '''Deposits the given amount.'''
        self._balance += amount
        return self._balance

    # Implementation of withdraw method
    def withdraw(self, amount):
        '''Withdraws the given amount.
        Returns None if successful, or an
        error message if unsuccessful.'''
        # check amount is less than 0 or not
        if amount < 0:
            return 'Amount must be >= 0'
        elif self._balance < amount:
            return 'Insufficient funds'
        else:
            self._balance -= amount
        return None

    # Implementation of computeInterest method
    def computeInterest(self):
        '''Computes, deposits, and returns the interest.'''
        # calculate interest
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest


# Implementation of Bank class
class Bank(object):
    '''This class represents a bank as a dictionary of
    accounts. An optional file name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent file storage.'''

    # Implementation of __init__
    def __init__(self, fileName=None):
        '''Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts.'''

        self._accounts = {}
        self.fileName = fileName
        # check fileName is not equal to None
        if fileName != None:
            # open the file in read mode
            fileObj = open(fileName, 'rb')
            # Iterate the loop
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    # close the file
                    fileObj.close()
                    break

    # Implementation of add method
    def add(self, account):
        '''Inserts an account using its PIN as a key.'''
        self._accounts[account.getPin()] = account

    # Implementation of remove method
    def remove(self, pin):
        return self._accounts.pop(pin)

    # Implementation of get method
    def get(self, pin):
        return self._accounts.get(pin, None)

    # Implementation of computeInterest method
    def computeInterest(self):
        '''Computes interest for each account and
        returns the total.'''
        total = 0
        # Iterate the loop
        for account in self._accounts.values():
            total += account.computeInterest()
        return total

    # Implementation of __str__ method
    def __str__(self):
        '''Return the string rep of the entire bank.'''
        return '\n'.join(map(str, self._accounts.values()))

    # Implementation of save method
    def save(self, fileName=None):
        '''Saves pickled accounts to a file. The parameter
        allows the user to change file names.'''
        # check fileName is not equal to None
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        # open the file in write mode
        fileObj = open(self.fileName, 'wb')

        # Iterate the loop
        for account in self._accounts.values():
            pickle.dump(account, fileObj)
        # close the file
        fileObj.close()


# Implementation of testBank method
def testBank(self, number=0):
    '''Returns a bank with the specified number of accounts and/or
    the accounts loaded from the specified file name.'''
    # create an object for Bank class
    bank = Bank()
    # Iterate the loop
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1), str(1000 + i), 100.00))
    return bank

from Car import Car
from Account import Account
from UberX import UberX


if __name__ == '__main__':

    user1 = Account("Jorge Garcia", "INE34284")
    
    my_uber = UberX('2FG234', user1, 'Ford', 'Focus')
    my_uber.print_data_car()
    
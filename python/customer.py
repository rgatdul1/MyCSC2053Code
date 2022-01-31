from person import Person

class Customer(Person):
    empty_list = {}
    def __int__(self,first_name, last_name, orders=empty_list):
        self.orders = orders
        super().__init__(first_name, last_name)

    def __str__(self):
        return super().__str__() + " " + str(len(self.orders))

    def add_order(self, order_num):
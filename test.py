import os

clear = lambda: os.system('cls')

store_items = [["C1", "Chickenjoy", 89],
               ["C2", "Chickenjoy w/ Spaghetti", 100],
               ["C3", "Chickenjoy w/ Fries", 96],
               ["B1", "Burgersteak", 90],
               ["B2", "Burgersteak w/ Lumpia", 110],
               ["B3", "Burgersteak w/ Fries", 100],
               ["Y1", "Yumburger", 20],
               ["Y2", "Yumburger w/ Fries", 50],
               ["S1", "Spaghetti", 60],
               ["S2", "Spaghetti w/ Fries", 80],
               ]
user_input = None

my_cart = []


class SalesClass:
    total_price = 0
    item_code = None
    item_quantity = 0

    def payment(self):
        amount = 0
        while self.total_price > amount:
            try:
                clear()
                print("              WELCOME TO JABEEEEEEE")
                SalesClass.show_item()
                SalesClass.check_cart()
                amount = 0
                amount = int(input("Cash Tendered: "))
                if self.total_price > amount:
                    print("Insufficient Amount")

            except:
                print("Invalid Input")
                continue
        if self.total_price < amount:
            change = amount - self.total_price
            print(f"Your Change: {change}")
        print("Thank you!")

    @classmethod
    def split_input(cls, user_inp):
        vals = user_inp.split(" ")
        print(vals)
        cls.item_code = vals[0]
        cls.item_quantity = int(vals[1])

    @staticmethod
    def show_item():
        print("\n")
        print("{: >5} {: >25} {: >10}".format("Code", "Item", "Price"))
        for item in store_items:
            print("{: >5} {: >25} {: >10}".format(*item))

    @classmethod
    def removeItem(cls):

        input_item_code = input("Enter Item Code to remove: ").upper()
        cls.split_input(input_item_code)
        for row2, data2 in enumerate(my_cart):
            if cls.item_code == my_cart[row2][0]:
                if my_cart[row2][1] > 1:
                    my_cart[row2][1] = my_cart[row2][1] - cls.item_quantity
                    my_cart[row2][3] = my_cart[row2][2] * my_cart[row2][1]
                    if my_cart[row2][1] < 1:
                        my_cart.pop([row2][0])

                else:
                    my_cart.pop([row2][0])
                break
        cls.check_cart()

    @classmethod
    def getTotalPrice(cls):
        cls.total_price = 0
        for row, customer_items in enumerate(my_cart):
            cls.total_price += my_cart[row][3]
        print("\n{: >38}".format(f"TOTAL: {cls.total_price}"))

    @classmethod
    def check_cart(cls):
        print("\n----------------------------------------")
        print("{: >5} {: >10} {: >10} {: >10}".format("Item", "Qty", "Price", "Total"))

        for customer_items in my_cart:
            print("{: >5} {: >10} {: >10} {: >10}".format(*customer_items))
        cls.getTotalPrice()
        print("\n----------------------------------------")

    @classmethod
    def order(cls):
        total = 0
        for a, b in enumerate(store_items):
            for c, d in enumerate(b):
                if cls.item_code == d:
                    is_exist = False
                    num_row = 0
                    for row, data in enumerate(my_cart):
                        if my_cart[row][0] == store_items[a][c]:
                            is_exist = True
                            num_row = row
                            break

                    total = cls.item_quantity * store_items[a][c + 2]

                    if is_exist:
                        my_cart[num_row][1] += cls.item_quantity
                        my_cart[num_row][3] += total

                    else:
                        temp_cart = [None, None, None, total]
                        temp_cart[0] = (store_items[a][c])
                        temp_cart[1] = cls.item_quantity
                        temp_cart[2] = (store_items[a][c + 2])
                        my_cart.append(temp_cart)


while user_input != "F":
    try:
        clear()
        print("              WELCOME TO JABEEEEEEE")
        SalesClass.show_item()
        SalesClass.check_cart()
        user_input = input("Enter Code: ").upper()

        if user_input == "C":
            SalesClass.check_cart()

        elif user_input == "S":
            SalesClass.show_item()

        elif user_input == "R":
            SalesClass.removeItem()

        else:
            SalesClass.split_input(user_input)
            SalesClass.order()
    except:
        pass

payment = SalesClass()
payment.payment()

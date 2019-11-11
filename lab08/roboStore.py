# Intro to Programming Lab 6
# Jack Mullane
# 10/7/2019

from products import Product


URF = Product("Ultrasonic range finder", 2.50, 4)
SM = Product("Servo motor", 14.99, 10)
SC = Product("Servo controller", 44.95, 5)
MB = Product("Microcontroller Board", 34.95, 7)
LRF = Product("Laser range finder", 149.99, 2)
LPB = Product("Lithium polymer battery", 8.99, 8)

product_list = [URF, SM, SC, MB, LRF, LPB]


def print_stock():
    print("\nAvailable Products")
    print("------------------")
    for i in range(0, len(product_list)):
        if product_list[i].quantity > 0:
            print(str(i) + ")", product_list[i].name, "$", product_list[i].price)
    print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break

        prod_id = int(vals[0])
        count = int(vals[1])

        if product_list[prod_id].stockCheck(count) == True:
            if cash >= product_list[prod_id].purchaseCost(count):
                cash -= product_list[prod_id].purchaseCost(count)
                product_list[prod_id].purchase(count)
                print("You purchased", count, product_list[prod_id].name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product_list[prod_id].name)


main()

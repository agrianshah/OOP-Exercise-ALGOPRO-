from Belanja import BelanjaTAP

class OrderItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.price_per_pound = self.get_price_per_pound()
        self.cost = self.get_cost()

    def get_price_per_pound(self):
        if self.name == "Wagyu Steaks":
            return 450.00
        elif self.name == "Matsutake Mushrooms":
            return 272.00
        elif self.name == "Le Bonnotte Potatoes":
            return 270.81
        elif self.name == "Moose Cheese":
            return 487.20

    def get_cost(self):
        return self.amount * self.price_per_pound

    def __str__(self):
        return f"Item: {self.name}\nAmount ordered: {self.amount} pounds\nPrice per pound: ${self.price_per_pound:.2f}\nPrice of order: ${self.cost:.2f}"


def create_list_of_order_items():
    order_items = []
    n = int(input("How many items will you order today? "))
    while n < 1:
        print("Number of items must be at least 1.")
        n = int(input("How many items will you order today? "))
    for i in range(n):
        name = input(f"Item #{i+1}- Enter food: ")
        amount = float(input(f"Enter amount of pounds: "))
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input(f"Enter amount of pounds: "))
        order_items.append(OrderItem(name, amount))
    return order_items


def display_list_of_order_items(order_items):
    for item in order_items:
        print(item)


def calculate_total_cost(order_items):
    total_cost = sum([item.cost for item in order_items])
    return total_cost


def main():
    order_items = create_list_of_order_items()
    print("\nHere's a summary of the items purchased:")
    display_list_of_order_items(order_items)
    total_cost = calculate_total_cost(order_items)
    print(f"\nTotal cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
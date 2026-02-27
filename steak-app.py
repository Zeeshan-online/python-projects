class Customer:
    def __init__(self, name):
        self.name = name
        self.order = []

    def add_to_order(self, item):
        self.order.append(item)

    def view_bill(self, menu):
        total = 0
        print()
        print("----- 🧾 Bill Summary -----")
        for item in self.order:
            price = menu[item][1]
            print(f"{item} 🥩 - $ {price}")
            total += price
        print("---------------------------")
        print(f"Total Amount: $ {total}")
        print("---------------------------")
        return total


class SteakRestaurant:
    def __init__(self):
        self.menu = {
            1: ("Classic Ribeye Steak", 25),
            2: ("T-Bone Steak", 32),
            3: ("BBQ Beef Steak", 22),
            4: ("Grilled Chicken Steak", 18),
            5: ("Cheese Stuffed Steak", 28)
        }

    def display_menu(self):
        print()
        print("===== 🥩 Welcome To Steak House 🥩 =====")
        print("--------- MENU ---------")
        for key, value in self.menu.items():
            print(f"{key}. {value[0]} 🥩 - $ {value[1]}")
        print("----------------------------")

    def take_order(self, customer):
        while True:
            self.display_menu()
            print("6. View Bill 🧾")
            print("7. Exit ❌")
            print()
            choice = input("Select an Option: ")

            if choice.isdigit():
                choice = int(choice)
                if choice in self.menu:
                    item_name = self.menu[choice]  # ✅ Fixed here
                    customer.add_to_order(item_name[0])  # store only name
                    print()
                    print(f"{item_name[0]} added to your order! ✅")
                    print()
                elif choice == 6:
                    customer.view_bill(self.get_menu_dict())
                    input("Press Enter to continue...")
                elif choice == 7:
                    print()
                    print("Thank you for visiting! 👋")
                    break
                else:
                    print("Invalid option ❌")
            else:
                print("Please enter a valid number!")

    def get_menu_dict(self):
        # returns dictionary like {'Classic Ribeye Steak': ('Classic Ribeye Steak', 25), ...}
        return {value[0]: value for value in self.menu.values()}


# ===== Main Program =====
print("Welcome to the Premium Steak Restaurant App 🥩")
print()

name = input("Enter Your Name: ")
customer = Customer(name)
restaurant = SteakRestaurant()

restaurant.take_order(customer)
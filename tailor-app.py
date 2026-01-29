class TailorApp:

    def __init__(self):
        self.orders = {}

    def menu(self):
        print("\n🧵 Tailor App")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Exit")

    def calculate_price(self, cloth):
        prices = {'shirt': 20, 'pants': 30, 'suit': 100}
        return prices.get(cloth.lower(), 12)

    def get_measurements(self, cloth):
        cloth = cloth.lower()

        if cloth == 'shirt':
            return {
                'chest': float(input('Chest (inches): ')),
                'length': float(input('Length (inches): '))
            }

        elif cloth == 'pants':
            return {
                'waist': float(input('Waist (inches): ')),
                'length': float(input('Length (inches): '))
            }

        else:
            return {
                'chest': float(input('Chest (inches): ')),
                'waist': float(input('Waist (inches): ')),
                'length': float(input('Length (inches): '))
            }

    def add_order(self):
        name = input('Customer Name: ').title()
        cloth = input('Cloth Type (shirt/pants/suit/other): ')

        measurements = self.get_measurements(cloth)
        price = self.calculate_price(cloth)

        self.orders[name] = {
            'cloth': cloth,
            'measurements': measurements,
            'price': price
        }

        print(f'✅ Order Added | 💰 ${price}')

    def view_orders(self):
        if not self.orders:
            print("❌ No orders found")
            return

        for name, data in self.orders.items():
            print(f"\n👕 Customer: {name}")
            print(f"Cloth: {data['cloth']}")

            for k, v in data['measurements'].items():
                print(f"{k.capitalize()}: {v} inches")

            print(f"Price: ${data['price']}")

    def run(self):
        while True:
            self.menu()
            choice = input('Choose (1-3): ')

            if choice == '1':
                self.add_order()

            elif choice == '2':
                self.view_orders()

            elif choice == '3':
                print('😊👋 Goodbye!')
                break

            else:
                print("❌ Invalid choice")


TailorApp().run()

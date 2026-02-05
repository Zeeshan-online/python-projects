class BugerApp:
    
    def __init__(self):
        
        self.orders = {}
        
    def menu(self):
        
        print("\n Buger App")
        
        print("1. Add Order")
        
        print("2. View Orders")
        
        print("3. Exite")
        
    def calculate_price(self, size ):
        
        prices = {'small': 5, 'medium': 7, 'large': 10}
        
        return prices.get(size.lower(), 6)
    
    def add_order(self):
        
        name = input('Customer Name: ').title()
        
        size = input('Buger Size\n (small: 5/mdeium: 7/large: 10 ): ')
        
        price = self.calculate_price(size)
        
        self.orders[name] = {
            'size': size,
            # 'masurements': maseurements,
            'price': price,
        }
        
        print(f"Oder Added price: ${price}")
        
    def view_orders(self):
        
        if not  self.orders:
            
            print("No orders found")
            
            return
        for name, data in self.orders.items():
            
            print(f"\n Customer: {name}")
            
            print(f"Buger Size: {data['size']}")
            
            print(f"Measurments: {data['masurements']}")
            
            print("Total Price: ${data['price]}")
            
    def run(self):
        
        while True:
            
            self.menu()
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                
                self.add_order()
                
            elif choice == '2':
                
                self.calculate_price()
                self.view_orders()
                
            elif choice == '3':
                
                print("Goodbye!")
                
                break
            else:
                
                print("Invilid choice!")
                
BugerApp().run()                
                                            
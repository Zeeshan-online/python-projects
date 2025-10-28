    # sevrice provider class
class Provider:
    def __init__(self, name, rating):
        
        self.name = name
        
        self.rating = rating
        
    # show provider onfo
    
    def show(self):
        
        print(f"Provider: {self.name} | Rating: {self.rating}")
        
    # services class
    
class Service:
    
    def __init__(self, name, price, provider):
        
        self.name = name
        
        self.price = price
        
        self.provider = provider
        
    # show service with provider
    
    def show(self):
        
        print(f"{self.name} -${self.price}")
        
        self.provider.show()
        
# App class

class HouseServiceApp:
    
    def __init__(self):
        
        self.services = [
            Service("Plumber", 50, Provider("Rammzan", 4.8)),
            
            Service("Electrician", 70, Provider("Ahsan", 4.6)),
            
            Service("Cleaner", 30, Provider("Abid", 4.9))
        ]            
        
        self.cart = []
        
    # show services
    
    def show_services(self):
        
        for i, s in enumerate(self.services):
            print(f"\n{i+i}. ", end=""); s.show()
    
    # Add services
    
    def add_to_cart(self, idx):
        
        self.cart.append(self.services[idx])
        
        print("Added to cart.")
        
    # show cart
    
    def show_cart(self):
        
        if not self.cart: print("empty cart"); return
        
        for s in self.cart: s.show()
        
    # Checkout
    
    def checkout(self):
        
        total = sum (s.price for s in self.cart)
        
        print(f"Total = ${total}")
        
# Main

app = HouseServiceApp()

while True:
    
    print("\n--- House Services Menu ----") 
    
    print("1. show Services")
    
    print("2. Add Service to cart")
    
    print("3. View cart")
    
    print("4. Checkout")
    
    print("5. Exit")
    
    c = input("Choose: ")
    
    if c == "1": app.show_services()
    
    elif c == "2":
        app.show_services()
        
        n = int(input("Select service number: ")) -1
        
        app.add_to_cart(n)
        
    elif c == "3":
        app.show_cart()
    
    elif c == "4":
        app.checkout()
        
    elif c == "5":
        break
                                              
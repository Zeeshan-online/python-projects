class WaiterApp:
    
    def __init__(self):
        
        self.menu = {"Buger": 5, "Pizza": 12, "Tea": 2}
        
        self.tables = {1: [],2: [], 3: [], }
        
    def banner(self):
        
        print()
        
        print("🍽️ WELCOME TO PYTHON RESTAURANT 🍽️")   
        
        print()
        
        
    def show_menu(self):
        
        print()
        
        print("---MENU---")
        
        for i, p in self.menu.items():
            
            print(f"{i:<8} $ {p}")
            
        print()
        
        
    def take_order(self):
        
        t = int(input("Table (1-3): "))
        
        print()
        
        item = input("item: ").title()
        
        if t in self.tables and item in self.menu:
            
            self.tables[t].append(item)
            
            print(f"✔️ {item} added to Table {t}")
            
        else:
            print("Invalid table or item")
            
        print()
        
    def show_bill(self):
        
        print()
        
        t = int(input("Table (1-3): "))
        
        orders = self.tables.get(t, [])
        
        total = sum(self.menu[i] for i in orders) 
        
        print(f"🧾 Table {t} Bill")
        
        print("Orders: ", orders if orders else "No orders")
        
        print("Total: $", total) 
        
        print()
        
        
app = WaiterApp()

app.banner()

while True:
    
    print("1️⃣ Menu, 2️⃣ order, 3️⃣ Bill, 4️⃣ Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        
        app.show_menu()
        
    elif choice == "2":
        
        app.take_order()
        
    elif choice == "3":
        
        app.show_bill()
        
    elif choice == "4":
        print("Thanks! Visit agian.")
        
        break  
    
    else: print("Invalid option")
    
    print()                               
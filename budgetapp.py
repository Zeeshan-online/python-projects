class BudgetApp:
    
    def __init__(self):
        
        self.categories = {}
        
        
        
    def add_category(self, name):
        
        if name not in self.categories:
            
            self.categories[name] = 0
            
            print(f"Category {name} added. ")
            
        else:
            
            print(f"Category {name} already exists.")
            
    
    def add_income(self, category, amount):
        
        if category in self.categories:
            
            self.categories[category] += amount
        else:
            
            self.categories[category] = amount
            
            
    def add_expense(self, category, amount):
        
        if category in self.categories:
            
            if self.categories[category] >= amount:
                
                self.categories[category] -= amount
                
                print(f"Spent ${amount} from {category}")
                
            else:
                
                print("Insufficient funds in category.") 
                
        else:
            
            print("Category not found.")
            
            
    def view_budget(self):
        
        if not self.categories:
            
            print("No categories found.")
            
        for cat, amt in self.categories.items():
            
            print(f"{cat}: ${amt}")                               
            
            
def main():
    
    app = BudgetApp()
    
    while True:
        
        print("\n--- Budget App Menu ---")
        
        print("1. Add Category")
        
        print("2. Add Income")
        
        print("3. Add Expense")
        
        print("4. View Budget")
        
        print("5. Exit")
        
        
        choice = input("Enter your choice: ")

        
        if choice == '1':
            
            name = input("Enter category name: ")
            
            app.add_category(name)
            
        elif choice == '2':
            
            cat = input("Enter category name: ")
            
            amt = float(input("Enter amount: "))
            
            app.add_income(cat, amt)
            
        elif choice == '3':
            
            cat = input("Enter category: ")
            
            amt = float(input("Enter amount: "))
            
            app.add_expense(cat, amt)
            
        elif choice == '4':
            
            app.view_budget() 
            
        elif choice == '5':
            
            print("Goodbye!")
            
            break
        
        else:
            print("Invalid choice") 
            
if __name__ == "__main__":
    
    main()                      
            
                           
                           
     
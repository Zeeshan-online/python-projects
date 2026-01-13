class User:
    
    def __init__(self, name, balance=0):
        
        self.name = name
        
        self.balance = balance
        
        
    def show_balance(self):
        
        print(f"{self.name}, your balance is ${self.balance}")
        
        
    def add_money(self, amount):
        
        self.balance += amount
        
        print(f"${amount} add. New balance: ${self.balance}")
        
     
    def send_money(self, receiver, amount):
        
        if self.balance >= amount:
            
            self.balance -= amount
            
            receiver.balance += amount
            
            print(f"Sent ${amount} to {receiver.name}")
            
        else:
            
            print("Insufficient Balance")
            
     
    
def main():
    
    user1 = User("Usman", 100) 
    
    user2 = User("Ali", 50)
    
    
    while True:
        
        print("\n---- Payment App ----")
        
        print("1. Show Balance")
        
        print("2. Add Money")
        
        print("3. Send Money")
        
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            
            user1.show_balance()
            
        elif choice == '2':
            
            amt = float(input("Enter amount to add: "))
            
            user1.add_money(amt)
            
            
        elif choice == '3':
            
            amt = float(input("Enter amount to send to Ali: "))   
            
            user1.send_money(user2, amt)
            
        elif choice == '4':
            
            print("Goodby")
            
            break
            
        else:
            
            print("Invalid choice.")
            
            
if __name__ == "__main__":
    
    main()            
                                                   
        
    
    
class BankAccount:
    
    # initializen account with pin & history
    def __init__(self, name, pin, balance=0):
        
        self.name = name
        
        self.pin = pin
        
        self.balance = balance
        
        self.history = []
        
    # deposite money
    def deposit(self, amount):
        
        self.balance += amount
        
        self.history.append(f"Deposited ${amount}")
        
        print(f"${amount} deposited! New balance: ${self.balance}")
    
    # withdraw money
    
    def withdraw(self, amount):
        
        if amount <= self.balance:
            
            if amount <= self.balance:
                self.balance -= amount
                
                self.history.append(f"Withdraw ${amount}")
                
                print(f"${amount} withdraw! New balance: ${self.balance}")  
            else:
                print("Insufficient balance!") 
                
    # show balance
    
    def show_balance(self):
        
        print(f"Account Holder: {self.name}, Balance: ${self.balance}")
        
        # show transaction hiistory
        
    def show_history(self):
        
        print("\n--- Transaction History ---")             
        
        for t in self.history:
            
            print(t) if self.history else print("No Transaction yet!")
            
# --- main program ---

name = input("Enter your name: ")

pin = input("set a 4-digit PIN: ")

account = BankAccount(name, pin)

# ask for pin before access

if input("Enter PIN to login: ") != account.pin:
    
    print("Wrong PIN! Access Denied.")
    
    exit()
    
    
while True:
    
    print("\n1.Deposit 2.Withdraw 3.Show Balance 4.History 5.Exit")
    
    choice = input("choose: ")
    
    if choice == "1":
        
        account.deposit(int(input("Enter amount: ")))
       
    elif choice == "2":
        
        account.withdraw(int(input("Enter amount: ")))
     
    elif choice == "3":
        
        account.show_balance()
        
    elif choice == "4":
        
        account.show_history()
        
    elif choice == "5":
        
        print("Goodby!")
        
        break
    else:
        print("Invalid choice!")
        
                            
    
    
                     
            
                 
            
                 
            
                 
        
        
        
        
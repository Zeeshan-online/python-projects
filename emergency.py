class EmergencyApp:
    
    def __init__(self):
        
        self.contacts = {
            '1': ("Police", '15'),
            
            '2': ('Ambulance', '1122'),
            
            '3': ("Fire Brigade", '16'),
            
            '4': ("Rescue Services", '1122')
        }
        
        self.running = True
        
    def show_menu(self):
        
        print("\n🚨 Emergency Assistance App 🚨")    
        
        print("-" * 35)
        
        print("1️⃣   Police")
        
        print("2️⃣   Ambulance")
        
        print("3️⃣   Fire Brigade")
        
        print("4️⃣   Rescue Services")
        
        print("5️⃣   View All Emergency Numbers")
        
        print("0️⃣   Exit")
        
        print("-" * 35)
        
    
    def handle_choice(self, choice):
        
        if choice in self.contacts:
            
            self.make_emergency_call(choice) 
            
        elif choice == '5':
            
            self.show_all_contacts()
            
        elif choice == '0':
            
            self.exit_app()
         
        else:
            print("Invalid choice!")
            
            
    def make_emergency_call(self, choice):
        
        name, number = self.contacts[choice]
        
        print(f"\n📞 Calling {name}...")
        
        print(f"\n ☎️ Dialing {number}...")
        
        print("⏳ Please stay calm. Help is on the way.") 
        
      
    def show_all_contacts(self):
        
        print("\n 📋 Emergency Contact List")
        
        print("-" * 35)
        
        for name, number in self.contacts.values():
            
            print(f" * {name}: {number}")
            
       
    def exit_app(self):
        
        print("\n👋 Exiting Emergency App")
        
        print("stay safe! ❤️")      
        
        self.running = False
        
    def run(self):
        
        while self.running:
            
            self.show_menu()
            
            choice = input("-> Select an Option: ").strip()
            
            self.handle_choice(choice)
            
if __name__ == "__main__":
    
    app = EmergencyApp()
    
    app.run()                      
        
                   
            
            
            
                       
        
        
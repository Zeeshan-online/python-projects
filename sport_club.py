class SportClub:
    
    def __init__(self):
        
        self.member = {}
        
        
    def menu(self):
        
        print() 
        
        print("⚽ Sport Club App ⚽")
        
        print("1. Add Member")
        
        print("2. Update Traning Status")
        
        print("3. View Member ")
        
        print("4. Exit")
        
        
    def add_member(self):
        
        name = input("Member Name: ")
        
        sport = input("Sport: ")
        
        coach = input("Coach Name: ")
        
        period = input("Training period: (e.g. 3 months): ")
        
        fee = float(input("Membership Fee($): "))
        
        self.member[name] = {
            
            "sport": sport,
            
            'coach': coach,
            
            "period": period,
            
            "status": "In progress",
            
            "fee": fee
        }
        
        print("Member added successfully!")
        
        
    def update_status(self):
        
        name = input("Member Name: ")
        
        if name not in self.member:
            
            print("menber not found!")
            
            return
        
        print("1. In Progress")
        
        print("2. Completed")
        
        choice = input("set status: ")
        
        self.member[name]['status'] = "completed" if choice == '2' else "In progress"
        
        print("Status updated")
        
        
    def view_member(self):
        
        if not self.member:
            
            print("No member yet!")
            return
            
            print("\\n Members list") 
            
            for name, m in self.member.items():
                
               print(f"""
                     
👨‍🏫 {name}

🏋️ Sport: {m['sport']}

🧑‍🏫 Coach: {m['coach']}

📆 Period: {m['period']}

📌 Status: {m['status']}  

💰 Fee: {m['fee']}                   
""") 
               
               
    def run(self):
        
        while True:
            
            self.menu()
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                
                self.add_member()
                
            elif choice == '2':
                
                self.update_status()
                
            elif choice == '3':
                
                self.view_member()
                
            elif choice == '4':
                
                print("See you next training!")
                
                break
            else:
                
                print("Invaid choice!")
                
SportClub().run()                                        
        
        
        
        
        
        
        
        
                
class Plumber:
    
    def __init__(self, name, rating):
        
        self.name = name
        
        self.rating = rating
        
        self.available = True
       
       
class PlumberApp:
    
    def __init__(self):
        
        self.issues = ["Leaking pipe", "Clogged Drain", "Broken Tap", 
                       "Water Heater Issue", "Low Water Pressure"]
        
        self.plumbers = [Plumber('Ali', 4.8), Plumber("Sara", 4.6), Plumber("Hassan", 4.9)]
        
    
    def show_issues(self):
        
        for i, issue in enumerate(self.issues, 1):
            
            print(f"{i}. {issue}")
            
    def recommend_plumber(self):
        
        available = [p for p in self.plumbers if p.available] 
        
        print("\\nRecommended Plumber:")
        
        for i, p in enumerate(available, 1):
            
            print(f"{i}. {p.name} ⭐ {p.rating}")
            
            return available
        
    def book_job(self, issue):
        
        
        Plumbers = self.recommend_plumber()
        
        if not Plumbers:
            
            print("❌ No plumber available"); return
            
        choice = int(input("Select Plumber Number: ")) -1
        
        if 0 <= choice < len(Plumbers):
            
            p = Plumbers[choice]; p.available = False
            
            print(f"\\n🔧 {p.name} is fixing '{issue}'...")
            
            input("Press Enter when done...")
            
            print(f"💰 Payment of ${input("Enter amount: $")} completed! ✅")
            
            
            p.available = True
            
        else: print("❌ Invalid selection")
        
    
    def menu(self):
        
        while True:
            
            print("\\n 🚰 Plumber App\\n1. Book Severice\\n2. Exit")
            
            choice = input("Choose: ")
            
            
            if choice == '1':
                
                self.show_issues()
                
                i = int(input("Issue number: ")) - 1
                
                issue = self.issues[i] if 0 <= i < len(self.issues) else "Unknow"
                
                self.book_job(issue)
                
            elif choice == "2": print("Goodbye!"); break
            
            else: print("❌ Invaid choice")
            

PlumberApp().menu()                
                
                    
            
            
            
            
                        
        
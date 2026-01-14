import datetime

import random

class TherapyApp:
    
    def __init__(self):
        
        self.journal_entries = []
        
        self.mood_logs = []
        
        self.affirmations = [
            
            'You are doing your best, and that is enough',
            
            'You are stronger than you thing',
            
            'Every day is a new beginning',
            
            "It's okay to take break",
            
            "You are worth of love and care"
        ]
        
    def show_menu(self):
        
        print("\n---- Therapy App menu ----")    
        
        print("1. Write in journal")
        
        print("2. Log mood")
        
        print("3. View past journal")
        
        print("4. Get an Affirmation")
        
        print("5. Exit")
        
        
        
    def write_journal(self):
        
        entry = input("Write your journal entry: ")
        
        timestamp = datetime.datetime.now()
        
        self.journal_entries.append((timestamp, entry))
        
        print("journal entry saved.")
        
        
    def log_mood(self):
        
        mood = input("How are you feeling today (e.g., happy, sad, anxious)? ")
        
        timestamp = datetime.datetime.now()
        
        self.mood_logs.append((timestamp, mood)) 
        
        print("Mood logged.")
        
        
    def view_journal(self):
        
        print("\n--- Past Journal Entries ---")
        
        if not self.journal_entries:
            
            print("No journal entries found.")
            
        else:
            
            for time, entry in self.journal_entries:
                
                print(f"[{time.strftime('%Y-%m-%d %H:%M')}] {entry}")
                
                
    def get_affirmation(self):
        
        affirmaton = random.choice(self.affirmations) 
        
        print(f"Affiramtion: {affirmaton}")    
        
        
    def run(self):
        
        print("Welcome to the Therapy App")
        
        while True:
            
            self.show_menu()
            
            choice = input("Select an option (1-5): ")
            
            if choice == '1':
                
                self.write_journal()
                
            elif choice == '2':
                
                self.log_mood()
                
            elif choice == '3':
                
                self.view_journal()
                
            elif choice == '4':
                
                self.get_affirmation()
                
            elif choice == '5':
                
                print("Goodby1")
                
                break
            else:
                print("Invalid input")
                
if __name__ == "__main__":
    
    app = TherapyApp()
    
    app.run()                        
                
                                           
        
               
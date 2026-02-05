class Patient:
    
    def __init__(self, pid, name, condition):
        
        self.pid = pid
        
        self.name = name
        
        self.condition = condition
        
        self.medicines = []
        
    
    def add_medicine(self, name, time):
        
        self.medicines.append((name, time))    
        
        
class NursingApp:
    
    
    def __init__(self):
        
        self.patients = {}
        
    def add_patient(self):
        
        pid = input("Enter patient ID: ")
        
        name = input("Enter patient name: ")
        
        condition = input("Condition: ")
        
        self.patients[pid] = Patient(pid, name, condition)
        
        print("Patient added")
        
    def view_patients(self):
        
        if not self.patients:
            
            print("No patients Found!")
            
            for p in self.patients.values():
                
                print(f"\\n 🩺 {p.pid} | {p.name} | {p.condition}")
                
                if p.medicines:
                    
                    print(f" 💊 {n[0]} at {n[1]}")
                    
                else:
                    print("💊 No medicines")
                    
    def add_medicine(self):
        
        pid = input("Enter patient ID: ")
        
        if pid in self.patients:
            
            name = input("Medicine name: ")
            
            time = input("Time to take medicine(Morning/Night): ")
            
            self.patients[pid].add_medicine(name, time)
            
            print("💊 Medicine scheduled")
            
        else:
            
            print("Patient not found!")
            
            
    def menu(self):
        
        while True:
            
            print("🏥 Nursing Management System")
            
            print("1. Add Patient")
            
            print("2. View Patients")
            
            print("3. Add Medicine")
            
            print("4. Exit")
            
            
            choice  = input("Choose option: ")
            
            if choice == '1':
                
                self.add_patient()
                
            elif choice == '2':
                
                self.view_patients() 
                
            elif choice == '3':
                
                self.add_medicine()
                
            elif choice == '4':
                
                print("Exiting...")
                
                break
            else:
                
                print("Invalid choice!") 
                
                
NursingApp().menu()                          
                                                                
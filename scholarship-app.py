class ScholarShipApp:
    
    def __init__(self):
        
        self.scholarships = {}
        
        
    def add_scholarship(self):
        
        name = input("Enter scholarship name: ")
        
        min_gpa = float(input("Enter mimium GPA required: "))
        
        self.scholarships[name] = {"min_gpa": min_gpa, "students": []}
        
        print("scholarship added successfully.") 
        
        
    def apply(self):
        
        name = input("student name: ")
        
        gpa = float(input("student GPA: "))
        
        sch = input("scholarship name: ")
        
        if sch in self.scholarships:
            
            self.scholarships[sch]["students"].append({"name": name, "gpa": gpa})
            
            print("application submitted successfully.")
            
        else:
            print("scholarship not found")
            
    def view_sholarships(self):
        
        for s in self.scholarships:
            
            print(f"{s}, (Min GPA: {self.scholarships[s]['min_gpa']})")   
            
            
    def check(self):
      name = input("student name: ")

      for s, data in self.scholarships.items():
          for st in data["students"]:   # ✔ correct key
             if st["name"] == name:
                status = (
                    "Eligible"
                    if st["gpa"] >= data["min_gpa"]
                    else "Not Eligible"
                )
                print(f"{s}: {status}")
                    
     
    def menu(self):
        
        while True:
            
            print("\n1. Add Scholarship\n2. Apply\n3. View\n4. Check 5.Exit")
            
            c = input("choose: ")
            
            if c == "1":
                self.add_scholarship()
                
            elif c == '2':
                self.apply()
                
            elif c == '3':
                self.view_sholarships()
                
            elif c == '4':
                self.check()
                
            elif c == '5':
                break
            
            else:
                print("invalid chouce") 
                
app = ScholarShipApp()

app.menu()                                               
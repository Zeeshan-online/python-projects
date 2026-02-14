import datetime

class Customer:
    
    def __init__(self, name, phone, car_model):
        
        self.name = name
        
        self.phone = phone
        
        self.car_model = car_model
        
        
class Servicecenter:
    
    def __init__(self):
        
        self.services = {
            
            '1': ("Oli Change", 500),
            
            '2': ("Break Repair", 1500),
            
            '3': ("Engine Repair", 5000),
            
            '4': ("Car Wash", 300),
            
            '5': ("Battery Replacement", 2000)            
        }        
        
        
    def display_services(self):
        
        print()
        
        print("Available Services: ")
        
        print("_" * 35)
        
        for key, value in self.services.items():
            
            print(f"{key}. {value[0]} - Rs. {value[1]}")
            
        print("-" * 35)
        
     
    def calculate_bill(self, selected_services):
        
        total = 0
        
        for service in selected_services:
            
            total += self.services[service][1]
         
        return total
    
    def generate_bill(self, customer, selected_services):
        
        print()
        
        print(" Generating Bill...")
        
        print("-" * 40)
        
        print(f"Customer Name: {customer.name}")
        
        print(f"phone     :{customer.phone}")
        
        print(f"Car Model :{customer.car_model}")
        
        print(f"Date    :{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("-" * 40)
        
        total = 0
        
        for service in selected_services:
            
            service_name, service_cost = self.services[service]
            
            print(f"{service_name:<25} - Rs. {price}")
            
            total += price
            
            print("-" * 40)
            
            print(f"Total Amount: Rs. {total} ")
            
            print("-" * 40)
            
            self.records.append((customer.name, total))
            
     
    def show_records(self):
        
        print()
        
        print("Service Records:")
        
        print("-" * 35)
        
        if not self.records:
            
            print("No records found.")
            
        else: 
            
            for record in self.records:
                
                print(f"Customer: {record[0]}, Total Bill: Rs. {record[1]}")  
                
        
        print("-" * 35)
        
        
class CarRepairApp:
    
    def __init__(self):
        
        self.service_center = Servicecenter()
        
        
    def main_menu(self):
        
        print("\n Welcome To Smart Car Service Center")   
        
        print("1. New Services Booking")
        
        print("2. View Service Records")
        
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            
            self.new_booking()
         
        elif choice == '2':
            
            self.center.show_records()
            
        elif choice == '3':
            
            print("Thans for using our service. Goodbye!")
            
            return
        
        else:
            print("Invalid choice! plaease try again ")
            
        
    def new_booking(self):
        
        print() 
        
        print("---New Service Booking--- ")
        
        name = input("Enter your name: ")
        
        phone = input("Enter your phone number: ")
        
        car = input("Enter your car model: ")
        
        Customer = Customer(name, phone, car)
        
        self.center.display_services()
        
        selected_services = input("Select services (comma separated numbers): ").split(",")
        
        try:
            
            selected_services = [int(s.strip()) for s in selected.split(",")]
            
            self.center.generate_bill(customer, selected_services) 
            
        except:
            
            print()
            
            print("Invalid input1")
            
            
if __name__ == "__main__":
    
    app = CarRepairApp()
    
    app.main_menu()            
                                                      
        
                        
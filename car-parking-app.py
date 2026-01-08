class ParkingSlot:
    
    def __init__(self, slot_id):
        
        self.slot_id = slot_id
        self.is_occupied = False
        
        self.vehicle_number = None
        
    def park(self, vehicle_number):
        
        self.is_occupied = True
        self.vehicle_number = vehicle_number
        
        
    def leave(self):
        
        self.is_occupied = False
        self.vehicle_number = None
        
    def info(self):
        return f"slot_id: {self.slot_id}: {"Occupied by" + self.vehicle_number if self.is_occupied else "Available"}"
    
class ParkingLot:
    
    def __init__(self, size):
        self.slots = [ParkingSlot(i+ 1) for i in range(size)]
        
        
        
    
    
    def display_slots(self):
        for slot in self.slots:
             
            print(slot.info())
            
    def park_vehicle(self, vehicle_number):
        
        for slot in self.slots:
            if not slot.is_occupied:
                slot.park(vehicle_number)
                
                print(f"Vhicle {vehicle_number} parked in slot {slot.slot_id}.")
                return
            print("sorry, parking lot is full.")
            
    def remove_vehicle(self, slot_id):
        
        if 1 <= slot_id <= len(self.slots):
            slot = self.slots[slot_id -1]
            
            if slot.is_occupied:
               print(f"Vehicle {slot.vehicle_number} left slot {slot.slot_id}")
               
               slot.leave()
               
            else:
                print(f"Slot is already empty. ")
                
                                   
def main():
     
    lot_size = int(input("Enter number of parking slots: "))
    
    lot = ParkingLot(lot_size) 
    
    while True:
        
        print("\n1. Park Vehicle\n2. Remove Vehicle\n3. View Slots\n4. Exit")
        
        choice = input("Enter your choice: ")                     
                
        if choice == '1':
            v_num = input("Enter vechicle number: ")
            
            lot.park_vehicle(v_num)  
         
        elif choice == '2':
            
            try:
                slot_id = int(input("Enter slot id to remove vehicle from: "))
                
                lot.remove_vehicle(slot_id)
                
            except ValueError:
                
                print("Please enter valid number")
                
        elif choice == '3':
            
            lot.display_slots()
            
        elif choice == '4':
            
            print("Exiting...")
            
            break
        else:
            print("Invalid choice. please try againg")
            
if __name__ == '__main__':
    
    main()                           
               
                  
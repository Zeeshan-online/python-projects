# flight booking app

class Flight:
    
    # crate a flight
    
    def __init__(self, code, seats, price):
        
        self.code = code
        
        self.seats = seats
        
        self.price = price
        
class FlinghtBookingSystem:
    
    # init system
    
    def __init__(self):
        
        self.flights = {}
        
        self.ticket_id = 1
        
        # add flight
        
    def add_flight(self, code, seats, price):
        
        self.flights[code] = Flight(code, seats, price)
        
        # view all flight
        
    def view_flights(self):
        
        for f in self.flights.values():
            
            print(f"{f.code} | Seats Left: {f.seats} | price: ${f.price}")
            
    #  book a seat
    
    def book_seat(self, code):
        
        if code in self.flights and self.flights[code].seats > 0:
            
            self.flights[code].seats -= 1
            
            print("Seat booked!")
            
            return self.flights[code].price 
        else:
            print("Not available!")
            
            return None
        
        # process system
        
        def pay(self, amount):
            
            print(f"Payment of ${amount} successful!")
            
        # generate ticket receipt
        
        def generate_ticket(self, flight_code, amount):
            
            print("\n ===== TICKET PECEIPT =====")
            
            print(f"TICKET ID: {self.ticket_id}")
            
            print(f"Flight Code: {flight_code}")
            
            print(f"Amount Paid: ${amount}")
            
            print("Status: confirmed")
            
            print("=====================") 
            
            self.ticket_id += 1 
           
system = FlinghtBookingSystem()

while True:
    
    print("\n Flight Booking System")
    
    print("1 Add Flight")
    
    print("2 View Flights")
    
    print("3 Book & Pay")
    
    print("4 Exit")
    
    ch = input("Select Option: ") 
    
    if ch == "1":
        
        code = input("Enter Flifgt code: ")
        
        seats = int(input("Enter total seats: "))
        
        price = int(input("Enter ticket price: "))           
          
        system.add_flight(code, seats, price)
        
    elif ch == "2":
        
        system.view_flights()
        
    elif ch == "3":
        
        code = input("Enter flight code: ")        
        
        price = system.book_seat()
        
        if price:
            
            confirm = input(f"Pay $ {price}? (y/n): ")
            
            if confirm.lower() == "y":
                
                system.pay(price)
                
                system.generate_ticket(code, price)
                
            else: 
                print("Payment canceled!")
                
    elif ch == "4":
        
        print("Goodbye!")
        
        break
    
    else:
        print("Invalid Option!")                                              
class Workout:
    
    def __init__(self):
        self.plan = {}
        
    def add_workout(self, day, workout):
        if day in self.plan:
            self.plan[day].append(workout)
        else:
            self.plan[day] = [workout]
            
    def view_plan(self):
        if not self.plan:
            print("No workouts added yet.")
        else:
            for day, workouts in self.plan.items():
                print(f"{day}: {', '.join(workouts)}")
                
    def delete_day(self, day):
        if day in self.plan:
            del self.plan[day]
            print(f"Deleted workouts for {day}.")
        else:
            print("Day not found")
            

def main():
    workout_app = Workout()   
    
    while True:
        print("\n-----Bodybuilding App-----")
        print("1. Add Workout")
        print("2. View Plan")
        print("3. Delete Day")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            day = input("Enter the day (e.g, Monday): ")
            exercise = input("Enter the exercise (e.g, Chest Workout): ")
            workout_app.add_workout(day, exercise)
        
        elif choice == "2":
            workout_app.view_plan()
            
        elif choice == "3":
            day = input("Enter the day to delete (e.g, Monday): ")
            workout_app.delete_day(day)
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
                                  

if __name__ == "__main__":
    main()

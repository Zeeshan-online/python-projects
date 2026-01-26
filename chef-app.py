class ChefApp:

    def __init__(self):
        self.recipes = {}

    def menu(self):
        print("\n 👨‍🍳 Chef App")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Total Kitchen Cost")
        print("4. Exit")

    def add_recipe(self):
        name = input("Recipe name: ").title()
        ingredients = input("Ingredients: ")
        cost = float(input("Total cost ($): "))
        self.recipes[name] = (ingredients, cost)
        print("✅ Recipe Added!")

    def view_recipes(self):
        if not self.recipes:
            print("No recipe found")
            return

        for r, (i, c) in self.recipes.items():
            print(f"🍽️ {r} → {i} | ${c}")

    def total_cost(self):
        total = sum(c for _, c in self.recipes.values())
        print(f"🍜 Total Kitchen Cost: ${total}")

    def run(self):
        while True:
            self.menu()
            choice = input("Choose: ")

            if choice == '1':
                self.add_recipe()
            elif choice == '2':
                self.view_recipes()
            elif choice == '3':
                self.total_cost()
            elif choice == '4':
                print("👋 Goodbye chef!")
                break
            else:
                print("Invalid choice")


ChefApp().run()

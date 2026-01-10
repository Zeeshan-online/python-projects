class IQtestApp:

    def __init__(self):
        self.question = {
            'what is 5 + 7?': '12',
            'what number next: 2, 4, 8, 16?': '32',
            "if All is to 3, then Hello is to what?": '5',
            'What is the opposite of ODD?': 'even',
            'which is heavier, 1kg of feathers or 1kg of lead?': 'neither',
        }
        self.score = 0

    def display_menu(self):
        print("\nIQ test menu:\n1. Take Test\n2. Show score\n3. Exit")
        choice = input("Enter your choice: ").strip()

        actions = {
            '1': self.take_test,
            '2': self.show_score,
            '3': self.exit_app
        }
        actions.get(choice, self.invalid)()

    def invalid(self):
        print("Invalid choice try again.")

    def take_test(self):
        self.score = 0
        for q, a in self.question.items():
            ans = input(q + " ").strip().lower()
            if ans == a:
                self.score += 1

        print(f"Test completed! You scored {self.score}/{len(self.question)}")

    def show_score(self):
        print(f"Your current score is {self.score}/{len(self.question)}")

    def exit_app(self):
        print("Exiting the application. Goodbye!")
        raise SystemExit


# ✅ MUST be outside the class
if __name__ == "__main__":
    app = IQtestApp()
    while True:
        app.display_menu()

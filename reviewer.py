import random

class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def ask(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        user_answer = input("Enter your answer: ").upper()
        if user_answer == self.answer:
            print("Correct!\n")
        else:
            print("Incorrect. The correct answer is", self.answer + "\n")

class MultipleChoiceReviewer:
    def __init__(self):
        self.questions = []
        self.wrong_questions = []

    def add_question(self, question):
        self.questions.append(question)

    def ask_questions(self):
        shuffled_questions = random.sample(self.questions, len(self.questions))  # Shuffle the questions
        for question in shuffled_questions:
            question.ask()
            input("Press Enter to continue to the next question...")

    def retry(self):
        if not self.wrong_questions:
            print("You got all questions correct. There are no questions to retry.")
            return

        random.shuffle(self.wrong_questions)  # Shuffle the incorrect questions
        for question in self.wrong_questions:
            question.ask()
            input("Press Enter to continue to the next question...")

if __name__ == "__main__":
    reviewer = MultipleChoiceReviewer()

    # Add some questions to the reviewer
    reviewer.add_question(Question("They are expected to perform variety of tasks depending on their specialization and job level?", ["A. Manager", "B. Senior", "C. Engineer", "D. Chief Manager"], "C"))
    reviewer.add_question(Question("People make possible the realization of human dreams by extending their reach in the real world, what is this?", ["A. Building", "B. Experimenting", "C. Prototyping", "D. Engineering"], "D"))
    reviewer.add_question(Question("They are the practitioners of the art of managing the application of science and mathematics?", ["A. Engineer", "B. Scientist", "C. Physicist", "D. Developer"], "A"))
    reviewer.add_question(Question("a “creative problem-solving process of planning, organizing, leading and controlling an organization’s resources to achieve its mission and objectives”.?",
                 ["A. Manager", "B. Management", "C. Human Resources", "D. Superior"], "B"))
    reviewer.add_question(Question("Three levels of Management?",
                 ["A. Middle, First-line, Head", "B. First-line, Middle, Executive", "C. Top, Mid, Bot", "D. First-line, Middle, Top"], "D"))
    reviewer.add_question(Question("distinguished from other managers because he [or she] possesses both an ability to apply engineering principles and a skill in organizing and directing people and projects?",
                 ["A. Engineering Executive", "B. Engineering Technician", "C. Engineering Manager", "D. Engineering Supervisor"], "C"))






    while True:
        # Ask the user the questions
        reviewer.ask_questions()

        # Give the user the option to retry
        if reviewer.wrong_questions:
            print("You got some questions wrong. Let's retry them.")
            reviewer.retry()
        else:
            print("Congratulations! You got all the questions correct.")

        retry_choice = input("Do you want to retry the entire quiz? (yes/no): ").lower()
        if retry_choice != "yes":
            break

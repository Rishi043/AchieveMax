# from pywebio.input import *
# from pywebio.output import *
# from pywebio.session import *
# from pywebio import start_server

# def mock_test():
#     score = 0
#     questions = [
#         {
#             'question': "Samuel covers the distance from his home to his office at a speed of 25 km/hr and comes back at a speed of 4 km/hr. He completes the whole journey within 5 hours 48 minutes. Find out the distance from his home to office:",
#             'options': ["20 km", "18 km", "15 km", "25 km"],
#             'answer': "20 km"
#         },
#         {
#             'question': "Samuel covers the distance from his home to his office at a speed of 25 km/hr and comes back at a speed of 4 km/hr. He completes the whole journey within 5 hours 48 minutes. Find out the distance from his home to office:",
#             'options': ["9", "8", "10", "6"],
#             'answer': "6"
#         },
#         {
#             'question': "A policeman sees a thief at a distance of 100 meters and starts to chase him. The thief sees him and starts to run too. If the thief is running at the speed of 8 km/hr and the policeman is running at the speed of 10 km/hr, find out the distance covered by the thief before the policeman catches him.",
#             'options': ["250 meters", "400 meters", "450 meters", "401 meters"],
#             'answer': "400 meters"
#         },
#         {
#             'question': "Paul has to travel 24 km. After walking for 1 hour 40 minutes he sees that he has covered 5/7 of the distance left to cover. Find out Paul’s speed in meters per second.",
#             'options': ["5/3 m/s", "7/5 m/s","2/3 m/s","8/5 m/s"],
#             'answer': "5/3 m/s"
#         },
#         {
#             'question': "The ratio of the speed of two trains is 7:8. If the second train covers 400 km in 4 h, find out the speed of the first train.",
#             'options': ["69.4 km/h", "78.6 km/h", "87.5 km/h", "40.5 km/h"],
#             'answer': "87.5 km/h"
#         },
#         {
#             'question': "How many terms are there in 3,9,27,81........531441?",
#             'options': ["25", "12","13","14"],
#             'answer': "12"
#         },
#         {
#             'question': "If the average of four consecutive odd numbers is 16, find the smallest of these numbers?",
#             'options': ["5", "7","13","11"],
#             'answer': "13"
#         },
#         {
#             'question': "If the sum of two numbers is 13 and the sum of their square is 85. Find the numbers?",
#             'options': ["6 & 7", "5 & 7","6 & 0","5 & 8"],
#             'answer': "6 & 7"
#         },
#         {
#             'question': "The difference between a two-digit number and the number obtained by interchanging the positions of its digits is 36. What is the difference between the two digits of that number?",
#             'options': ["4", "9","8","None of these"],
#             'answer': "4"
#         },
#         {
#             'question': "A two-digit number is such that the product of the digits is 12. When 9 is subtracted from the number, the digits are reversed. The number is:",
#             'options': ["34", "62","43","26"],
#             'answer': "43"
#         }
#     ]
    
#     put_markdown("# Mock Test")
#     name = input("Enter your name: ", type="text")
    
#     for i, question in enumerate(questions, 1):
#         put_markdown(f"### Question {i}: {question['question']}")
#         answer = radio("Select an option:", options=question['options'])
#         if answer == question['answer']:
#             score += 1
#         put_text("")  # Add a blank line for spacing
    
#     put_markdown("## Test Result")
#     put_text(f"Name: {name}")
#     put_text(f"Score: {score}/{len(questions)}")
#     if score >= len(questions) / 2:
#         put_text("Result: Passed")
#     else:
#         put_text("Result: Failed")

# if __name__ == "__main__":
#     start_server(mock_test, port=8080)




import tkinter as tk
from tkinter import messagebox

class MockTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mock Test")
        self.root.geometry("900x600+290+70")
        root.resizable (False, False)




        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                'question': "Samuel covers the distance from his home to his office at a speed of 25 km/hr and comes back at a speed of 4 km/hr. He completes the whole journey within 5 hours 48 minutes. Find out the distance from his home to office:",
                'options': ["20 km", "18 km", "15 km", "25 km"],
                'answer': "20 km"
            },
            {
                'question': "Samuel covers the distance from his home to his office at a speed of 25 km/hr and comes back at a speed of 4 km/hr. He completes the whole journey within 5 hours 48 minutes. Find out the distance from his home to office:",
                'options': ["9", "8", "10", "6"],
                'answer': "6"
            },
            {
                'question': "A policeman sees a thief at a distance of 100 meters and starts to chase him. The thief sees him and starts to run too. If the thief is running at the speed of 8 km/hr and the policeman is running at the speed of 10 km/hr, find out the distance covered by the thief before the policeman catches him.",
                'options': ["250 meters", "400 meters", "450 meters", "401 meters"],
                'answer': "400 meters"
            },
            {
                'question': "Paul has to travel 24 km. After walking for 1 hour 40 minutes he sees that he has covered 5/7 of the distance left to cover. Find out Paul’s speed in meters per second.",
                'options': ["5/3 m/s", "7/5 m/s","2/3 m/s","8/5 m/s"],
                'answer': "5/3 m/s"
            },
            {
                'question': "The ratio of the speed of two trains is 7:8. If the second train covers 400 km in 4 h, find out the speed of the first train.",
                'options': ["69.4 km/h", "78.6 km/h", "87.5 km/h", "40.5 km/h"],
                'answer': "87.5 km/h"
            },
            {
                'question': "How many terms are there in 3,9,27,81........531441?",
                'options': ["25", "12","13","14"],
                'answer': "12"
            },
            {
                'question': "If the average of four consecutive odd numbers is 16, find the smallest of these numbers?",
                'options': ["5", "7","13","11"],
                'answer': "13"
            },
            {
                'question': "If the sum of two numbers is 13 and the sum of their square is 85. Find the numbers?",
                'options': ["6 & 7", "5 & 7","6 & 0","5 & 8"],
                'answer': "6 & 7"
            },
            {
                'question': "The difference between a two-digit number and the number obtained by interchanging the positions of its digits is 36. What is the difference between the two digits of that number?",
                'options': ["4", "9","8","None of these"],
                'answer': "4"
            },
            {
                'question': "A two-digit number is such that the product of the digits is 12. When 9 is subtracted from the number, the digits are reversed. The number is:",
                'options': ["34", "62","43","26"],
                'answer': "43"
            }
        ]

        # self.name_label = tk.Label(root, text="Enter your name:", font=("Elephant",15,'bold'))
        # self.name_label.pack()
        # self.name_entry = tk.Entry(root)
        # self.name_entry.pack()
        
        
        self.name_label = tk.Label(root, text="Enter your name:", font=("Elephant", 16, 'bold'))
        self.name_label.place(x=350, y=60)
        
        # Create and place the entry widget
        self.name_entry = tk.Entry(root)
        self.name_entry.place(x=350, y=105)
        self.txt_email=Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        
        
        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack()
        
        self.option_vars = []
        self.option_buttons = []

        for _ in range(4):
            var = tk.StringVar(value="")
            btn = tk.Radiobutton(root, variable=var, value="", text="", wraplength=400)
            self.option_vars.append(var)
            self.option_buttons.append(btn)
            btn.pack(anchor="w")

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=f"Question {self.current_question + 1}: {question['question']}")
        
        for i, option in enumerate(question['options']):
            self.option_vars[i].set(option)
            self.option_buttons[i].config(text=option, value=option)
        
    def next_question(self):
        selected_option = None
        for var in self.option_vars:
            if var.get():
                selected_option = var.get()
                break
        
        if selected_option == self.questions[self.current_question]['answer']:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.question_label.pack_forget()
        for btn in self.option_buttons:
            btn.pack_forget()
        self.next_button.pack_forget()

        name = self.name_entry.get()
        result_text = f"Name: {name}\nScore: {self.score}/{len(self.questions)}\n"
        result_text += "Result: Passed" if self.score >= len(self.questions) / 2 else "Result: Failed"
        
        self.result_label.config(text=result_text)
        self.result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MockTestApp(root)
    root.mainloop()
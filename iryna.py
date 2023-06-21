import tkinter as tk
from tkinter import messagebox
import time
import random
import math

class MentalMathQuiz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mental Math Quiz")
        
        self.timer_label = tk.Label(self.window, text="Time Left: ")
        self.timer_label.pack()
        
        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()
        
        self.answer_entry = tk.Entry(self.window)
        self.answer_entry.pack()
        
        self.submit_button = tk.Button(self.window, text="Submit", command=self.check_answer)
        self.submit_button.pack()
        
        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack()
        
        self.time_limit = 300  # Час на виконання тесту (в секундах)
        self.score = 0
        self.num_questions = 300
        self.current_question = 0
        self.start_time = time.time()
        
        self.generate_question()
        self.start_timer()
        
        self.window.mainloop()
    
    def generate_question(self):
        if self.current_question < self.num_questions:
            question_type = random.choice(["addition", "subtraction", "multiplication", "division"])
            
            operand1 = 0  # Задаємо початкове значення
            
            if question_type == "addition":
                operand1 = random.randint(-100, 2000)
                operand2 = random.randint(-100, 2000)
                operator = "+"
                answer = operand1 + operand2
            
            elif question_type == "subtraction":
                operand1 = random.randint(-101, 2000)
                operand2 = random.randint(-100, operand1)
                operator = "-"
                answer = operand1 - operand2
            
            elif question_type == "multiplication":
                operand1 = random.randint(-11, 100)
                operand2 = random.randint(-10, 100)
                operator = "*"
                answer = operand1 * operand2
            
            elif question_type == "division":
                operand2 = random.randint(1, 100)
                answer = random.randint(1, 100)
                operand1 = operand2 * answer
                operator = "/"
            
            # elif question_type == "square_equation":
            #     operand1 = random.randint(1, 10)
            #     operand2 = random.randint(-10, 10)
            #     operand3 = random.randint(-10, 10)
            #     operator = "x^2 + {}x + {} = 0".format(operand2, operand3)
            #     answer = "No Solution"
            #     if operand2**2 - 4*operand1*operand3 >= 0:
            #         x1 = (-operand2 + math.sqrt(operand2**2 - 4*operand1*operand3)) / (2*operand1)
            #         x2 = (-operand2 - math.sqrt(operand2**2 - 4*operand1*operand3)) / (2*operand1)
            #         answer = "x1 = {}, x2 = {}".format(x1, x2)
                
            self.current_question += 1
            self.question_label.config(text="Question {}: {} {} {} = ?".format(
                self.current_question, operand1, operator, operand2))
            self.correct_answer = answer
            self.answer_entry.delete(0, tk.END)
        else:
            self.finish_quiz()

    
    def check_answer(self):
        user_answer = self.answer_entry.get()
        
        if user_answer == str(self.correct_answer):
            self.score += 1
            self.score_label.config(text="Score: {}".format(self.score))
        
        self.generate_question()
    
    def start_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        
        if elapsed_time >= self.time_limit:
            self.finish_quiz()
        else:
            time_left = self.time_limit - elapsed_time
            self.timer_label.config(text="Time Left: {}s".format(time_left))
            self.window.after(1000, self.start_timer)
    
    def finish_quiz(self):
        self.window.withdraw()  # Приховуємо вікно гри
        messagebox.showinfo("Quiz Finished", "Quiz Finished!\nYour Score: {}".format(self.score))
        self.window.quit()  # Закриваємо вікно
    
quiz = MentalMathQuiz()

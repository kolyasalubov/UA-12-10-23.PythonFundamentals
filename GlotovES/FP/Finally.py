import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


class Students:
    def __init__(self, csv_file='students.csv'):
        self.file_path = csv_file
        try:
            self.df = pd.read_csv(csv_file)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=['Full Name', 'Math', 'Physics', 'Chemistry', 'Literature', 'Informatics'])
            self.df.to_csv(csv_file, index=False)

    def print_menu(self):
        print("1. Add student")
        print("2. Remove student")
        print("3. Get student statistics")
        print("4. Get subject statistics")
        print("5. Get group statistics")
        print("6. Get average scores")
        print("0. Exit")

    def process_choice(self, choice):
        if choice == 1:
            self.add_student()
        elif choice == 2:
            self.remove_student()
        elif choice == 3:
            self.get_student_statistics()
        elif choice == 4:
            self.get_subject_statistics()
        elif choice == 5:
            self.get_group_statistics()
        elif choice == 6:
            self.calculate_average_grades()
        elif choice == 0:
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")

    def add_student(self):
        full_name = input("Enter student's full name: ")
        math = int(input("Enter Math grade: "))
        physics = int(input("Enter Physics grade: "))
        chemistry = int(input("Enter Chemistry grade: "))
        literature = int(input("Enter Literature grade: "))
        informatics = int(input("Enter Informatics grade: "))
        
        new_student = pd.DataFrame([[full_name, math, physics, chemistry, literature, informatics]],
                                   columns=['Full Name', 'Math', 'Physics', 'Chemistry', 'Literature', 'Informatics'])
        self.df = pd.concat([self.df, new_student], ignore_index=True)
        self.df.to_csv(self.file_path, index=False)

    def remove_student(self):
        full_name = input("Enter student's full name to remove: ")
        try:
            self.df = self.df[self.df['Full Name'] != full_name]
            self.df.to_csv(self.file_path, index=False)
            print(f"Student {full_name} removed successfully.")
        except KeyError:
            print("Student not found.")



    def get_student_statistics(self):
        full_name = input("Enter student's full name: ")
        try:
            student_data = self.df[self.df['Full Name'] == full_name]
            statistics = student_data.iloc[:, 1:].astype(float)
            print(f"Statistics for {full_name}:\n{statistics}")
        except KeyError:
            print("Student not found.")

    def get_subject_statistics(self):
        subject = input("Enter subject: ")
        try:
            statistics = self.df[subject].astype(float)
            print(f"Statistics for {subject}:\n{statistics}")
        except KeyError:
            print("Invalid subject.")

    def get_group_statistics(self):
        try:
            statistics = self.df.iloc[:, 1:].astype(float)            
            print(f"Group statistics:\n{statistics}")
            self.plot_group_statistics()
        except KeyError:
            print("No data available for group statistics.")

    def plot_group_statistics(self):
        try:
            group_statistics = self.df.iloc[:, 1:].astype(float)
            group_statistics.plot(kind='bar', figsize=(8, 4))
            plt.title('Group Statistics')
            plt.xlabel('Metrics')
            plt.ylabel('Values')
            plt.show()
        except KeyError:
            print("No data available for group statistics.")


    def calculate_average_grades(self):
        try:
            grades = self.df.iloc[:, 1:].astype(float)
            average_grades = np.mean(grades, axis=0)
            
            for subject, average_grade in zip(grades.columns, average_grades):
                print(f"Average grade for {subject}: {average_grade:.2f}")
        except KeyError:
            print("No data available for average grades calculation.")


students_manager = Students()


print("Initial data:")
print(students_manager.df)
print()

while True:
    students_manager.print_menu()
    try:
        user_choice = int(input("Enter your choice: "))
        students_manager.process_choice(user_choice)
    except ValueError:
        print("Invalid input. Please enter a number.")

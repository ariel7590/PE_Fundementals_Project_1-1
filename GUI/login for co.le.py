from tkinter import *

from .Courses import Course
from .Subjects import Question
from .Tests import Tests
from .managment import Management
from .files import Files
my_files = Files()
my_management = Management()
my_tests = Tests()
my_questions = Question()
my_courses = Course()


class Login:

    def __init__(self, master):
        frame = Frame(master)

        self.local_master = master

        master.title("Sorting tool for academy")
        self.e1 = Label(master, text="Login:")
        self.e1.grid(row=0, sticky=E)

        self.e1 = Entry(master, width=20)
        self.e1.grid(row=0, column=1, columnspan=10, padx=10, pady=10)

        self.e2 = Label(master, text="Password:")
        self.e2.grid(row=1, sticky=E)

        self.e2 = Entry(master, width=20)
        self.e2.grid(row=1, column=1, columnspan=10, padx=10, pady=10)

        self.c = Checkbutton(master, text='keep me logged in')
        self.c.grid(columnspan=2)

        self.verification_button = Button(master, text="Accept", padx=10, pady=5, command=self.my_click)
        self.verification_button.grid(row=3, column=1)


    def my_exams_adder(self):


        key = int(input('which format would you like?\npress 1 for docx.\npress 2 for pdf\npress 3 for jpeg'))
        if key == 1:
            my_tests.add_element(my_files.add_docx_file())
        elif key == 2:
            my_tests.add_element(my_files.add_pdf_file())
        else:
            my_tests.add_element(my_files.add_jpeg_file())

    def my_exams_remover(self):
        key1 = int(input('which format would you like?\npress 1 for docx.\npress 2 for pdf\npress 3 for jpeg'))
        if key1 == 1:
            key2 = int(input('to delete all the elements of the list - press 1\nto delete s specific element - press 2'))
            if key2 == 1:
                my_tests.remove_all()

            elif key2 == 2:
                index = int(input('choose an index:'))
                my_tests.remove(index)

        elif key1 == 2:
            my_tests.add_element(my_files.add_pdf_file())
        else:
            my_tests.add_element(my_files.add_jpeg_file())

    def my_exams(self, key):
        top = Toplevel(self.local_master)

        Label(top, text="choose one of the following options:").grid(row=0, sticky=W)

        button1 = Button(top, text="Add new exam", command=self.my_exams_adder)
        button1.grid(row=1, sticky=W)

        button2 = Button(top, text="Add new exam", command=self.my_exams_remover)
        button2.grid(row=1, sticky=W)

        button3 = Button(top, text="Questions", command=self.my_questions)
        button3.grid(row=2, sticky=W)

        button4 = Button(top, text="Lecturers", command=self.my_lecturers)
        button4.grid(row=3, sticky=W)

    def my_questions(self, key):
        print('hello')

    def my_lecturers(self, key):
        print('hello')

    def calculus1(self):
        top1_level = Toplevel(self.local_master)

        Label(top1_level, text="choose one of the following options:").grid(row=0, sticky=W)

        button1 = Button(top1_level, text="Exams", command=lambda: self.my_exams(1))
        button1.grid(row=1, sticky=W)

        button2 = Button(top1_level, text="Questions", command=lambda: self.my_questions(1))
        button2.grid(row=2, sticky=W)

        button3 = Button(top1_level, text="Lecturers", command=lambda: self.my_lecturers(1))
        button3.grid(row=3, sticky=W)

    def calculus2(self):
        top1_level = Toplevel(self.local_master)

        Label(top1_level, text="choose one of the following options:").grid(row=0, sticky=W)

        button1 = Button(top1_level, text="Exams", command=lambda: self.my_exams(2))
        button1.grid(row=1, sticky=W)

        button2 = Button(top1_level, text="Questions", command=lambda: self.my_questions(2))
        button2.grid(row=2, sticky=W)

        button3 = Button(top1_level, text="Lecturers", command=lambda: self.my_lecturers(2))
        button3.grid(row=3, sticky=W)

    def linear_algebra(self):
        top1_level = Toplevel(self.local_master)

        Label(top1_level, text="choose one of the following options:").grid(row=0, sticky=W)

        button1 = Button(top1_level, text="Exams", command=lambda: self.my_exams(3))
        button1.grid(row=1, sticky=W)

        button2 = Button(top1_level, text="Questions", command=lambda: self.my_questions(3))
        button2.grid(row=2, sticky=W)

        button3 = Button(top1_level, text="Lecturers", command=lambda: self.my_lecturers(3))
        button3.grid(row=3, sticky=W)

    def cs_introduction(self):
        top1_level = Toplevel(self.local_master)

        Label(top1_level, text="choose one of the following options:").grid(row=0, sticky=W)

        button1 = Button(top1_level, text="Exams", command=lambda: self.my_exams(4))
        button1.grid(row=1, sticky=W)

        button2 = Button(top1_level, text="Questions", command=lambda: self.my_questions(4))
        button2.grid(row=2, sticky=W)

        button3 = Button(top1_level, text="Lecturers", command=lambda: self.my_lecturers(4))
        button3.grid(row=3, sticky=W)

    def Architecture1(self):
        top1_level = Toplevel(self.local_master)

        Label(top1_level, text="choose one of the following options:").grid(row=0, sticky=W)

        button1 = Button(top1_level, text="Exams", command=lambda: self.my_exams(5))
        button1.grid(row=1, sticky=W)

        button2 = Button(top1_level, text="Questions", command=lambda: self.my_questions(5))
        button2.grid(row=2, sticky=W)

        button3 = Button(top1_level, text="Lecturers", command=lambda: self.my_lecturers(5))
        button3.grid(row=3, sticky=W)

    def Architecture2(self):
        top1_level = Toplevel(self.local_master)

        Label(top1_level, text="choose one of the following options:").grid(row=0, sticky=W)

        button1 = Button(top1_level, text="Exams", command=lambda: self.my_exams(6))
        button1.grid(row=1, sticky=W)

        button2 = Button(top1_level, text="Questions", command=lambda: self.my_questions(6))
        button2.grid(row=2, sticky=W)

        button3 = Button(top1_level, text="Lecturers", command=lambda: self.my_lecturers(6))
        button3.grid(row=3, sticky=W)


    def my_click(self):
        login = "victor"
        password = "cohen"

        user_login = self.e1.get()
        user_password = self.e2.get()
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        print(self.e1.get())
        print(self.e2.get())

        if user_login != login and user_password != password:
            my_label = Label(self.local_master, text="wrong login and wrong password")
            my_label.grid(row=4, column=1)

        elif user_login != login:
            my_label = Label(self.local_master, text="wrong login")
            my_label.grid(row=4, column=1)

        elif user_password != password:
            my_label = Label(self.local_master, text="wrong password")
            my_label.grid(row=4, column=1)
        else:
            new_label = Label(self.local_master, text="welcome " + user_login)
            new_label.grid(row=5, column=1)

            top1_level = Toplevel(self.local_master)

            Label(top1_level, text="choose one of the following courses :").grid(row=0, sticky=W)

            button1 = Button(top1_level, text="Calculus 1", command=self.calculus1)
            button1.grid(row=1, sticky=W)

            button2 = Button(top1_level, text="Calculus 2", command=self.calculus2)
            button2.grid(row=2, sticky=W)

            button3 = Button(top1_level, text="Linear algebra 2", command=self.linear_algebra)
            button3.grid(row=3, sticky=W)

            button4 = Button(top1_level, text="Computer science Introduction 2", command=self.cs_introduction)
            button4.grid(row=4, sticky=W)

            button5 = Button(top1_level, text="Architecture 1", command=self.Architecture1)
            button5.grid(row=5, sticky=W)

            button5 = Button(top1_level, text="Architecture 1", command=self.Architecture2)
            button5.grid(row=5, sticky=W)




root = Tk()
beta = Login(root)
root.mainloop()







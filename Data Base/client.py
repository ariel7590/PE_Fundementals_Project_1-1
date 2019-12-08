# coding=utf-8

"""
Create a connection to the remote server
input: None.
output: socket connection
"""
from pip._vendor.distlib.compat import raw_input


def connect():
    import socket

    my_soc = socket.socket()
    my_soc.connect(('127.0.0.1', 8482))
    return my_soc


"""
choosing between few options and in each option creating command to be send to the server
input: the user choice from the menu and parameter that the user typed.
output: print a massage to the screen and create a recvest for the server by the data protocol
"""


def get_param(choice):
    if choice == '1':
        print("Type the sub subject: ")
        return "SSUB" + raw_input()
    elif choice == '2':
        print("Enter the subject name: ")
        return "SUBJ" + raw_input()
    elif choice == '3':
        print("Enter the subject ID: ")
        return "FID" + raw_input()
    else:
        print("Sorry, no can do my friend :( ")


"""
print a menu to the screen
input: None
output: choice that typed by the user
"""


def menu():
    print("Hello dear Friend, what would you like to do?")
    print(" 1. find question by sub subject")
    print(" 2. find all questions in subject")
    print(" 3. find question difficulty by id.")
    print(" 6. quit")
    return raw_input()


def main():
    client_socket = connect()
    while True:
        choice = menu()
        if choice == '6':
            client_socket.close()
            print(
                "█████████████████████████████████████████████████████████████████████████████████████████████████████████████\n█░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█\n█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█\n█░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░███████░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█\n█░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░███████████████░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████\n█░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░███████░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█\n█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█\n█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░███████░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█\n█░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀░░███████████████░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████\n█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░███████░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█\n█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█\n█░░░░░░░░░░░░░░░░███████░░░░░░███████░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░░███████░░░░░░███████░░░░░░░░░░░░░░█\n█████████████████████████████████████████████████████████████████████████████████████████████████████████████\n")
            break
        command = get_param(choice)
        client_socket.send(command)
        data = client_socket.recv(1024)
        print(data)


main()

subject_dict = {}

"""
this function parsed the database into a list of dicts
input: None
output: the parsed dict
"""


def parsing():
    file_ob = open('DB.txt', 'r')
    file_data = file_ob.read()
    file_ob.close()
    file_data = file_data.split('#')
    file_data = file_data[1:]

    for subject in file_data:
        subject_list = []
        first_star = subject.index('*')
        subject_name = subject[:first_star]
        subject_name = subject_name.replace('\n', '')

        questions = subject[first_star+1:]
        questions = questions.split('*')

        for question in questions:
            question_dict = {}
            question_params = question.split('::')
            question_dict["sub_subject"] = question_params[0]
            question_dict["difficulty_level"] = question_params[1]
            question_dict["test_or_quiz"] = question_params[2]
            question_dict["year"] = question_params[3]
            question_dict["semester"] = question_params[4]
            question_dict["file_format"] = question_params[5]
            question_dict["is_solved"] = question_params[6]
            question_dict["file_path"] = question_params[7]
            question_dict["question_id"] = question_params[8]
            subject_list.append(question_dict)
            subject_dict[subject_name] = subject_list


"""
this function control the internet side of the server and setup the socket
and listen to a connection from the user
input: None.
output: the socket created return the socket that the client connected
"""


def connect():
    import socket

    serv_soc = socket.socket()
    serv_soc.bind(("0.0.0.0", 8482))

    serv_soc.listen(1)
    client_soc, client_address = serv_soc.accept()

    return client_soc, serv_soc

"""
split the data from the client to command and the parameters
input: client data
output: the protocol command and the parameter from the user
"""


def slicing(client_data):
    command = client_data[:3]
    pram = client_data[3:]
    return command, pram

"""
the following functions search for the user reqeust by the command and parameter
input: command and parameter
output: respond to send back to the client

"""


def searching(command, pram):
    if command == "SSUB":
        return SSUB(pram)
    elif command == "SUBJ":
        return SUBJ(pram)
    elif command == "FID":
        return find_in_question(pram, "difficulty_level")



def SSUB(parm):
    for subject in subject_dict.values():
        for question in subject:
            if parm.lower() in question["sub_subject"].lower():
                return question[""]
    return None


def SUBJ(parm):
    question_list = []
    if parm.capitalize() in subject_dict.keys():
        for question in subject_dict[parm.capitalize()]:
            question_list.append(question["file_path"])
    return '\n'.join(question_list)


def find_in_question(parm, command):
    for subject in subject_dict.values():
        for question in subject:
            if parm.lower() in question["question_id"].lower():
                return question[command]
    return None



def main():
    parsing()
    client_soc, serv_soc = connect()
    while True:
        client_data = client_soc.recv(1024)
        if not(client_data):  # closing the network connection if there is no data from the client
            client_soc.close()
            serv_soc.close()
            break
        command, pram = slicing(client_data)
        answer = searching(command, pram)
        client_soc.send(answer)  # send the suitable response back to the client


main()

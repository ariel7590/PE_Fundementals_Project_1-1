"""from files import Files
something = Files()
something.add_file()"""

class Management:
    def __init__(self):
        self.lecturers = []

    def insert(self, lec_login, lec_password): #the user puting a login and password dor the lecturer for accessing the system
        if len(self.lecturers) == 0: #case 1 - the list is empty
            pairs = [lec_login, lec_password]
            self.lecturers.append(pairs) # appending the list of (log,pass) to the list of the lecturers

        else: # if the list isn't empty
            flag = True
            pairs = [lec_login, lec_password] # creating a new pair (list)
            for pairs_review in self.lecturers: # iterating through the list of lecturers
                if pairs == pairs_review: # if match have been found
                    print('log and password already exists')

            self.lecturers.append(pairs) # if match haven't been found, add the new pair into the list of lecturers

    def delete_lecturer(self,lec_login, lec_password): # this function deleting a lecturer from the lecturer list
        if len(self.lecturers) == 0:  # case 1 - the list is empty
            print("could't find match")

        else: # if the list isn't empty
            pairs = [lec_login, lec_password] # put the arguments in a list (log,pass)
            index = 0
            for pairs_review in self.lecturers: # loop through the list
                if pairs == pairs_review: # if match have been found
                    self.lecturers.pop(index) # remove the inner list (pop)
                    print('Mission accomplished')
                index = index + 1
            print("could't find match") # if the code came down here - means it didn't found any match

    def change_log_or_pass(self,lec_login, lec_password): # this method changes the log/pass to a new one
        if len(self.lecturers) == 0:  # case 1 - the list is empty
            print("could't find match")

        else: # if the list isn't empty
            pairs = [lec_login, lec_password] # put the arguments in a list (log,pass)
            index = 0
            for pairs_review in self.lecturers: # loop through the list
                if pairs == pairs_review: # if match have been found
                    option = input('select the appropriate option: \n 1. login - press 1\n2. password - press 2 \n 3. both - press 3 ')
                    if option == '1':
                        new_login = input('please enter new login')
                        self.lecturers[index][0] = new_login

                    if option == '2':
                        new_password = input('please enter new password')
                        self.lecturers[index][1] = new_password

                    if option == '3':
                        new_login = input('please enter new login')
                        new_password = input('please enter new password')
                        new = [new_login, new_password]
                        self.lecturers[index] = new

                    index = index + 1

    def print_lecturer(self, index): # this method printing a specific item from the list
            if index < 0 and index > len(self.lecturers):
                print('invalid index')
            else:
                print(self.lecturers[index])

    def print_lecturers(self):
        for pairs in self.lecturers:
            print(pairs)





john = Management()
john.insert('dave', '123')
john.print_lecturers()
john.delete_lecturer('dave', '123')
john.print_lecturers()






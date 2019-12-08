class Subjects:

    def __init__(self):
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        while subject in self.subjects:
            to_remove = self.subjects.index(subject)
            del self.subjects[to_remove]

    def add_sub_subject(self, sub_subj):
        print("Which subject to add this to ?")
        subject = input()
        if subject in self.subjects:
            where_to = self.subjects.index(subject)
            self.subjects[where_to].append(sub_subj)
        else:
            self.subjects.append(sub_subj)

    def remove_sub_subject(self, sub_subj):
        while sub_subj in self.subjects:
            to_remove = self.subjects.index(sub_subj)
            del self.subjects[to_remove]

    def add_to_subject(self, subject, question):
        if subject in self.subjects:
            where_to = self.subjects.index(subject)
            self.subjects[where_to].append(question)
        else:
            self.subjects.append(subject)
            self.subjects[subject].append(question)

    def add_to_sub_subject(self,subject, sub_subj, question):
        if subject in self.subjects:
            to_subj = self.subjects.index(subject)
            if sub_subj in self.subjects[to_subj]:
                where_to = self.subjects[to_subj].index(sub_subj)
                self.subjects[to_subj][where_to].append(question)
            else:
                self.add_sub_subject(sub_subj)



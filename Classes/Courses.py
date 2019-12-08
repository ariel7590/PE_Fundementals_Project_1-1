class Course:
    def Course(self):
        courseList = []

        def getCourse(i):
            return courseList[i]

        def setCourse(i, data):
            courseList[i] = data

        def add(data):
            courseList.append(data)
            print(f"{data} added to courses data base")

        def remove(i):
            print(f"{courseList.pop(i)} removed")

        def view():
            print(courseList)

class Tests:
    def __init__(self, test=0):
        self.exam = None
        self.docx_test = []
        self.pdf_test = []
        self.jpeg_test = []

    def get_docx_test(self, index):
        if 0 <= index < len(self.docx_test):
            return self.docx_test[index]
        else:
            return 'invalid index'

    def get_pdf_test(self, index):
        if 0 <= index < len(self.exam):
            return self.pdf_test[index]
        else:
            return 'invalid index'

    def get_jpeg_test(self, index):
        if 0 <= index < len(self.exam):
            return self.jpeg_test[index]
        else:
            return 'invalid index'

    def set_test_with_index(self, data, index):
        if 0 < index < len(self.exam):
            self.exam.insert(index, data)
            print(f"{data} added to tests data base")
        else:
            return 'invalid index'

    def add_element(self, data):
        self.exam.append(data)
        print(f"{data} added to tests data base")

    def remove(self, index):
        if 0 < index < len(self.exam):
            print("element successfully removed")

    def remove_all(self):
        self.exam.clear()
        print("element successfully removed")

    def print_list(self):
        print(self.exam)

    def print_element_in_list(self, index):
        if 0 < index < len(self.exam):
            print(self.exam[index])








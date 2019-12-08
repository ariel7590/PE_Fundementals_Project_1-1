

class Files:
    def _init_(self):

        self.docx_files = []
        self.pdf_files = []
        self.jpeg_files = []

    def add_docx_file(self): # adding new docx element to the list.
        file_name = input('please enter the name of the file')
        file_format = 'docx'
        file_name = file_name + '.' + file_format
        my_file = open(file_name, mode="r")
        self.docx_files.append(my_file)
        my_file.close()

    def add_pdf_file(self):  # adding new pdf element to the list.
        file_name = input('please enter the name of the file')
        file_format = 'pdf'
        file_name = file_name + '.' + file_format
        my_file = open(file_name, mode="r")
        self.pdf_files.append(my_file)
        my_file.close()

    def add_jpeg_file(self):  # adding new jpeg element to the list.
        file_name = input('please enter the name of the file')
        file_format = 'jpeg'
        file_name = file_name + '.' + file_format
        my_file = open(file_name, mode="rb")
        self.jpeg_files.append(my_file)
        my_file.close()

    def clear_list(self, list_format):
        if list_format == 'docx':
            self.docx_files.clear()

        elif list_format == 'pdf':
            self.pdf_files.clear()

        else:
            self.jpeg_files.clear()

    def remove_index(self, index, list_format):
        if list_format == 'docx':
            self.docx_files.pop(index)

        elif list_format == 'pdf':
            self.pdf_files.pop(index)

        else:
            self.jpeg_files.pop(index)

    def remove_all_lists(self): # removind all the elements from each list
        key = input('are you sure to delete all your lists?')
        if key == 'yes':
            self.docx_files.clear()
            self.docx_files.clear()
            self.docx_files.clear()

    def get_list_by_format(self, list_format): # returning the list via format
        if list_format == 'docx':
            return self.docx_files

        elif list_format == 'pdf':
            return self.pdf_files.pop

        else:
            return self.jpeg_files.pop

    def get_list_with_index(self, list_format, index): # get a specific element from a specific list.
        if index < 0 and index > len(self.docx_files) or index > len(self.pdf_files) or index > len(self.jpeg_files):
            return 'invalid index'

        if list_format == 'docx':
            return self.docx_file[index]

        elif list_format == 'pdf':
            return self.pdf_files[index]

        else:
            return self.jpeg_files[index]




















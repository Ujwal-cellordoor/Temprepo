class DataEditing:

    def __init__(self, file_name):
        self.file_name = file_name

    def store(self, w):
        f = open(self.file_name, "a")
        # w = input("What do you want to store? >>")

        f.write(w + '\n')
        print("Content has been stored..")

    def read(self):
        f = open(self.file_name, "r")
        file_read = f.read()
        return file_read

    def deleteItem(self, content_to_delete):

        f = open(self.file_name, "r")
        lines = f.readlines()

        f = open("hello.txt", "w")
        for line in lines:
            if content_to_delete not in line:
                f.write(line)
        f.close()


key = int(input("key: "))

dataEditingObj = DataEditing("hello.txt")

if key == 1:
    w = input("What do you want to store? >>")
    dataEditingObj.store(w)
elif key == 2:
    read_file = dataEditingObj.read()
    print(read_file)
elif key == 3:
    deleted = dataEditingObj.deleteItem("KIWI")
    print(deleted)

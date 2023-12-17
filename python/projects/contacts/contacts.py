class ContactManager:
    def __init__(self, file_of_contacts):
        self.file_of_contacts = file_of_contacts
        self.count = 0
        self.list_of_contacts = []

    def addContact(self, name, phon_number, email):
        self.count += 1
        with open("contacts.txt", "a", encoding="utf-8") as self.file_of_contacts:
            self.file_of_contacts.write(name + "\n")
            self.file_of_contacts.write(phon_number + "\n")
            self.file_of_contacts.write(email + "\n\n")
        with open("contacts.txt", "r", encoding="utf-8") as self.file_of_contacts:
            for i in range(self.count):
                list_of_contact = []
                for j in range(3):
                    list_of_contact.append(self.file_of_contacts.readline())
                self.list_of_contacts.append(list_of_contact)



    def readContactsList(self):
        self.file_of_contacts = open("contacts.txt", "r", encoding="utf-8")
        print(self.file_of_contacts.read())
        self.file_of_contacts.close()

    def searchContact(self, name):
        flag = 0
        for i in range(self.count):
            if name == self.list_of_contacts[i][0][:-1]:
                print("This man is exist in this notebook ")
                print(self.list_of_contacts[i][0] + self.list_of_contacts[i][1] + self.list_of_contacts[i][2])
                flag = 1
                break
        if flag == 0:
            print("This man isn't exist in the notebook")

    def updateInformation(self, name, phon_number, email):
        flag = 0
        for i in range(self.count):
            if self.list_of_contacts[i][0][:-1] == name:
                self.list_of_contacts[i][1] = phon_number + "\n"
                self.list_of_contacts[i][2] = email + "\n"
                flag = 1
                break
        if flag == 0:
            print("Sorry but the contact hase didn't found")
        else:
            with open("contacts.txt", "w", encoding="utf-8") as self.file_of_contacts:
                for item in self.list_of_contacts:
                    self.file_of_contacts.write(item[0] + item[1] + item[2])





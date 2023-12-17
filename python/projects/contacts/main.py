from contacts import ContactManager
file_of_contacts = open("contacts.txt", "w", encoding="utf-8")
file_of_contacts.close()
contact = ContactManager(file_of_contacts)
contact.addContact("avi", "055446677", "email.gmail.com")
contact.readContactsList()
contact.searchContact("avi")
contact.updateInformation("avi", "05678910", "12345.gmail")
contact.readContactsList()

class Contact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower()]
        return results

    def display_contacts(self):
        print("Contact List:")
        for contact in self.contacts:
            print(f"{contact.name} - Email: {contact.email}, Phone: {contact.phone_number}")

# Example usage:
contact1 = Contact("John Doe", "john@example.com", "123-456-7890")
contact2 = Contact("Alice Smith", "alice@example.com", "987-654-3210")
contact_list = ContactList()

contact_list.add_contact(contact1)
contact_list.add_contact(contact2)
contact_list.display_contacts()

search_results = contact_list.search_contact("john")
print("Search Results:")
for result in search_results:
    print(f"{result.name} - Email: {result.email}, Phone: {result.phone_number}")

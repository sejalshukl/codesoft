class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not results:
            print("No contacts found.")
            return
        for contact in results:
            print(contact)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found. Enter new details.")
                contact.name = input("Enter new name: ").strip()
                contact.phone = input("Enter new phone number: ").strip()
                contact.email = input("Enter new email: ").strip()
                contact.address = input("Enter new address: ").strip()
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ").strip()
            contact_book.search_contact(keyword)
        
        elif choice == '4':
            name = input("Enter the name of the contact to update: ").strip()
            contact_book.update_contact(name)
        
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ").strip()
            contact_book.delete_contact(name)
        
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

      
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        
        self.contact_listbox = tk.Listbox(root, width=40)
        self.contact_listbox.grid(row=6, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
            self.view_contacts()
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone number")

    def update_contact(self):
        selected_contact = self.contact_listbox.get(tk.ACTIVE)
        if selected_contact:
            name = selected_contact.split(":")[0].strip()
            if name in self.contacts:
                new_phone = self.phone_entry.get()
                if new_phone:
                    self.contacts[name] = new_phone
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    self.clear_entries()
                    self.view_contacts()
                else:
                    messagebox.showwarning("Warning", "Please enter a new phone number")
            else:
                messagebox.showwarning("Warning", "Contact not found")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update")

    def delete_contact(self):
        selected_contact = self.contact_listbox.get(tk.ACTIVE)
        if selected_contact:
            name = selected_contact.split(":")[0].strip()
            if name in self.contacts:
                del self.contacts[name]
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.view_contacts()
            else:
                messagebox.showwarning("Warning", "Contact not found")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name}: {phone}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

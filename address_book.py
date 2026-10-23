"""A simple address book with search, CSV export, and JSON backups."""

import csv
import hashlib
import json
import re

contacts = {}


def add_contact(full_name, phone, email="", city="Unknown"):
    """Add a contact after validating the phone number."""
    if not re.fullmatch(r"[0-9]{10}", phone):
        print("Invalid phone number for", full_name)
        return False

    contacts[full_name] = {
        "phone": phone,
        "email": email,
        "city": city,
    }
    return True


def contact_id(full_name):
    """Generate a stable contact identifier using SHA-256."""
    return hashlib.sha256(full_name.encode("utf-8")).hexdigest()[:12]


def search_contacts(text):
    """Find contacts by partial name or phone number."""
    found = []
    for name, info in contacts.items():
        if text.lower() in name.lower() or text in info["phone"]:
            found.append(name)
    return found


def update_city(full_name, city):
    """Update a contact's city if the contact exists."""
    try:
        contacts[full_name]["city"] = city
    except KeyError:
        print("No contact named", full_name)
        return False
    return True


def contacts_by_city():
    """Group contact names by city."""
    grouped = {}
    for name, info in contacts.items():
        grouped.setdefault(info["city"], []).append(name)
    return grouped


def print_directory():
    """Print all contacts in alphabetical order."""
    names = sorted(contacts)
    for index, name in enumerate(names, start=1):
        print(index, name, contacts[name]["phone"])


def export_csv(file_name="contacts.csv"):
    """Export contacts to a UTF-8 CSV file."""
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for name, info in contacts.items():
            writer.writerow([
                name,
                info["phone"],
                info["email"],
                info["city"],
            ])


def backup_book(file_name="contacts.json"):
    """Save contacts as JSON instead of using unsafe pickle."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)


def restore_book(file_name="contacts.json"):
    """Restore contacts from a JSON backup."""
    with open(file_name, "r", encoding="utf-8") as file:
        restored = json.load(file)

    if not isinstance(restored, dict):
        raise ValueError("Invalid backup: expected a contact dictionary.")

    for name, info in restored.items():
        if not isinstance(name, str) or not isinstance(info, dict):
            raise ValueError("Invalid backup: malformed contact entry.")
        if not all(
            isinstance(info.get(field), str)
            for field in ("phone", "email", "city")
        ):
            raise ValueError("Invalid backup: malformed contact details.")

    return restored


def main():
    """Demonstrate the address book features."""
    add_contact(
        "Neha Sharma", "9876543210", "neha@example.com", "Bengaluru"
    )
    add_contact(
        "Rahul Verma", "9123456780", "rahul@example.com", "Mysuru"
    )
    add_contact("Test User", "12345")
    add_contact("Kavya Nair", "9988776655", city="Bengaluru")

    update_city("Rahul Verma", "Chennai")
    update_city("Nobody", "Delhi")

    print_directory()
    print("Search 'ra':", search_contacts("ra"))
    print("By city:", contacts_by_city())
    print("ID for Neha:", contact_id("Neha Sharma"))

    export_csv()
    backup_book()
    restored = restore_book()

    first_contact = sorted(restored)[0] if restored else "None"
    print(
        "Contacts restored:",
        len(restored),
        "| first:",
        first_contact,
    )
    print(
        "Restored contacts match the in-memory address book:",
        restored == contacts,
    )


if __name__ == "__main__":
    main()

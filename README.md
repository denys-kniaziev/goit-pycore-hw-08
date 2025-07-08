# Woolf University. Python Programing Course. Homework – Serialization in Python

## Overview

Extend your AddressBook application to persist data between sessions using Python's `pickle` module. Ensure the address book is saved to disk on exit and restored on startup.

---

## Requirements

1. **Serialization Functions**

   * In a module (e.g., `storage.py`), implement:

     * **save\_data(book, filename)**: serializes the given AddressBook instance to the specified file using the pickle protocol.

     * **load\_data(filename)**: deserializes and returns an AddressBook instance from the specified file; if the file is missing or cannot be unpickled, returns a new, empty AddressBook.

2. **Integration in `main()`**

   * At startup, initialize the address book with:

     ```python
     from storage import load_data, save_data

     def main():
         book = load_data()
         # REPL loop here…
         save_data(book)
     ```
   * Ensure `save_data(book)` is called on program exit, even after exceptions.

3. **Persistence Behavior**

   * Contacts, phone numbers, birthdays, and any other fields must be retained across runs.
   * If the pickle file is missing or corrupted, the application starts with an empty address book without crashing.

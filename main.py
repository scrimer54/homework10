from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        if not self.value.isdigit() or len(self.value) != 10:
            raise ValueError("Invalid phone number format. Phone number must contain 10 digits.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone.value not in [p.value for p in self.phones]:
            raise ValueError("Phone number to be removed does not exist.")
        self.phones = [p for p in self.phones if p.value != phone.value]

    def edit_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        for phone in self.phones:
            if phone.value == old_phone.value:
                phone.value = new_phone.value
                return f"Phone number {old_phone.value} edited to {new_phone.value}"

        raise ValueError("Phone number to be edited does not exist.")

    def find_phone(self, phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                return p.value
            
        


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")
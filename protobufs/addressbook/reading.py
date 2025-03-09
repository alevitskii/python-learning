#!/usr/bin/env python3

import sys

import addressbook_pb2


# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(address_book: addressbook_pb2.AddressBook) -> None:
    for person in address_book.people:
        print("Person ID:", person.id)
        print("  Name:", person.name)
        if person.HasField("email"):
            print("  E-mail address:", person.email)

        for phone_number in person.phones:
            if phone_number.type == addressbook_pb2.Person.PhoneType.PHONE_TYPE_MOBILE:
                print("  Mobile phone #: ", end="")
            elif phone_number.type == addressbook_pb2.Person.PhoneType.PHONE_TYPE_HOME:
                print("  Home phone #: ", end="")
            elif phone_number.type == addressbook_pb2.Person.PhoneType.PHONE_TYPE_WORK:
                print("  Work phone #: ", end="")
            print(phone_number.number)


# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
with open(sys.argv[1], "rb") as f:
    address_book.ParseFromString(f.read())

ListPeople(address_book)

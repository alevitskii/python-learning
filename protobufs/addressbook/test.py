# protoc --proto_path=protobufs/addressbook/proto --python_out=protobufs/addressbook --pyi_out=protobufs/addressbook .\protobufs\addressbook\proto\addressbook.proto

import addressbook_pb2

person = addressbook_pb2.Person()
print(person.id)
person.id = 1234
print(person.name)
person.name = "John Doe"
print(person.name)
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

print(addressbook_pb2.Person.PhoneType.PHONE_TYPE_MOBILE)

print(person)

b = person.SerializeToString()
person2 = addressbook_pb2.Person()
person2.ParseFromString(b)
print(person2)

try:
    person.no_such_field = 1
except AttributeError as e:
    print(f"raised {e}")

try:
    person.id = "1234"  # type: ignore
except TypeError as e:
    print(f"raised {e}")

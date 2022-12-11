import uuid
name=input("Enter Name: ")
str(name)
surname=input("Enter Surname: ")
str(surname)
print(f"ID:{name[0:2]}{surname[0:2]}{str(uuid.uuid4())[0:5]}")
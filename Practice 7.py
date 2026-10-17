forname = input("Enter forname: ")
surname = input("Enter surname: ")
initials = f"{forname[0]}.{surname[0]}."
name = f"{forname} {surname}"
username = f"{forname[0:3]}{surname[0:3]}"
print(f"Name:   {name}")
print(f"Initials:   {initials}")
print(f"Length of name: {len(name)}")
print(f"Username:   {username}")
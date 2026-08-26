data = [1, 2, 3, 4, 5, 6 ,7]
choice = int(input("Enter the number you want to search for"))

for i in data:
    if choice == i:
        print(f"Data found. Index {data.index(choice)}")
        
else:
    print("Data not found.")
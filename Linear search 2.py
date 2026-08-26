data = [1, 2, 3, 4, 5, 6 ,7]
choice = int(input("Enter the number you want to search for"))

for i in range(len(data)):
    if choice == data[i]:
        print(f"Data found. Index {data.index(choice)}")
        break
        
else:
    print("Data not found.")
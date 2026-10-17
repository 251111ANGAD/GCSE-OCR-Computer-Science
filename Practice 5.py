day = int(input("Enter the day of the week:\n1. Monday\n2. Tuesday\n3. Wednesday\n...\n7. Sunday\n"))
if day == 6 or day == 7:
    print("Its the weekend!")
else:
    print("Keep on working.")

# Databricks program
vacancies = 5

applicants = int(input("Please enter your application number: "))

i = 0

while i<=applicants:
    if i>=vacancies:
        print("We are out of positions")
        break

    print("You have applied for the enrolment")
    i+=1


print("Finished the application process")






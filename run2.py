from datetime import datetime


def main():
    CurrentDate = datetime.now()
    print(CurrentDate)

    #ExpectedDate = "09/08/2015"
    ExpectedDate = str(input("Enter the date:"))
    ExpectedDate = datetime.strptime(ExpectedDate, "%d-%m-%Y")

    print(type(ExpectedDate))
    print(type(CurrentDate))

    if CurrentDate > ExpectedDate:
        print("Date missed")
    else:
        print("Date not missed")


main()

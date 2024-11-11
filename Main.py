from datetime import datetime

def calculate_fine(days_overdue):
    if days_overdue <= 7:
        return days_overdue * 20
    elif 8 <= days_overdue <= 14:
        return days_overdue * 50
    else:
        return days_overdue * 100

def main():
    bookID = input("Enter Book ID: ")
    dueDate = input("Enter Due Date (YYYY-MM-DD): ")
    returnDate = input("Enter Return Date (YYYY-MM-DD): ")

    dueDate = datetime.strptime(dueDate, "%Y-%m-%d")
    returnDate = datetime.strptime(returnDate, "%Y-%m-%d")

    days_overdue = (returnDate - dueDate).days

    if days_overdue > 0:
        fine_amount = calculate_fine(days_overdue)
        if days_overdue <= 7:
            fine_rate = 20
        elif 8 <= days_overdue <= 14:
            fine_rate = 50
        else:
            fine_rate = 100
    else:
        days_overdue = 0
        fine_amount = 0
        fine_rate = 0

    print(f"Book ID: {bookID}")
    print(f"Due Date: {dueDate.strftime('%Y-%m-%d')}")
    print(f"Return Date: {returnDate.strftime('%Y-%m-%d')}")
    print(f"Days Overdue: {days_overdue}")
    print(f"Fine Rate: Ksh. {fine_rate} per day")
    print(f"Fine Amount: Ksh. {fine_amount}")

if __name__ == "__main__":
    main()

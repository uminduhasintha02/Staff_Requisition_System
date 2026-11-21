from requisition import Requisition


requisitions = []


def create_sample_requisitions():
    sample1 = Requisition("S001", "John Smith")
    sample1.add_requisition([
        ("Keyboard", 100),
        ("Mouse", 50),
        ("Monitor", 150)
    ])
    requisitions.append(sample1)

    sample2 = Requisition("S002", "Sarah Jones")
    sample2.add_requisition([
    ("Office Chair", 300),
    ("Desk", 100)
])
    requisitions.append(sample2)

    sample3 = Requisition("S003", "David Brown")
    sample3.add_requisition([
        ("Laptop", 1200)
    ])
    sample3.respond_requisition("r")
    requisitions.append(sample3)

    sample4 = Requisition("S004", "Emma Wilson")
    sample4.add_requisition([
        ("Printer", 250),
        ("Paper", 100)
    ])
    requisitions.append(sample4)

    sample5 = Requisition("S005", "Michael Lee")
    sample5.add_requisition([
        ("Computer", 900)
    ])
    requisitions.append(sample5)


def add_new_requisition():
    print("\n========== NEW REQUISITION ==========")

    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    requisition = Requisition(staff_id, staff_name)

    items = []

    while True:
        item_name = input("\nEnter Item Name (or type 'done'): ")

        if item_name.lower() == "done":
            break

        if not item_name.strip():
            print("Item name cannot be empty.")
            continue

        try:
            price = float(input("Enter Item Price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

            items.append((item_name, price))

        except ValueError:
            print("Please enter a valid number.")

    try:
        total = requisition.add_requisition(items)

        requisitions.append(requisition)

        print("\nRequisition submitted successfully.")
        print(f"Total Amount: ${total:.2f}")
        print("Status:", requisition.status)

    except ValueError as error:
        print("Error:", error)


def manager_response():
    print("\n========== MANAGER RESPONSE ==========")

    pending_requisitions = [
        r for r in requisitions if r.status == "Pending"
    ]

    if not pending_requisitions:
        print("There are no pending requisitions.")
        return

    for requisition in pending_requisitions:
        print(
            requisition.requisition_id,
            "-",
            requisition.staff_name,
            "-",
            f"${requisition.total:.2f}"
        )

    requisition_id = input("\nEnter Requisition ID: ")

    for requisition in pending_requisitions:

        if requisition.requisition_id == requisition_id:

            print("\n1. Approve")
            print("2. Not Approve")

            decision = input("Enter your decision: ")

            if decision == "1":
                requisition.respond_requisition("a")

            elif decision == "2":
                requisition.respond_requisition("r")

            else:
                print("Invalid selection.")

            return

    print("Requisition ID not found.")


def display_all_requisitions():
    print("\n========== ALL REQUISITIONS ==========")

    if not requisitions:
        print("No requisitions available.")
        return

    for requisition in requisitions:
        requisition.display_requisition()


def display_statistics():
    Requisition.requisition_statistics(requisitions)


def main():

    create_sample_requisitions()

    while True:

        print("\n====================================")
        print(" STAFF REQUISITION MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add New Requisition")
        print("2. Manager Response")
        print("3. Display All Requisitions")
        print("4. Display Statistics")
        print("5. Exit")
        print("====================================")

        choice = input("Select an option: ")

        if choice == "1":
            add_new_requisition()

        elif choice == "2":
            manager_response()

        elif choice == "3":
            display_all_requisitions()

        elif choice == "4":
            display_statistics()

        elif choice == "5":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
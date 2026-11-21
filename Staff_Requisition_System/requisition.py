from datetime import date


class Requisition:

    requisition_count = 1

    def __init__(self, staff_id, staff_name):
        self.date = str(date.today())
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = f"R{Requisition.requisition_count:04d}"
        Requisition.requisition_count += 1

        self.items = []
        self.total = 0
        self.status = "Not Submitted"
        self.approval_reference = None

    def add_requisition(self, items):
        if not items:
            raise ValueError("The item list cannot be empty.")

        self.items = []

        for item_name, price in items:
            if not item_name.strip():
                raise ValueError("Item name cannot be empty.")

            if price < 0:
                raise ValueError("Price cannot be negative.")

            self.items.append((item_name, price))
            self.total += price

        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = "FN02004"
        else:
            self.status = "Pending"

        return self.total

    def respond_requisition(self, decision):
        if self.status != "Pending":
            print("This requisition is not pending.")
            return

        decision = decision.lower()

        if decision == "a":
            self.status = "Approved"
            self.approval_reference = (
                f"FN{self.requisition_id[1:]}"
            )
            print("Requisition approved.")

        elif decision == "r":
            self.status = "Not approved"
            self.approval_reference = None
            print("Requisition not approved.")

        else:
            print("Invalid decision.")

    def display_requisition(self):
        print("\n-----------------------------------")
        print("REQUISITION DETAILS")
        print("-----------------------------------")
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)

        print("\nRequested Items:")

        for item_name, price in self.items:
            print(f"{item_name}: ${price:.2f}")

        print(f"\nTotal: ${self.total:.2f}")
        print("Status:", self.status)
        print("Approval Reference:", self.approval_reference)
        print("-----------------------------------")

    @staticmethod
    def requisition_statistics(requisitions):
        total = len(requisitions)

        approved = sum(
            1 for r in requisitions if r.status == "Approved"
        )

        pending = sum(
            1 for r in requisitions if r.status == "Pending"
        )

        not_approved = sum(
            1 for r in requisitions if r.status == "Not approved"
        )

        print("\n========== STATISTICS ==========")
        print("Total Requisitions:", total)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not Approved:", not_approved)
        print("================================")
class Requisition:

    requisition_counter = 10000
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        Requisition.requisition_counter += 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.requisition_counter

        self.items = []
        self.total = 0.0
        self.status = "Pending"
        self.approval_reference = "Not available"
        Requisition.all_requisitions.append(self)

    def add_requisition(self, items):
        self.items = items
        self.total = 0.0

        for item in self.items:
            self.total += item[1]

        self.approve_requisition()

        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

    def respond_requisition(self, response):
        if self.status != "Pending":
            print("This requisition is not pending.")
            return

        if response.lower() == "approved":
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

        elif response.lower() == "not approved":
            self.status = "Not approved"
            self.approval_reference = "Not available"

        else:
            print("Invalid response. Please try again.")

    def display_requisition(self):
        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Items:", self.items)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)

    @classmethod
    def display_requisitions(cls):
        for requisition in cls.all_requisitions:
            requisition.display_requisition()

    @classmethod
    def requisition_statistics(cls):
        total = len(cls.all_requisitions)

        approved = 0
        pending = 0
        not_approved = 0

        for requisition in cls.all_requisitions:
            if requisition.status == "Approved":
                approved += 1
            elif requisition.status == "Pending":
                pending += 1
            elif requisition.status == "Not approved":
                not_approved += 1
                
        print("\n========== REQUISITION STATISTICS ==========")
        print("Total requisitions submitted:", total)
        print("Total approved requisitions:", approved)
        print("Total pending requisitions:", pending)
        print("Total not approved requisitions:", not_approved)

        return {
            "Total": total,
            "Approved": approved,
            "Pending": pending,
            "Not approved": not_approved
        }
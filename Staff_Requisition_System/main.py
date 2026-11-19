
from requisition import Requisition


requisition1 = Requisition("17/11/2026", "FN19", "John Paul")
requisition1.add_requisition([
    ["Keyboard", 150],
    ["Mouse", 100],
    ["USB Cable", 200]
])

requisition2 = Requisition("17/11/2026", "FN20", "Tracy Brown")
requisition2.add_requisition([
    ["Monitor", 450],
    ["Keyboard", 300]
])

requisition3 = Requisition("17/11/2026", "FN15", "Emma Wellington")
requisition3.add_requisition([
    ["Laptop", 1000],
    ["Mouse", 200]
])

requisition4 = Requisition("17/11/2026", "FN02", "Catlin White")
requisition4.add_requisition([
    ["Headphones", 150],
    ["Keyboard", 150]
])

requisition5 = Requisition("17/11/2026", "FN25", "David Smith")
requisition5.add_requisition([
    ["Printer", 600],
    ["Paper", 300]
])


print("\n========== INITIAL REQUISITIONS ==========")

Requisition.display_requisitions()

Requisition.requisition_statistics()


print("\n========== MANAGER RESPONSES ==========")

requisition2.respond_requisition("approved")
print("Requisition 2 has been approved.")

requisition3.respond_requisition("not approved")
print("Requisition 3 has not been approved.")


print("\n========== UPDATED REQUISITIONS ==========")

Requisition.display_requisitions()

Requisition.requisition_statistics()

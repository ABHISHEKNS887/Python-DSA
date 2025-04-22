# Floyd's cycle-finding algorithm

# 📌 Purpose:
# To detect if a cycle exists in a sequence (e.g., a linked list), and optionally find the start of the cycle.

# 🧠 How it works:
# You use two pointers:

# 🐢 Slow pointer (tortoise): moves one step at a time

# 🐇 Fast pointer (hare): moves two steps at a time

# If there’s a cycle, the fast pointer will eventually meet the slow pointer inside the cycle.
# If there’s no cycle, the fast pointer will reach the end (None).

# 🔁 Steps:
# Initialize both pointers at the head.

# Move slow by 1, fast by 2.

# If they meet → cycle detected.

# To find cycle start:

# Move one pointer to the head again.

# Move both by 1 step now.

# Where they meet is the start of the cycle.

# ✅ Example:
# Let’s say you have a linked list:

# 1 → 2 → 3 → 4 → 5
#          ↑     ↓
#          ← ← ←
# Node 5 points back to node 3 (cycle starts at 3).

# 💻 Python Implementation:

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def detect_cycle(head):
    slow = fast = head

    # Step 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Step 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Start node of the cycle

# 🧪 Test:

# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Create cycle: 1→2→3→4→5→3...
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3

start = detect_cycle(n1)
print("Cycle starts at:", start.val if start else "No cycle")
# 🟢 Output:

# Cycle starts at: 3

# ⏱️ Time & Space Complexity:
# Time: O(n)

# Space: O(1) ← key advantage!
def loop_size(node):
    slow = node
    fast = node
    # Move until they meet
    while fast and fast.next:
        slow = slow.next  # Move 1 step
        fast = fast.next.next  # Move 2 steps

        if slow == fast:
            # They met, Now count loop size
            break

    # Count loop size
    count = 1
    slow = slow.next  # Move slow one step

    while slow != fast:  # Until they meet again
        slow = slow.next
        count += 1

    return count

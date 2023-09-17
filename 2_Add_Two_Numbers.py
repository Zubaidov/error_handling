class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()  # Create a dummy node to simplify the code
        current = dummy

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

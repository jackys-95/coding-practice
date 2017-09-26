class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current_result = result
        result_last_node = None
        l1_current = l1
        l2_current = l2
        l1_len = 0
        l1_last_node = None
        l2_last_node = None
        l2_len = 0
        carry = False
        while l1_current is not None and l2_current is not None:
            arg1 = l1_current.val
            arg2 = l2_current.val
            current_sum = arg1 + arg2 + 1 if carry else arg1 + arg2
            carry = True if current_sum >= 10 else False
            current_result.val = current_sum % 10
            current_result.next = ListNode(0)
            l1_last_node = l1_current
            l1_current = l1_current.next
            l2_last_node = l2_current
            l2_current = l2_current.next
            result_last_node = current_result
            current_result = current_result.next
            l1_len += 1
            l2_len += 1
        result_last_node.next = None
        # handle case where len(l1) != len(l2)
        if l1_last_node.next is not None:
            l1_len += 1
        if l2_last_node.next is not None:
            l2_len += 1
        if l1_len > l2_len:
            result_last_node.next = l1_last_node.next
        elif l2_len > l1_len:
            result_last_node.next = l2_last_node.next

        # handle the case where there is still carry, propogate the carry
        if carry and l1_len != l2_len:
            current_result = result_last_node.next
            while current_result is not None and carry:
                print(current_result.val)
                current_sum = current_result.val + 1
                carry = True if current_sum >= 10 else False
                current_result.val = current_sum % 10
                result_last_node = current_result
                current_result = current_result.next
        if carry:
            result_last_node.next = ListNode(1)
        return result

l1 = ListNode(9)
l1.next = ListNode(9)
l2 = ListNode(1)

sol = Solution()
l3 = sol.addTwoNumbers(l2, l1)
print(l3.val)
print(l3.next.val)
print(l3.next.next)

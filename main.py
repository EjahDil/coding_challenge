from lead_code import LeadCode

if __name__ == "__main__":
    
    lead_obj = LeadCode()

    l1 = lead_obj.ListNode(2, lead_obj.ListNode(4, lead_obj.ListNode(3)))
    l2 = lead_obj.ListNode(5, lead_obj.ListNode(6, lead_obj.ListNode(4)))

    result = lead_obj.addTwoNumbers(l1, l2)

    def linked_list_to_list(node):
        result_list = []
        while node:
            result_list.append(node.val)
            node = node.next
        return result_list

    output = linked_list_to_list(result)
    print(output)

    
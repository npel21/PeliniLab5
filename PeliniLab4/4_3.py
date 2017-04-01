# Problem 3
func_list = ["strcpy", "sprintf", "strncpy", "wcsncpy", "swprintf"]

# For each of the segments
for seg in Segments():
    # For each of the defined elements
    for head in Heads(seg, SegEnd(seg)):
        # If it's an instruction
        if isCode(GetFlags(head)):
            # Get the mnemonic and increment the count
            mnem = GetMnem(head)
            # Check if a function is called
            if mnem == 'call':
                # Retrieve function name
                func_name = GetFunctionName(head)
                # Get operand of an instruction
                Opnd = GetOpnd(head, 0)
                for func_call in func_list:
                    if Opnd.find(func_call):
                        func_addr = hex(head)
                        print func_name, ':', func_addr, ':', func_call
from sets import Set

# Problem 3

for i in range(GetEntryPointQty()): # Retrieve number of entry points
    ord = GetEntryOrdinal(i)    # Retrieve entry point ordinal number
    if ord == 0:    # 0 if entry point doesn't exist otherwise entry point ordinal
        continue
    addr = GetEntryPoint(ord)   # Retrieve entry point address
    #print("Export[%s]:Address[%x]\n" % (GetFunctionName(addr), addr))

# Loop through code refs
for ref_from in CodeRefsFrom(addr, 0): # Get a list of code references from 'ea'
    # Sets caller_name to function being called directly by exported function.
    caller_name = GetFunctionName(ref_from)
    # Print "Name of Exported Function:caller_name" if any of the desired functions are found.
    if caller_name == "strcpy" or  caller_name == "sprintf" or caller_name == "strncpy" or caller_name == "wcsncpy" or caller_name == "swprintf":
        print GetFunctionName(addr), caller_name
    
    
    # First layer
    for layer1 in CodeRefsFrom(ref_from, 0):
        caller_name = GetFunctionName(layer1)
        if caller_name == "strcpy" or  caller_name == "sprintf" or caller_name == "strncpy" or caller_name == "wcsncpy" or caller_name == "swprintf":
            print GetFunctionName(addr), caller_name
        
        
        # Second layer
        for layer2 in CodeRefsFrom(layer1, 0):
            caller_name = GetFunctionName(layer2)
            if caller_name == "strcpy" or  caller_name == "sprintf" or caller_name == "strncpy" or caller_name == "wcsncpy" or caller_name == "swprintf":
                print GetFunctionName(addr), caller_name
            
            
            # Third layer
            for layer3 in CodeRefsFrom(layer2, 0):
                caller_name = GetFunctionName(layer3)
                if caller_name == "strcpy" or  caller_name == "sprintf" or caller_name == "strncpy" or caller_name == "wcsncpy" or caller_name == "swprintf":
                    print GetFunctionName(addr), caller_name
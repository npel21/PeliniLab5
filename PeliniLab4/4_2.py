# Problem 2
ea = ScreenEA()

# Loop through all the functions
for f in Functions(SegStart(ea), SegEnd(ea)):
    
    # Get the name of the function being called
    f_name = GetFunctionName(f)
    
    # For each of the incoming references
    for ref in CodeRefsTo(f, 0):    # Get a list of code references to 'ea'
       
        # Name of the function
        caller_name = GetFunctionName(ref)
        # Address that makes the call
        caller_addr = GetFunctionAttr(ref, FUNCATTR_START)  # Get a function attribute
        print caller_name, hex(caller_addr), f_name
        
        # Function called so print info
        if f_name == "strcpy" or f_name == "sprintf" or f_name == "strncpy" or f_name == "wcsncpy" or f_name == "swprintf":
            print caller_name, hex(caller_addr), f_name

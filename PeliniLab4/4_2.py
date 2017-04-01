# Problem 2

func_list = ["strcpy", "sprintf", "strncpy", "wcsncpy", "swprintf"]

for spec_func in func_list:
    spec_addr = LocByName(spec_func)
    if spec_addr == BADADDR:
        print spec_func, "not found"
    else:
        # Supposed to retrieve function name from linear address, doesn't seem to work
        spec_name = GetFunctionName(spec_addr)
        spec_addr = hex(spec_addr)
        print spec_name, ":", spec_addr, ":", spec_func
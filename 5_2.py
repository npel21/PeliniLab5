#---------------------------------------------------------------------
# Debug notification hook test
#
# This script start the executable and steps through the first five
# instructions. Each instruction is disassembled after execution.
#
# Author: Gergely Erdelyi <dyce@d-dome.net>
#---------------------------------------------------------------------

'''
Write a script that defines a DBG_Hooks object. The script should be capable to be run
against CrackME2.exe to change its functionality such that any password is correct except
the correct password. The script must implement at least one breakpoint and must print
out the entered password.
'''

from idaapi import *

class MyDbgHook(DBG_Hooks):
    """ Own debug hook class that implementd the callback functions """

    def dbg_process_start(self, pid, tid, ea, name, base, size):
        print "Process started, pid=%d tid=%d name=%s" % (pid, tid, name)
        return 0

    def dbg_process_exit(self, pid, tid, ea, code):
        print "Process exited pid=%d tid=%d ea=0x%x code=%d" % (pid, tid, ea, code)
        return 0

    def dbg_library_load(self, pid, tid, ea, name, base, size):
        print "Library loaded: pid=%d tid=%d name=%s base=%x" % (pid, tid, name, base)

    # Change CRACKME2 functionality
    def dbg_bpt(self, tid, ea):
        print "Breakpoint: 0x%x pid=%d" % (ea, tid)
        # Print out entered password
        if ea == 0x00401370:
            esi = GetRegValue("esi")
            print "Password was %X\n" % (Dword(esi))
        # Check registers
        if ea == 0x0040123C:
            check_reg = GetRegValue("cl")
            if check_reg == 0:
                reg_value = idaapi.regval_t()
                reg_value.ival = 1
                idaapi.set_reg_val("cl", reg_value)
            else:
                reg_value = idaapi.regval_t()
                reg_value.ival = 0
                idaapi.set_reg_val("cl", reg_value)
        return 0

    def dbg_trace(self, tid, ea):
        print tid, ea
        return 0

    def dbg_step_into(self):
        print "Step into"
        return self.dbg_step_over()

    def dbg_step_over(self):
        eip = GetRegValue("EIP")
        print "0x%x %s" % (eip, GetDisasm(eip))

        self.steps += 1
        if self.steps >= 5:
            request_exit_process()
        else:
            request_step_over()
        return 0

# Remove an existing debug hook
try:
    if debughook:
        print "Removing previous hook ..."
        debughook.unhook()
except:
    pass

# Install the debug hook
debughook = MyDbgHook()
debughook.hook()
debughook.steps = 0

# Add in breakpoints
AddBpt (0x401228)
AddBpt (0x40123F)

# Stop at the entry point
ep = GetLongPrm(INF_START_IP)
request_run_to(ep)

# Step one instruction
request_step_over()

# Start debugging
run_requests()

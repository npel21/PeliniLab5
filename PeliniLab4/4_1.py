# Problem 1
md5_constants = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee]

# For each of the segments
for seg in Segments():
    # For each of the defined elements
    for head in Heads(seg, SegEnd(seg)):
        if isData(head):
            hex_head = hex(head)
            for md5 in md5_constants:
                if hex_head == md5:
                    print md5
                    if md5 in md5_constants:    # Make sure exists in list
                        md5_constants.remove(md5)

if not md5_constants:   # If list is empty, all four md5s were found
    print "MD5 Constants present"

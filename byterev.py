# -*- coding: utf-8 -*-
#
# Python 2.7.1
#

from bitstring import BitArray

fname = 'image.jpg'

with open(fname, 'r+b') as fh:
    byte_map = [ord(b) for b in fh.read(4)]
    byte_list = [byte_map[0], byte_map[1], byte_map[2], byte_map[3]]
    print 'retrieved', len(byte_list), 'from file', fname
    offset = 0
    for ascii_val in byte_list:
        bin_val = BitArray(hex(ascii_val))
        print bin_val.bin
        BitArray.reverse(bin_val)
        print bin_val.bin
        fh.seek(offset)
        bin_val.tofile(fh)
        print 'writing offset', offset, 'of file', fname
        offset += 1

fh.close()

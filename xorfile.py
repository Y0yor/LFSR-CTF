def xorfile(file1, file2):
    file1b = bytearray(open(file1, 'rb').read())
    file2b = bytearray(open(file2, 'rb').read())
    # Get the largest file size
    size = len(file1b) if len(file1b) < len(file2b) else len(file2b)
    xor_tab = bytearray(size)
    # Xor each bit between two files
    for i in range(size):
        xor_tab[i] = file1b[i] ^ file2b[i]
    return xor_tab

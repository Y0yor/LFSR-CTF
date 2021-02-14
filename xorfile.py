def xorfile(file1, file2):
    file1b = bytearray(open(file1, 'rb').read())
    file2b = bytearray(open(file2, 'rb').read())
    # Récupération de la taille du plus petit fichier
    size = len(file1b) if len(file1b) < len(file2b) else len(file2b)
    xor_tab = bytearray(size)
    # Boucle pour xorer chaque bit entre les deux fichiers
    for i in range(size):
        xor_tab[i] = file1b[i] ^ file2b[i]
    return xor_tab

from xorfile import xorfile
from berlekampMasseyalgo import berlekamp_Massey_algorithm
import sys
import os


# Get magic number
def getseed(xorf):
    size = 8
    binary = []
    for i in range(size):
        temp = []
        for j in '{:08b}'.format(xorf[i]):
            temp += [int(j)]
        binary += temp
    return binary


# Get polynomia from seed
def getpolynomia(binary):
    size = 8
    print('Polynomia :')
    polynomia = berlekamp_Massey_algorithm(binary[:size*8])
    print(polynomia)
    return polynomia


# Decrypt with polynomia and seed
def decryptage(data, data_chiffre, polynomia, binary, taille):
    clef = []
    nbrdeg = len(polynomia)
    print("Number of degree :")
    print(nbrdeg)
    for i in range(polynomia[nbrdeg-1]):
        clef.append(binary[i])
    print("Seed :")
    print(clef)
    # key generation
    temp = 0
    for i in range(0, taille * 8):
        temp = clef[polynomia[0]+i]
        # (clef[0+i]^clef[5+i]^clef[13+i]^....^clef[n-1+i]) for each
        # degree up to max degree-1
        for j in range(1, nbrdeg-1):
            temp = temp ^ clef[polynomia[j]+i]
        clef.append(temp)
    print("Key size :")
    print(len(clef))
    # Decrypt png file
    index = 0
    for octet in data:
        octet_tmp = 0
        for i in range(8):
            octet_tmp <<= 1
            octet_tmp = octet_tmp | clef[index]
            index += 1
        data_chiffre.write(bytes([octet ^ octet_tmp]))
    data_chiffre.close()
    print("File has been decrypted !")


def lfsr(filename_enc, filename):
    # Xor files
    xorf = xorfile(filename_enc, 'src/sample.png')
    taille = os.path.getsize(filename_enc)
    # Get magic number
    binary = getseed(xorf)
    # Get polynomia
    polynomia = getpolynomia(binary)
    data = open(filename_enc, 'rb').read()
    data_chiffre = open(filename, 'wb')
    decryptage(data, data_chiffre, polynomia, binary, taille)
    return True


if __name__ == "__main__":
    lfsr(sys.argv[1], sys.argv[2])

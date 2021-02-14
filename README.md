# LFSR-CTF
Linear-feedback shift register (LFSR) is a shift register whose input bit is a linear function of its previous state.
The Galois LFSR uses the XOR operation as a linear function.

This scrips is an attack based on an implementation of Galois LFSR algorithm to decrypt .png files.

## How to use
python main.py <encrypted_file> <destination_file>

main.py is compatible with Python 3, but has only been tested against Python 3.7

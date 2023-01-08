# Define the functions used in each round of the algorithm
def F(x, y, z):
    return (x & y) | (~x & z)

def G(x, y, z):
    return (x & z) | (y & ~z)

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)

# Define the shift values for each function
s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
     5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

def program():
    # Initialize variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    
    # Convert input string to a list of bytes
    user_input = input("Please write something: ")
    data = [ord(c) for c in user_input]

    # Pad the data to a multiple of 512 bits
    data += [0x80] + [0] * ((56 - len(data) % 64) % 64)
    data += [len(data) * 8 // (2 ** 32), len(data) * 8 % (2 ** 32)]

    # Divide the data into 512-bit blocks
    blocks = [data[i:i+64] for i in range(0, len(data), 64)]

    # Process each block
    for block in blocks:
        # Initialize variables for this block
        a = h0
        b = h1
        c = h2
        d = h3

        # Perform the four rounds of the algorithm
        for i in range(64):
            if i < 16:
                f = F(b, c, d)
                g = i
            elif i < 32:
                f = G(b, c, d)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = H(b, c, d)
                g = (3 * i + 5) % 16
            else:
                f = I(b, c, d)
                g = (7 * i) % 16
            f = f + a + block[g] + (1 << 32)
            a = d
            d = c
            c = b
            b = (b + ((f << s[i]) | (f >> (32 - s[i])))) % (1 << 32)

        # Update the hash values for this block
        h0 = (h0 + a) % (1 << 32)
        h1 = (h1 + b) % (1 << 32)
        h2 = (h2 + c) % (1 << 32)
        h3 = (h3 + d) % (1 << 32)

    # Concatenate the final hash values and convert to a hex string
    hash_value = hex(h0)[2:] + hex(h1)[2:] + hex(h2)[2:] + hex(h3)[2:]

    # Print the hash value
    print(hash_value)
    program()

program()

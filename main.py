intValue = 3  # An int is the most basic numerical type, an integer

floatValue = -5.7  # A double precision floating point value. 64 bits.
# The first bit is the sign bit, 1 is negative, 0 is positive.
# The next 11 bits are the exponent, and then the significand is formed by 53 bits,
# The first one of those 53 is 1, and the remaining 52 are stored in the number.
# In between them is a decimal point
# The formula for the value then becomes Sign*-1*2^(exponent-1023)*significand

complexValue = complex(3, 4) # A complex number of the format 3 + 4j (For some reason i is called j)

boolValue = True  # A true or false boolean value that can serve as the input between an if, elif, or while statement

stringValue = "IT'S THE END OF THE WORLD AS WE KNOW IT"  # A string is a set of characters

arrayValue = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
for i in arrayValue:
    print(i)
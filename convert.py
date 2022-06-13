#!python3
'''
https://stackoverflow.com/questions/37578628/python-checking-if-string-consists-only-of-1s-and-0s
https://stackoverflow.com/questions/11592261/check-if-a-string-is-hexadecimal
Enter a decimal number and it will be converted to binary and hex
Enter 0b and your decimal number to convert to binary
Enter 0X and your decimal number to convert to hex

Example - convert 1123 to hex
Type a number: 0x16
16
0x10
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="dec, 0b111 or 0x10 style number")
args = parser.parse_args()
inpt = args.number

if inpt.find('0b') == 0:
    inpt = inpt[2:]
    all_binary = all(c in '01' for c in inpt)
    if all_binary:
        print(' Binary Value: ', inpt)
        print('Decimal Value: ', int(inpt, 2))
        h = int(inpt, 2)
        print('    Hex Value: ', hex(int(h)))

    elif all_binary == False:
        print('Number can only contain 0 and 1')  
elif inpt.find('0x') == 0:
    '''https://www.pythonpool.com/python-hexadecimal-to-decimal/'''
    inpt = inpt[2:]
    try:
#        if int(inpt, 16):
            b = int(inpt, 16)
            print(' Binary Value: ', bin(int(b)))
            print('Decimal Value: ', int(inpt, 16))
            print('    Hex Value: ', inpt)
    except ValueError:
        print('Number can only contain a-f')
else:
    print('    Decimal Value: ', inpt)
    print('     Binary value: ', bin(int(inpt)))
    print('Hexidecimal value: ', hex(int(inpt)))

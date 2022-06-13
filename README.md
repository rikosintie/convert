# convert
Simple Python script to convert between decimal, hex, binary

**Convert Binary to Decimal and Hex**
```
convert.py -n 0b1111
 Binary Value:  1111
Decimal Value:  15
    Hex Value:  0xf
```
**Convert Hex to decimal and Binary**
```
convert.py -n 0x10
 Binary Value:  0b10000
Decimal Value:  16
    Hex Value:  10
```

**Convert Decimal to Binary and Hex**
```
convert.py -n 16
    Decimal Value:  16
     Binary value:  0b10000
Hexidecimal value:  0x10
```

**There is some basic error trapping**

Hex
```
convert.py -n 0xah
Number can only contain a-f
```

Binary
```
convert.py -n 0b1112
Number can only contain 0 and 1
```

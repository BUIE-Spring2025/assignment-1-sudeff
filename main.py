#defining values of roman letters
roman_letter_convert = {
    0:"" 
    10: "X",
    20: "XX",
    30: "XXX",
    40: "XL",
    50: "L",
    60: "LX",
    70: "LXX",
    80: "LXXX",
    90: "XC",
    100: "C",
    200: "CC",
    300: "CCC",
    400: "CD",
    500: "D",
    600: "DC",
    700: "DCC",
    800: "DCCC",
    900: "CM",
    1000: "M"
}

number=input("Please enter a number to convert:")

digit_list = [int(digit) for digit in str(number)]
roman_list=[]

def roman_convert(num):
    digit_list = [int(digit) for digit in str(num)]
    if len(digit_list)==4:
        if digit_list[1]==3:
            roman_list.append('MMM')
        elif digit_list[1]==2:
            roman_list.append('MM')
        elif digit_list[1]==1:
            roman_list.append('M')
    


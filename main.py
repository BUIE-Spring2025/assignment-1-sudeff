# Defining values for numbers to Roman letters
roman_letters = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM"
}

def int_to_roman(num):
    # Constraint: 1 <= num <= 3999
    if num < 1 or num > 3999:
        raise ValueError("Number must be between 1 and 3999")

    #Building the Roman numeral string using dictionary lookups
    return (
        roman_letters.get((num // 1000) * 1000, "") +
        roman_letters.get((num % 1000 // 100) * 100, "") +
        roman_letters.get((num % 100 // 10) * 10, "") +
        roman_letters.get(num % 10, "")
    )
def Convert_Roman( num):
        symbol = [ "M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        value = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        roman_num = ''
        i = 0
        while  num > 0:
            for x in range(num // value[i]):
                roman_num += symbol[i]
            num %= value[i]
            i += 1
        return roman_num

try:
    Number = int( input("Lütfen 1 ile 3999 arasında bir sayı giriniz: "))
    if 4000>Number>0 :
        print(Convert_Roman(Number))
    else:
        print("!!HATA!! Girdiğiniz sayı 1 ile 3999 arasında değildir")
except ValueError:
    print("Lütfen integer değer giriniz")

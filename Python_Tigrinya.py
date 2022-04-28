"""
እዛ ፕሮግራም ስምካን ዕድሜካን ትህባ እሞ፥ ንማዓስ ዓ.ም ሚእቲ ዓመት ክትገብር ኢካ ትነግር፡፡
"""
import datetime

name = input ("መን'ዩ ስምካ: ")
age = int(input("ክንደይ እዩ ዕድሚካ: "))
now = datetime.datetime.now()
by_year= int((now.year + 100) - age)
print (name + " ኣብ", by_year, "ዓ.ም ሚእቲ ዓመት ክትገብር እካ::")

"""
Output:
>>> %Run character_input.py
መን'ዩ ስምካ: ጣሃ
ክንደይ እዩ ዕድሚካ: 29
ጣሃ ኣብ 2093 ዓ.ም ሚእቲ ዓመት ክትገብር እካ::
>>> 
"""

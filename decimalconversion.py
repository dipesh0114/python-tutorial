0.1 + 0.1 + 0.4 # 0.600000000000001
0.1 + 0.1 + 0.1 # 0.300000000000004

0.1 + 0.1 + 0.1 - 0.3  # 5.55111512125783e -17 

(0.1 + 0.1 + 0.1) - 0.3   # 5.55111512125783e -17 

from decimal import Decimal

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') #Decimal('0.0)

from fractions import Fraction

myFra = Fraction(2,7)
print(myFra)



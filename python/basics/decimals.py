from decimal import Decimal, getcontext
from unicodedata import decimal

print(getcontext())

getcontext().prec = 4

print(getcontext())

print(Decimal('1.2') - Decimal('1.0'))
print(1.2 - 1.0)
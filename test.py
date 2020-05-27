# import Clock object
from clockcalc import Clock

# import converter functions
from clockcalc import minutes, hours, days

# CONSTATNTS
a = Clock(10,30)
b = Clock( 5, 0)
c = Clock( 0,30)

print('a =', a)
print('b =', b)
print('c =', c)

print()

# ARITHMETIC
# ===========

# add - clocks future
print('a + b  =', a + b)

# sub - interval or pass hours
print('a - b  =', a - b)

# floordiv - division
print('a // b =', a // c)

# mul - multiplication
print('b * c  =', b * c)


print()


# COMPARISON
# ===========

# is equals?
print('a == c =', a == c)

# is not equals?
print('a != b =', a != b)

# is greater than?
print('a > b  =', a > b)

# is less than?
print('b < a  =', b < a)

# is greater or equals?
print('c >= Clock(0,30) =', c >= Clock(0,30))

# is less that or equals?
print('c <= Clock(0,15) =', c <= Clock(0,15))

print()

# AUGMENTED ASIGNMENT
# ===================
x = Clock(9,30)
y = Clock(0,30)
x += y
print('x =', x)

print()

# CLOCK ATTRIBUTES
#==================

# .increase(minute) - increasing the clock by minute
print('a =', a)
a.increase(30)
print('a.increase(30) =', a)
print()

# .decrease(minute) - decreasing the clock by minute
print('b =', b)
b.decrease(120)
print('b.decrease(60) =', b)
print()

# .center() - the center clock of the clock
print('a =', a)
print('b =', b)
print('a.center(b) =', a.center(b))
print()

# .quarter() - the quarter times point
print('Clock(12,0).quarter() =', Clock(12,0).quarter())

# .quartal() - the quartal times of the clock
print('Clock(12,0).quartal() =', Clock(12,0).quartal())
print()

# .days() - return days leap
print('Clock(50,30).days()   =', Clock(50,30).days())
print()

# .string() - return str
print('a.string() =', a.string())
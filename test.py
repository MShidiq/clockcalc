# import Clock object
from clockcalc import Clock

# import converter functions
from clockcalc import minutes, hours, days

# CONSTATNTS
a = Clock(10,30)
b = Clock( 5, 0)
c = Clock( 0,30)

# ARITHMETIC
# ===========

# add - clocks future
print(a + b)

# sub - interval or pass hours
print(a - b)

# floordiv - division
print(a // c)

# mul - multiplication
print(b * c)

print(a)
a = Clock(a + b)
print(a)

# COMPARISON
# ===========

# is equals?
print(a == Clock(10,30))

# is not equals?
print(a != b)

# is greater than?
print(a > b)

# is less than?
print(b < a)

# is greater or equals?
print(c >= Clock(0,30))

# is less that or equals?
print(c <= Clock(0,15))



# CLOCK ATTRIBUTES
#==================

# .increase(minute) - increasing the clock by minute
a.increase(30)
print(a)

# .decrease(minute) - decreasing the clock by minute
b.decrease(120)
print(b)

# .center() - the center clock of the clock
print(a.center(b))

# .quarter() - the quarter times point
print(Clock(12,0).quarter())

# .quartal() - the quartal times of the clock
print(Clock(12,0).quartal())

# .days() - return days leap
print(Clock(48,30).days())

# .string() - return str
print(a.string())
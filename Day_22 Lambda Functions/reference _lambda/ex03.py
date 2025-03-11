hari = lambda ac, bc: ac + bc
yy = hari(4, 4)  # HERE we are save the hari function, but we called indirectly
print(yy)
del hari
print(yy)

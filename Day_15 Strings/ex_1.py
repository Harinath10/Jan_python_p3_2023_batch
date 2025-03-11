val = "we aRe pytHoN p3 baTch JanuAry , Twenty twenty three"
print(type(val))
print(val)  # we aRe pytHoN p3 baTch JanuAry , Twenty twenty three
print(val.upper())   # WE ARE PYTHON P3 BATCH JANUARY , TWENTY TWENTY THREE
print(val.lower())   # we are python p3 batch january , twenty twenty three
print(val.swapcase())  # WE ArE PYThOn P3 BAtCH jANUaRY , tWENTY TWENTY THREE
print(val.title()) # We Are Python P3 Batch January , Twenty Twenty Three
print(val.count("a"))  # 3
print(val.count("A"))  # 1
print(val.index("J"))  # 23


print("\n----------------------------------------")

val_2 = "Hello world"
print(val_2.istitle())

val_3 = "D"
print(val_3.isalpha())

val_4 = "68.0"
print(val_4.isdigit())


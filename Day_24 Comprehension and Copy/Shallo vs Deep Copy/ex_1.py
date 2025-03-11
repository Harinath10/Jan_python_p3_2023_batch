import copy

 # shallo copy

first_val = [10,20,30]
final_val = copy.copy(first_val)
final_val.append("python")
print(final_val)      # [10, 20, 30, 'python']
print(first_val)



print("===============================")

third_val = [1,2,3,[10,20],4,5]
fourth_val = copy.copy(third_val)
fourth_val[3][0] = 'Ten'
print(fourth_val)
print(third_val)
fourth_val.append("xyz")
print(fourth_val)
print(third_val)
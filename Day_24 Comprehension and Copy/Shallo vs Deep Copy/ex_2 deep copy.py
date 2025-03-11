import copy

 # deep copy

first_val = [10,20,30,[40,50,60]]
final_val = copy.deepcopy(first_val)
final_val[3][0] = 'Ten'
print(final_val)      # [10, 20, 30, 'python']
print(first_val)



print("===============================")

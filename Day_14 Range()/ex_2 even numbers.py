starting_val = int(input("enter starting val:"))
step_val = int(input("enter step val:"))
end_val = int(input("enter end val:"))

print("odd numbers is:", list(range(starting_val,end_val,step_val)))
print("even numbers is:", list(range(starting_val-1,end_val,step_val)))
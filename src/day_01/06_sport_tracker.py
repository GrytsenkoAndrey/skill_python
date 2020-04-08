
cal = 5000
step = 340
stepC = 0

while cal > 3600:
    cal = cal - step
    stepC = stepC + 1
    print(f"Step is {stepC} calories {cal}")
else:
    print(f"Steps are {stepC}")
# assumed numbers to be integer values

nums = []
terminator = -999
print("Please enter {} to terminate the program".format(terminator))
while True:
    num = int(input("Enter a number: "))
    if num == terminator: break
    else: nums.append(num)
print("Sum of the entered numbers is: ", sum(nums))
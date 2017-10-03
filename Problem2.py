#enter a non negative integer to find the the factorial of it. This requres the loop.
#done by Jessica Lam & Kevin Kye. For HW3 due on October 5, 2017.

factoral=1
input_integer=int(input("Enter a nonnegative integer:"))

for num in range(1, input_integer+1):
    factoral=num*factoral
print("The factoral of",input_integer,"is",factoral)

print("max min")
def max_min(*numbers):
    print(f"Day so duoc truyen vao: {numbers}")
    return max(numbers),min(numbers)
max,min=max_min(2,3,5,11,20,23,155)
print(f"max: {max}, min: {min}")
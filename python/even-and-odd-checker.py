numbers = [*range(1,10,1)]

# fucntions to check even or odd  ( we will pass numbers array)
def check_even_od(numbers):

    for num in numbers:
        if(num % 2 == 0):
            print(f"{num} is Even")
        else:
            print(f"{num} is odd ")
        
check_even_od(numbers)
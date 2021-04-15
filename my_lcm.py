# Program to compute the lcm of two numbers
# Two methods:

# Method 1 (Slower and Longer code):

def lcm_of_two_numbers(num1, num2):
    
    if num1 > num2:
    
        greater = num1
    
    else:
    
        greater = num2
    
    while True:
            
        if ((greater % num1 == 0) and (greater % num2 == 0)):
            
            lcm = greater
            break
        
        greater+= 1
    
    return lcm

# Method 2 (Faster and shorter):

# Formula Number1 * Number2 = L.C.M. * G.C.D.

# Finds the GCD:

def compute_gcd(x,y):
    
    while (y):
        
        x , y = y, x % y

    return x

# Find the LCM:

def compute_lcm(num1, num2):
    
    lcm = (num1 * num2)//compute_gcd(num1, num2)
    
    return lcm


print("\nProgram to find the LCM of two numbers \n")
num1 = int(input("Enter the first number: \n"))
num2 = int(input("\nEnter the second numer: \n"))

# result = lcm_of_two_numbers(num1, num2)                       # Longer method.

result = compute_lcm(num1, num2)                                # Shorter method.

print("\nThe lcm of the towo numbers " + str(num1) + " and " + str(num2) + " is: " + str(result))
print("\nEnd \n")
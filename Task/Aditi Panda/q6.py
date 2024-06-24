# Function to check whether a number is prime or not
def is_prime(n):
    # Check if n=1 or n=0
    if n <= 1:
        return False
    # Check if n=2 or n=3
    if n == 2 or n == 3:
        return True
    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check from 5 to square root of n
    # Iterate i by (i+6)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Function to find minimum and maximum prime numbers
def prime(arr):
    # To store minimum and maximum prime numbers
    maxx = -1
    minn = -1
    # create a dictionary to count elements
    mp = {}
    # Iterate to store elements in dictionary
    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    # Iterate to store minimum prime number
    for num in sorted(mp):
        if is_prime(num):
            minn = num
            break
            
    # Iterate in reverse order to find maximum prime number
    for num in sorted(mp, reverse=True):
        if is_prime(num):
            maxx = num
            break

    if minn == -1 or maxx == -1:
        print("No prime numbers found in the array")
    else:
        print("Minimum:", minn)
        print("Maximum:", maxx)
        print("The difference is:", maxx - minn)

# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    prime(arr)

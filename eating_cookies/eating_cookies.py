'''
Input: an integer
Returns: an integer
'''
cache={}
def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        cache[0] = 1
        return 1
    elif n == 2:
        cache[2] = 2
        return 2
    elif n == 3:
        cache[3] = 4
        return 4

    if n in cache:
        return cache[n]

    cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

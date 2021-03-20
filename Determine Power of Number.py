### Determine power of something by the following formula: x ** round(log(n)/log(x)) == n  ;  where x is the power of something and n is the number

### Here's an example with the power of three and the power of four

def isPowerOfThree(n):
        if n <= 0 :
            return False
        elif 3**round(log(n)/log(3)) == n:
            return True
        return False
        
def isPowerOfFour(n):
    if n <= 0:
        return False
    elif 4**round(log(n)/log(4)) == n:
        return True
    return False
    
### Now the general function

def isPowerOf(x, n):
    if n <= 0:
        return False
    elif x**round(log(n)/log(x)) == n:
        return True
    return False

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
    except:
        raise ValueError('Error: Please enter numeric values only')
        
    try:
        denominator = float(denominator)
    except:
        raise ValueError('Error: Please enter numeric values only')
          
    if denominator == 0:
        raise ZeroDivisionError('Error: Cannot divide by zero')
        
    return numerator/denominator
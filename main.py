from mean_var_std import calculate

# Test the function
if __name__ == '__main__':
    # Test case 1: Valid input
    print("Testing with valid input [0,1,2,3,4,5,6,7,8]:")
    result = calculate([0,1,2,3,4,5,6,7,8])
    print(result)
    print()
    
    # Test case 2: Invalid input
    print("Testing with invalid input [1,2,3]:")
    try:
        result = calculate([1,2,3])
    except ValueError as e:
        print(f"Error: {e}")
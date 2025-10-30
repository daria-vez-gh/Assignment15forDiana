def rod_cutting(n, prices):
    """
    Find the optimal way to cut a rod to maximize profit
    """
    # Initialize DP arrays
    max_val = [0] * (n + 1)
    first_cut = [0] * (n + 1)
    
    # Build DP table bottom-up
    for length in range(1, n + 1):
        max_value = -1
        best_cut = 0
        
        # Try all possible first cuts
        for cut in range(1, length + 1):
            # Price for cut length + optimal value for remaining length
            current_value = prices[cut - 1] + max_val[length - cut]
            
            if current_value > max_value:
                max_value = current_value
                best_cut = cut
        
        max_val[length] = max_value
        first_cut[length] = best_cut
    
    # Reconstruct the solution
    pieces = []
    remaining = n
    
    while remaining > 0:
        cut = first_cut[remaining]
        pieces.append(cut)
        remaining -= cut
    
    return max_val[n], pieces

# Example from the assignment
def test_rod_cutting():
    n = 8
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    
    max_value, pieces = rod_cutting(n, prices)
    
    print(f"Rod length: {n}")
    print(f"Prices: {prices}")
    print(f"Maximum value: {max_value}")
    print(f"Recommended pieces: {pieces}")
    print(f"Verification: Sum of pieces = {sum(pieces)}")

if __name__ == "__main__":
    test_rod_cutting()
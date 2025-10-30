def rod_cutting(length, prices):
    best_value = [0] * (length + 1)
    first_cut = [0] * (length + 1)
    
    for i in range(1, length + 1):
        max_value = 0
        best_cut = 0

        for j in range(1, i + 1):
            if j <= len(prices):
                value = prices[j - 1] + best_value[i - j]
                if value > max_value:
                    max_value = value
                    best_cut = j

        best_value[i] = max_value
        first_cut[i] = best_cut
        cuts = []
    remaining = length
    while remaining > 0:
        cuts.append(first_cut[remaining])
        remaining -= first_cut[remaining]

    return cuts, best_value[length]
    
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8
cuts, total = rod_cutting(rod_length, prices)

print("Recommended cuts: ", cuts)
print("Maximum obtainable value: ", total)
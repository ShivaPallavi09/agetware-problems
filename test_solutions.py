# test_solutions.py
from solutions import caesar_cipher, format_indian_currency, combine_lists, minimize_loss

print("--- Testing Caesar Cipher ---")
encoded = caesar_cipher("Hello World!", 3, 'encode')
print(f"Encoded: {encoded}") # Expected: Khoor Zruog!
decoded = caesar_cipher(encoded, 3, 'decode')
print(f"Decoded: {decoded}") # Expected: Hello World!

print("\n--- Testing Indian Currency Format ---")
print(f"123456.7891 -> {format_indian_currency(123456.7891)}") # Expected: 1,23,456.7891
print(f"12345678 -> {format_indian_currency(12345678)}")       # Expected: 1,23,45,678
print(f"1000 -> {format_indian_currency(1000)}")             # Expected: 1,000

print("\n--- Testing Combining Lists ---")
list1 = [{"positions": [10, 50], "values": ["A"]}]
list2 = [{"positions": [30, 80], "values": ["B"]}]
# Overlap is [30, 50], length 20. len1 is 40. 20 > 40/2 is FALSE.
# len2 is 50. 20 > 50/2 is FALSE. Should not merge.
print(f"Test 1 (No Merge): {combine_lists(list1, list2)}")
# Expected: [{'positions': [10, 50], 'values': ['A']}, {'positions': [30, 80], 'values': ['B']}]

list3 = [{"positions": [10, 50], "values": ["C"]}]
list4 = [{"positions": [15, 45], "values": ["D"]}]
# Overlap is [15, 45], length 30. len1 is 40. 30 > 40/2 is TRUE. Should merge.
print(f"Test 2 (Merge): {combine_lists(list3, list4)}")
# Expected: [{'positions': [10, 50], 'values': ['C', 'D']}]

print("\n--- Testing Minimizing Loss ---")
prices = [20, 15, 7, 2, 13]
loss = minimize_loss(prices)
# Buy at 15, sell at 12 -> loss 3
# Buy at 20, sell at 15 -> loss 5
# Buy at 20, sell at 12 -> loss 8
# Buy at 8, sell at 2 -> loss 6
print(f"Prices {prices}, Minimum Loss: {loss}") # Expected: 3

prices_2 = [5, 10, 3]
loss_2 = minimize_loss(prices_2)
# Buy at 5, sell at 3 -> loss 2
# Buy at 10, sell at 3 -> loss 7
print(f"Prices {prices_2}, Minimum Loss: {loss_2}") # Expected: 2
# solutions.py
import math
import bisect # bisect function for the efficient minimize_loss solution

# Problem 1: Caesar Cipher
def caesar_cipher(message, shift, mode='encode'):
    """
    Encodes or decodes a message using the Caesar cipher.
    :param message: The string to be processed.
    :param shift: The integer shift value.
    :param mode: 'encode' or 'decode'.
    :return: The processed string.
    """
    if mode == 'decode':
        shift = -shift
    
    result = ""
    for char in message:
        if 'a' <= char <= 'z':
            start = ord('a')
            new_pos = (ord(char) - start + shift) % 26
            result += chr(start + new_pos)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            new_pos = (ord(char) - start + shift) % 26
            result += chr(start + new_pos)
        else:
            result += char
    return result

# Problem 2: Indian Currency Format
def format_indian_currency(number):
    """
    Converts a floating-point number into a comma-separated Indian currency string.
    Eg: 1234567.89 -> 12,34,567.89
    :param number: The float or int to be formatted.
    :return: A string in Indian currency format.
    """
    s = str(number)
    if '.' in s:
        integer_part, fractional_part = s.split('.')
    else:
        integer_part, fractional_part = s, None

    last_three = integer_part[-3:]
    other_digits = integer_part[:-3]
    if other_digits:
        # Reverse the 'other_digits' string, group by 2, join with comma, then reverse back
        groups = [other_digits[max(0, i-2):i] for i in range(len(other_digits), 0, -2)]
        formatted_integer = ",".join(reversed(groups)) + "," + last_three
    else:
        formatted_integer = last_three
        
    if fractional_part:
        return f"{formatted_integer}.{fractional_part}"
    else:
        return formatted_integer

# Problem 3: Combining Two Lists
def combine_lists(list1, list2):
    """
    Combines two lists of elements based on an overlap condition.
    The lists are assumed to be sorted by left_position.
    :param list1: First list of elements.
    :param list2: Second list of elements.
    :return: A new combined list.
    """
    p1, p2 = 0, 0
    result = []
    
    while p1 < len(list1) and p2 < len(list2):
        elem1 = list1[p1]
        elem2 = list2[p2]
        
        l1, r1 = elem1['positions']
        l2, r2 = elem2['positions']
        
        overlap_start = max(l1, l2)
        overlap_end = min(r1, r2)
        overlap_len = max(0, overlap_end - overlap_start)
        
        len1 = r1 - l1
        len2 = r2 - l2
        
        if overlap_len > len1 / 2 or overlap_len > len2 / 2:
            new_elem = {
                "positions": elem1['positions'] if l1 <= l2 else elem2['positions'],
                "values": elem1['values'] + elem2['values']
            }
            result.append(new_elem)
            p1 += 1
            p2 += 1
        else:
            if l1 <= l2:
                result.append(elem1)
                p1 += 1
            else:
                result.append(elem2)
                p2 += 1
                
    result.extend(list1[p1:])
    result.extend(list2[p2:])
    
    return result

# Problem 4: Minimizing Loss
def minimize_loss(prices):
    """
    Calculates the minimum loss from buying and selling a house in later years.
    This is an O(n log n) solution, which is highly efficient.
    :param prices: A list of distinct projected prices.
    :return: The minimum possible loss.
    """
    if len(prices) < 2:
        return 0

    min_loss = float('inf')
    seen_prices = [] # This list will be kept sorted

    for price in prices:
        insertion_point = bisect.bisect_right(seen_prices, price)
        
        if insertion_point < len(seen_prices):
            potential_buy_price = seen_prices[insertion_point]
            loss = potential_buy_price - price
            if loss < min_loss:
                min_loss = loss
        
        # Add the current price to our list of seen prices, keeping it sorted.
        bisect.insort_left(seen_prices, price)
        
    return min_loss if min_loss != float('inf') else 0
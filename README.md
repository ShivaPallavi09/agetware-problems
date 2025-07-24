# AGETWARE Backend Assignment: Algorithmic Problems

This repository contains Python solutions to the problems listed in `problems.md` of the AGETWARE assignment.

## Files

-   `solutions.py`: Contains the Python functions that solve each of the four problems.
-   `test_solutions.py`: A simple script to execute the functions and demonstrate their correctness against sample inputs.

## Running the Tests

To verify the solutions, you can run the test script from your terminal:

```bash
python test_solutions.py
```

## Problem Explanations & Efficiency

Each problem was solved with a focus on efficiency and best practices.

1.  **Caesar Cipher**
    -   **Approach:** Implemented using modular arithmetic on ASCII character codes. This provides a clean and efficient solution that correctly handles letter wrapping.
    -   **Time Complexity:** $O(N)$, where N is the length of the message.

2.  **Indian Currency Format**
    -   **Approach:** Solved using string manipulation, correctly handling the unique "lakh/crore" comma style by grouping the last three digits first, then grouping the remaining digits in pairs.
    -   **Time Complexity:** $O(L)$, where L is the number of digits in the number.

3.  **Combining Two Lists**
    -   **Approach:** Since the input lists are sorted by their left position, a **two-pointer (merge-style) algorithm** was used. This approach iterates through both lists only once.
    -   **Time Complexity:** $O(N+M)$, where N and M are the lengths of the two lists. This is the optimal solution.

4.  **Minimizing Loss**
    -   **Approach:** A brute-force $O(n^2)$ solution would be too slow. This problem was solved efficiently by iterating through the prices while maintaining a **sorted list of previously seen prices**. For each new "sell" price, a binary search (`bisect`) is performed on the seen prices to find the smallest "buy" price that is still greater, thus minimizing the loss.
    -   **Time Complexity:** $O(n \log n)$. This is highly efficient and significantly better than the naive approach.

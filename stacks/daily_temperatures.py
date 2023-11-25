"""
Daily Temperatures - Medium

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

Optimal time complexity: O(n)
Optimal space complexity: O(n)
"""

def get_daily_temperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            result[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return result


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(get_daily_temperatures(temperatures))
    temperatures = [89,62,70,58,47,47,46,76,100,70]
    print(get_daily_temperatures(temperatures))
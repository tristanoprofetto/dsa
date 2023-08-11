"""
Merge Overlapping Intervals - Medium

Write a function that takes in a non-empty array of arbitrary integers and merges any overlapping invervals


Optimal Time Complexity: 
Optimal Space Complexity: 
"""

def merge_intervals(intervals):
    intervals = sorted(intervals)
    output = [intervals[0]]
    for i in range(1, len(intervals)):
        prev_start, prev_end = output[-1]
        current_start, current_end = intervals[i]
        if current_start > prev_end:
            output.append([current_start, current_end])
        else:
            output[-1][1] = max(prev_end, current_end)

    return output


if __name__ == "__main__":
    intervals = [
        [1, 2],
        [3, 5],
        [4, 6],
        [6, 12],
        [13, 18]
    ]
    merge_intervals(intervals)
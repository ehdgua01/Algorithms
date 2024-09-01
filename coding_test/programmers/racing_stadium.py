def solution(heights):
    heights.sort()
    if len(heights) % 2:
        max_height = heights.pop()
        right = len(heights) // 2
        result = [
            *(heights[right + i] - heights[i] for i in range(len(heights) // 2)),
            max_height - heights[right],
        ]
        result.sort()
        return result[1]
    else:
        right = len(heights) // 2
        return min(heights[right + i] - heights[i] for i in range(len(heights) // 2))

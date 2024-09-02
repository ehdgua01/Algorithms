def solution(board, h, w):
    positions = {
        max(0, h - 1): [w],
        min(len(board) - 1, h + 1): [w],
        h: [max(0, w - 1), min(len(board) - 1, w + 1)],
    }
    return sum(
        board[height][width] == board[h][w]
        for height in positions
        for width in positions[height]
        if not (height == h and width == w)
    )


def test_cases():
    assert (
        solution(
            [
                ["blue", "red", "orange", "red"],
                ["red", "red", "blue", "orange"],
                ["blue", "orange", "red", "red"],
                ["orange", "orange", "red", "blue"],
            ],
            3,
            1,
        )
        == 2
    )
    assert (
        solution(
            [
                ["yellow", "green", "blue"],
                ["blue", "green", "yellow"],
                ["yellow", "blue", "blue"],
            ],
            0,
            1,
        )
        == 1
    )

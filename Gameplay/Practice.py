import unittest

# Test the function reverse()
def reverse(gridCell):
    for ind in range(4):
        i = 0
        j = 3
        while (i < j):
            gridCell[ind][i], gridCell[ind][j] = gridCell[ind][j], gridCell[ind][i]
            i += 1
            j -= 1
    return gridCell

def transpose(gridCell):
    temp=[list(t) for t in zip(*gridCell)]
    gridCell.clear()
    gridCell.extend(temp)
    return gridCell

def compressGrid(gridCell):
        compress = False
        # Create a clone grid
        temp = [[0] * 4 for i in range(4)]
        for i in range(4):
            cnt = 0
            for j in range(4):
                # If encountering a non-zero element, move this element to the leftmost position in the new grid
                if gridCell[i][j] != 0:
                    temp[i][cnt] = gridCell[i][j]

                    # If the element is moved from its original position
                    if cnt != j:
                        compress = True
                    cnt += 1
        # Set the compressed grid cell to gridCell
        gridCell = temp
        return gridCell


def mergeGrid(gridCell):
    merge = False
    for i in range(4):
        for j in range(3):
            # If found 2 equal elements and they are non-zeroes
            if gridCell[i][j] == gridCell[i][j + 1] and gridCell[i][j] != 0:
                gridCell[i][j] *= 2
                gridCell[i][j + 1] = 0
                #score += self.gridCell[i][j]
                merge = True
    return gridCell



def printGridCell(gridCell):
    for row in gridCell:
        print("+----" * len(row) + "+")
        print("|" + "|".join(f"{cell:4}" for cell in row) + "|")
    print("+----" * len(gridCell[0]) + "+")

class TestReverseFunction(unittest.TestCase):
    def test_reverse_unique_elements(self):
        grid=[
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        expected = [
            [4, 3, 2, 1],
            [8, 7, 6, 5],
            [12, 11, 10, 9],
            [16, 15, 14, 13]
        ]
        self.assertEqual(reverse(grid), expected)

    def test_reverse_repeating_elements(self):
        grid = [
            [1, 1, 2, 2],
            [3, 3, 4, 4],
            [5, 5, 6, 6],
            [7, 7, 8, 8]
        ]
        expected = [
            [2, 2, 1, 1],
            [4, 4, 3, 3],
            [6, 6, 5, 5],
            [8, 8, 7, 7]
        ]
        self.assertEqual(reverse(grid), expected)
    def test_reverse_all_same_elements(self):
        grid = [
            [1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3],
            [4, 4, 4, 4]
        ]

        expected = grid.copy()
        self.assertEqual(reverse(grid), expected)
    def test_reverse_mix_of_zero_and_non_zero_elements(self):
        grid = [
            [0, 0, 0, 1],
            [2, 0, 0, 0],
            [0, 3, 0, 0],
            [0, 0, 4, 0]
        ]
        expected = [
            [1, 0, 0, 0],
            [0, 0, 0, 2],
            [0, 0, 3, 0],
            [0, 4, 0, 0]
        ]
        self.assertEqual(reverse(grid), expected)

class TestTransposeFunction(unittest.TestCase):
    def test_transpose_square_matrix(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected = [[1, 5], [2, 6], [3, 7], [4, 8]]
        result = transpose(grid)
        self.assertEqual(grid, expected)

    def test_transpose_single_row(self):
        grid = [[1, 2, 3]]
        expected = [[1], [2], [3]]
        result = transpose(grid)
        self.assertEqual(grid, expected)

    def test_transpose_single_column(self):
        grid = [[1], [2], [3]]
        expected = [[1, 2, 3]]
        result = transpose(grid)
        self.assertEqual(grid, expected)

class TestCompressFunction(unittest.TestCase):
    def test_compression_with_empty_grid(self):
        grid=[[0, 0, 0, 0] for _ in range(4)]
        expected=[[0, 0, 0, 0] for _ in range(4)]
        result=compressGrid(grid)
        self.assertEqual(result, expected, "Empty grid should remain unchanged!")

    def test_compression_with_no_compress_needed(self):
        grid = [[1, 2, 3, 4], [4, 3, 2, 1], [0, 1, 0, 2], [2, 0, 1, 0]]
        expected = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 0, 0], [2, 1, 0, 0]]
        result = compressGrid(grid)
        self.assertEqual(result, expected, "Grid should be compressed correctly.")

    def test_compress_with_full_compress_needed(self):
        grid = [[0, 0, 0, 1], [0, 0, 2, 0], [0, 3, 0, 0], [4, 0, 0, 0]]
        expected = [[1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0]]
        result = compressGrid(grid)
        self.assertEqual(result, expected, "All rows should be compressed to the left.")

    def test_compress_with_partial_compress_needed(self):
        grid = [[2, 0, 2, 2], [0, 0, 0, 3], [4, 4, 0, 0], [0, 5, 0, 5]]
        expected = [[2, 2, 2, 0], [3, 0, 0, 0], [4, 4, 0, 0], [5, 5, 0, 0]]
        result = compressGrid(grid)
        self.assertEqual(result, expected, "Rows should be partially compressed to the left.")

class TestMergeGridFunction(unittest.TestCase):
    def test_merge_adjacent_identical_elements(self):
        grid = [[2, 2, 4, 0], [4, 4, 4, 4], [0, 0, 2, 2], [2, 0, 0, 0]]
        expected=[[4, 0, 4, 0], [8, 0, 8, 0], [0, 0, 4, 0], [2, 0, 0, 0]]
        merged_grid=mergeGrid(grid)
        self.assertEqual(merged_grid, expected, "Adjacent identical elements should be merged." )

    def test_no_merge_for_non_adjacent_elements(self):
        grid = [[2, 0, 2, 4], [4, 0, 0, 4], [2, 4, 2, 4], [0, 0, 0, 0]]
        expected = [[2, 0, 2, 4], [4, 0, 0, 4], [2, 4, 2, 4], [0, 0, 0, 0]]
        merged_grid = mergeGrid(grid)
        self.assertEqual(merged_grid, expected, "Non-adjacent identical elements should not be merged.")

    def test_sequence_of_more_than_two_identical_elements(self):
        grid = [[2, 2, 2, 2], [0, 0, 0, 0], [2, 2, 4, 4], [16, 16, 8, 8]]
        expected_output = [[4, 4, 0, 0], [0, 0, 0, 0], [4, 0, 8, 0], [32, 0, 16, 0]]
        merged_grid = mergeGrid(grid)
        self.assertEqual(merged_grid, expected_output,
                         "Only the first pair in a sequence of more than two identical elements should be merged.")


    def test_no_elements_to_merge(self):
        grid = [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 16384, 32768, 65536]]
        expected = [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 16384, 32768, 65536]]
        merged_grid = mergeGrid(grid)
        self.assertEqual(merged_grid, expected, "Grid without mergable elements should remain unchanged.")


if __name__ == '__main__':
    unittest.main()





#gridCell=[[1, 0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#print("Before: ")
#printGridCell(gridCell)
#reversedGridCell=reverse(gridCell)
#print("After: ")
#printGridCell(reversedGridCell)

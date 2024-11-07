# Author: Ashton Lee
# Github User: ashton01L
# Date: 11/6/2024
# Description: You are given a puzzle consisting of a row of squares that contain nonnegative integers, with a zero in
# the rightmost square.
def row_puzzle(row):
    """
    Determines if a puzzle is solvable by trying to move a token from the first index
    to the last index, based on the values in the squares. The token can only move left
    or right by a number of squares equal to the current square's value.

    :param:
        row (list): A list of non-negative integers where the last element is zero.

    :return:
        bool: True if it is possible to reach the last square, False otherwise.
    """
    # Create a set to track visited indices
    visited = set()

    def dfs(index):
        """
        Helper function that recursively determines if the puzzle is solvable from the current index.

        :param:
            index (int): The current index of the token in the row.
            visited (set): A set of indices already visited to avoid cycles.

        :return:
            bool: True if the last square is reachable from the current index, False otherwise.
        """
        # Base case: if we're at the last index
        if index == len(row) - 1:
            return True

        # If we have already visited this index, return False to avoid cycles
        if index in visited:
            return False

        # Mark this index as visited
        visited.add(index)

        move_distance = row[index]

        # Try moving right
        if index + move_distance < len(row) and dfs(index + move_distance):
            return True

        # Try moving left
        if index - move_distance >= 0 and dfs(index - move_distance):
            return True

        # If no valid moves, unmark and return False
        visited.remove(index)
        return False

    # Start recursion from index 0
    return dfs(0)

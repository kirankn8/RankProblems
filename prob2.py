# Problem :

"""
Given a squared sized grid G of size N in which each cell has a
lowercase letter. Denote the character in the ith row and in the jth
column as G[i][j].

You can perform one operation as many times as you like: Swap two
column adjacent characters in the same row G[i][j] and G[i][j+1] for
all valid i,j.

Is it possible to rearrange the grid such that the following
condition is true?

G[i][1]≤G[i][2]≤⋯≤G[i][N] for 1≤i≤N and G[1][j]≤G[2][j]≤⋯≤G[N][j] for
1≤j≤N

In other words, is it possible to rearrange the grid such that every
row and every column is lexicographically sorted?

Note: c1≤c2, if letter c1 is equal to c2 or is before c2 in the
alphabet.

Input Format

The first line begins with T, the number of testcases. In each
testcase you will be given N. The following N lines contain N
lowercase english alphabet each, describing the grid.

Output Format

Print T lines. On the ith line print YES if it is possible to
rearrange the grid in the ith testcase or NO otherwise.

"""

def gridChallenge(grid):
    # Complete this function
    for i in range(len(grid)):
        grid[i] = list(grid[i])
        grid[i].sort()
    
    transposed_grid = list(zip(*grid))
    for ele in transposed_grid:
        prev_str = "".join(ele)
        new_str = "".join(sorted(ele))
        if prev_str != new_str:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        grid = []
        grid_i = 0
        for grid_i in range(n):
           grid_t = str(input().strip())
           grid.append(grid_t)
        result = gridChallenge(grid)
        print(result)

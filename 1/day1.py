import pandas as pd

# Read and split into two series
df = pd.read_csv('input.txt', sep=' ', header=None)
df = df[[0,3]]

left = df[0].sort_values().reset_index(drop=True)
right = df[3].sort_values().reset_index(drop=True)

# fin is part1, fin2 is part2
fin = 0
fin2 = 0

for i in range(0, 1000):
    fin += abs(left[i] - right[i])

    # For part 2, grab the number and then get the length of the filtered right series
    left_num = left[i]
    right_count = len(right.loc[right == left_num])

    fin2 += left_num * right_count

print(fin)
print(fin2)
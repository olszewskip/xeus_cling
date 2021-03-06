import random

# ---1---
gpu_tile_width = 100
cpu_tile_width = 13
is_fat_interesting_region_present = 1
number_of_lean_regions = 3
column_and_bucket_counts = """
4 4
2 5
1 6
117 2
9886 2
30 4
30 5
30 6
200 2
"""
row_count = 100
#

# # ---2---
# gpu_tile_width = 100
# cpu_tile_width = 10
# is_fat_interesting_region_present = 1
# number_of_lean_regions = 3
# column_and_bucket_counts = """
# 0 4
# 2 5
# 1 6
# 117 2
# 9886 2
# 30 4
# 30 5
# 30 6
# 200 2
# """
# row_count = 100
# #


with open("dummy_gpu_tile_width.txt", "w") as output_file:
        output_file.write(str(gpu_tile_width))
        
with open("dummy_cpu_tile_width.txt", "w") as output_file:
        output_file.write(str(cpu_tile_width))

with open("dummy_is_fat_interesting_region_present.txt", "w") as output_file:
        output_file.write(str(is_fat_interesting_region_present))
        
with open("dummy_number_of_lean_regions.txt", "w") as output_file:
        output_file.write(str(number_of_lean_regions))

column_and_bucket_counts = \
[tuple(map(int, column_and_bucket_count.split())) \
 for column_and_bucket_count in column_and_bucket_counts.strip().split("\n")]

with open("dummy_column_and_bucket_counts.csv", "w") as output_file:
    for column_count, bucket_count in column_and_bucket_counts:
        output_file.write(f"{column_count},{bucket_count}\n")

consequtive_bucket_counts =\
[bucket_count \
 for column_count, bucket_count in column_and_bucket_counts \
 for _ in range(column_count)]

data = []

for _ in range(row_count):
    row = []
    for bucket_count in consequtive_bucket_counts:
        row.append(random.randint(0, bucket_count - 1))
    data.append(row)
    
for column_index in range(len(data[0])):
    column_values = set(data[row_index][column_index] for row_index in range(row_count))
    assert column_values.issubset(range(consequtive_bucket_counts[column_index]))

with open("dummy_discrete_data.csv", "w") as output_file:
    for row in data:
        output_file.write(",".join(map(str, row)))
        output_file.write("\n")

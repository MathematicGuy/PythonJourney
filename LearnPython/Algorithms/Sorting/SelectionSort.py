nums = [1, 2, 8, 9, 7, 6, 4, 5, 3]

int_min = 999999999
int_temp = 0

for num in nums:
	currentNumPos = nums.index(num)  # current num position
	print("current num pos: {}".format(currentNumPos))
	for pos in range(len(nums[currentNumPos:])):
		print(f"Selecting item #{pos}")
		if nums[pos] < num:
			int_min = nums[pos]

	int_temp = currentNumPos

print()
print(nums)


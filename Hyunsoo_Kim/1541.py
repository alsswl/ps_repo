formula = input()
flag = 0
if (formula[0] == "-"):
    flag = 1
form_list = formula.split("-")

# -를 제외한 항들의 핪의 값
nums = []

for form in form_list:
    tmp_sum = 0
    tmp_nums = form.split('+')
    if tmp_nums[0] == "":
        continue
    for num in tmp_nums:
        tmp_sum += int(num)
    nums.append(tmp_sum)

# print(nums)
ans = 0
if flag == 0:
    ans += nums[0]
    for num in nums[1:]:
        ans -= num
else:
    for num in nums:
        ans -= num


print(ans)

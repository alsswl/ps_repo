
# 전체 배열 원소 갯수
N = int(input())

# 배열 입력받기
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# 어차피 하나만 정렬하라했지만, 상관없음.
arr_a = sorted(arr_a)
arr_b = sorted(arr_b)
# 단, B는 역순으로 정렬
arr_b = arr_b[::-1]
# print(arr_b)

ans = 0

# 곱셈 합 구하기
for i in range(N):
    ans += (arr_a[i]*arr_b[i])


print(ans)

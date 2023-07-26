T = int(input())

# 회사원을 뽑는 함수


def recruit():
    # 지원자수 입력받기
    N = int(input())
    # 지원자 풀 저장할 리스트
    people = []
    # 지원자 입력받기
    for i in range(N):
        people.append(list(map(int, input().split())))

    # 지원자를 서류 순위로 정렬
    people.sort(key=lambda x: x[0])
    print(people)

    # 우선적으로 서류 1등 무조건 선발.
    ans = 1

    # 현재 면접 순위 가장 높은 사람
    top_interview = people[0][1]

    # 순차적으로 1번 사람을 제외하고,
    for ppl in people[1:]:
        # 면접 순위가 이미 뽑은 사람들 중 제일 높은 사람보다 높으면 계속 선발
        if ppl[1] < top_interview:
            ans += 1
            # 면접 최고점자가 바뀌면 면접 최고 순위 변경
            top_interview = ppl[1]
    print(ans)


for i in range(T):
    recruit()

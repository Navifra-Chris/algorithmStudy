import sys

input = sys.stdin.readline

t = int(input())

def solve():
    team_count = 0  # 숫자를 직접 관리하기 위해 team 리스트 대신 team_count 사용
    visited = [-1 for _ in range(n + 1)]  # -1로 초기화하여 아직 방문하지 않았음을 표시
    for start in range(1, n+1):
        if visited[start] != -1:
            continue
        
        current = start
        path = []

        while visited[current] == -1:
            visited[current] = start  # 현재 탐색 중인 시작 학생의 번호를 저장
            path.append(current)
            current = students[current]

        if visited[current] == start:  # 순환 구조가 시작된 학생과 동일한 학생을 만났을 때
            team_count += len(path) - path.index(current)

    print(n - team_count)

if __name__ == '__main__':
    for test_case in range(t):
        n = int(input())
        students = [0] + list(map(int, input().split()))

        solve()
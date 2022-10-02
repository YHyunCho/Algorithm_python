# PROGRAMMERS Lv2 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

# 작성자 : 조예현
# 최초 작성일 : 2022-09-26
# 최종 작성일 : 2022-10-01

def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people)-1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        
        answer += 1
    return answer

people = [70, 50, 80, 50]
limit = 100

solution(people, limit)
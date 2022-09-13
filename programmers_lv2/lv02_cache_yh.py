# PROGRAMMERS Lv1 [1차] 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

# 작성자 : 조예현
# 최초 작성일 : 2022-08-18
# 최종 작성일 : 2022-08-18

# LRU algorithm is that change pages that haven't been referenced for the longest time

def solution(cacheSize, cities) :
  answer = 0
  cache = [0 for i in range(5)]
  
  for i in range(len(cities)) :
    cities[i] = cities[i].lower()

  for i in range(len(cities)) :
    if cities[i] in cache :
      cache.pop(cache[cache.find(cities[i])])
      cache.append(cities[i])
      answer += 1
    else :
      cache = cache[1:]
      cache.append(cities[i])
      answer += 5

  print(answer)


  

  


cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
solution(cacheSize, cities)
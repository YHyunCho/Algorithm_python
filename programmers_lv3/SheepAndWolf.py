# PROGRAMMERS Lv3 양과 늑대
# https://school.programmers.co.kr/learn/courses/30/lessons/92343?language=python3

# 작성자 : 조예현
# 최초 작성일 : 2022-09-13
# 최종 작성일 : 2022-09-18

from collections import defaultdict

def dfs(node, sheep, wolf, visit, can_go):
    global answer, infos, tree
    
    # Change the corrent node to visiting
    visit[node] = 1
    # Add the child nodes of the corrent node in 'can_go' List 
    can_go += tree[node]
    
    # Counting wolves or sheep on the current node
    if infos[node]: wolf += 1
    else: sheep += 1
    
    # If there are more wolves than sheep, return
    if wolf >= sheep: return
    
    # If the sheep number is the maximum, Change the answer 
    if sheep > answer: answer = sheep
    
    # Continue the search to the node where it can go
    for n in can_go:
    	# remove node n from the 'can_go' list
        go = [nn for nn in can_go if nn != n and not visit[nn]]
        dfs(n, sheep, wolf, visit[:], go)
    
    
def solution(info, edges):
    global answer, infos, tree
    infos = info
    answer = 0
   
    tree = defaultdict(list)
    for key, value in edges:
        tree[key].append(value)
        
    visit = [0]*len(info)
    dfs(0, 0, 0, visit, [])
    
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
solution(info, edges)
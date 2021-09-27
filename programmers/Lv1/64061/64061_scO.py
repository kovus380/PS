# 64061 | 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
from typing import List


def solution(board: List[int], moves: List[int]) -> int:
    answer = 0
    stack = []
    for move in moves:
        for col in board:
            if col[move-1] != 0:
                stack.append(col[move - 1])
                col[move - 1] = 0
                while len(stack) >= 2 and (stack[-1] == stack[-2]):
                    stack.pop()
                    stack.pop()
                    answer += 2
                break


    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
res = solution(board, moves)
print(res)
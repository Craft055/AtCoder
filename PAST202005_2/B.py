#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import collections

def input():
    return sys.stdin.readline()



def resolve():
    n, m, q = map(int, input().split())

    s_list = [input().split() for i in range(q)]
    participant_solved_problem = []
    score_list = [0] * n
    problem_score_list = [n] * m

    data_deque = collections.deque([])

    for query in s_list:
        if query[0] == "2":
            if problem_score_list[int(query[2])-1] > 0:
                problem_score_list[int(query[2])-1] -= 1
            data_deque.append([int(query[1]), int(query[2])])
    print(data_deque)


    for query in s_list:
        if query[0] == "1":
            print(score_list[int(query[1])-1])
        if query[0] == "2":
            if problem_score_list[int(query[2])-1] > 0:
                problem_score_list[int(query[2])-1] -= 1
                pair = data_deque.popleft()
                for pair in participant_solved_problem:
                    if int(query[2]) == pair[1] and pair[0] != query[1]:
                            score_list[pair[0]-1] -= 1

                participant_solved_problem.append([int(query[1]), int(query[2])])


            score_list[int(query[1])-1] += problem_score_list[int(query[2])-1]





if __name__ == "__main__":
    resolve()


from itertools import permutations
from collections import deque
import re


def solution(expression):
    answer = 0
    cumulative_num = ""
    s = []
    for char in expression:
        if char not in ["*", "-", "+"]:
            cumulative_num += char
        else:
            s.append(int(cumulative_num))
            s.append(char)
            cumulative_num = ""
    s.append(int(cumulative_num))
    op = [x for x in expression if x in ["*", "-", "+"]]
    # Regexp 이용한 방법
    """ 
    nums=re.split('\*|\+|\-',expression)
    num_q=deque(nums)
    
    s=list()
    i,j=0,0
    
    while i<len(nums) and j<len(op):
        s.append(nums[i])
        s.append(op[j])
        i+=1
        j+=1
    s.append(nums[-1])
    """
    op = list(set(op))

    for op_set in permutations(op, len(op)):
        c_s = s[:]
        for op_order in op_set:
            i = 0
            dynamic_len = len(c_s)
            while i < dynamic_len:
                if c_s[i] == op_order:
                    first, second = c_s[i - 1], c_s[i + 1]
                    val = eval(str(first) + op_order + str(second))
                    c_s = c_s[: i - 1] + [val] + c_s[i + 2 :]
                    i -= 1

                dynamic_len = len(c_s)
                i += 1
        answer = max(answer, abs(int(c_s[0])))
    return answer

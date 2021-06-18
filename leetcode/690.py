"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    # id 1의 subordinates이 2나 3이라는 보장이 없으므로
    # dict을 이용해서 lookup을 먼저 만들어줌
    # employee의 subordinate의 id를 기반으로 lookup 수행
    self.lookup={emp.id:emp for emp in employees}


    def dfs(Employee):

      if not Employee.subordinates:
        return Employee.importance

      else:
        return Employee.importance + sum(
            dfs(self.lookup[sub]) for sub in Employee.subordinates)

    return dfs(self.lookup[id])
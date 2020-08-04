#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

struct treeNode {
  int id;
  vector<int> childs;
  bool deleted;
};

#define NODE_MAX 50

int N, deleted, leaf_cnt, root_idx;
treeNode nodes[NODE_MAX];

int ans();

void bfs(queue<int>);

int main(void) {
  leaf_cnt = 0;
  cin >> N;
  for (int i = 0; i <= N - 1; i++) {
    nodes[i].id = i;
    nodes[i].deleted = false;
  }
  for (int i = 0; i <= N - 1; i++) {
    int tmp;
    cin >> tmp;

    // 루트가 아니라면
    // 부모 노드의 자식에 현재 i번 노드를 추가
    if (tmp != -1) {
      nodes[tmp].childs.push_back(i);
    }
    // 루트 노드라면 위치를 기억
    else {
      root_idx = i;
    }
  }
  cin >> deleted;
  nodes[deleted].deleted = true;
  cout << ans();
}

int ans() {
  queue<int> q;
  // 루트부터 bfs 탐색 시작
  q.push(root_idx);
  bfs(q);
  return leaf_cnt;
}

void bfs(queue<int> q) {
  while (!q.empty()) {
    treeNode frontNode = nodes[q.front()];
    q.pop();

    // 삭제될 노드가 아니라면
    // 개수를 늘리고 자식노드 탐색
    if (!frontNode.deleted) {
      // 원래 리프노드이거나
      // 자식이 1개인 노드인데 그 자식이 삭제되어서
      // frontNode가 리프노드가 된다면
      if (frontNode.childs.size() == 0 ||
          (frontNode.childs.size() == 1 &&
           nodes[frontNode.childs[0]].deleted == true)) {
        leaf_cnt++;
      }
      for (int i = 0; i < frontNode.childs.size(); i++) {
        // frontNode들의 자식들에 대해서도 탐색을 한다
        q.push(frontNode.childs[i]);
      }
    }
    // 삭제될 노드라면
    // 탐색할 필요가 없음
    else {
      continue;
    }
  }
}
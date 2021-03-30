#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

struct water {
  int a;
  int b;
  int c;
};

priority_queue<int,vector<int>,greater<int>> pq;
bool visited[201][201][201];

int A, B, C;

void ans();

void bfs(queue<water>);

int main(void) {
  memset(visited, false, sizeof(visited));
  cin >> A >> B >> C;
  ans();
}

void ans() {
  queue<water> q;

  q.push({0, 0, C});
  visited[0][0][C] = true;
  bfs(q);

  while (!pq.empty()) {
    cout << pq.top() << " ";
    pq.pop();
  }
}

void bfs(queue<water> q) {
  while (!q.empty()) {
    water front = q.front();
    q.pop();

    if (front.a == 0) {
      pq.push(front.c);
    }

    // a에서 b로 옮길때

    // a 물을 b로 다 옮길때
    if (front.a + front.b <= B && !visited[0][front.a + front.b][front.c]) {
      q.push({0, front.a + front.b, front.c});
      visited[0][front.a + front.b][front.c] = true;
    }
    // a의 일부분만 b로 옮길때
    else if (front.a + front.b > B &&
             !visited[front.a + front.b - B][B][front.c]) {
      q.push({front.a + front.b - B, B, front.c});
      visited[front.a + front.b - B][B][front.c] = true;
    }

    // a->c

    // a 물을 c로 다 옮길때
    if (front.a + front.c <= C && !visited[0][front.b][front.c + front.a]) {
      q.push({0, front.b, front.c + front.a});
      visited[0][front.b][front.c + front.a] = true;
    }
    // a의 일부분만 c로 옮길때
    else if (front.a + front.c > C &&
             !visited[front.a + front.c - C][front.b][C]) {
      q.push({front.a + front.c - C, front.b, C});
      visited[front.a + front.c - C][front.b][C] = true;
    }

    // b->a

    if (front.b + front.a <= A && !visited[front.a + front.b][0][front.c]) {
      q.push({front.a + front.b, 0, front.c});
      visited[front.a + front.b][0][front.c] = true;
    }

    else if (front.b + front.a > A &&
             !visited[A][front.a + front.b - A][front.c]) {
      q.push({A, front.a + front.b - A, front.c});
      visited[A][front.a + front.b - A][front.c] = true;
    }

    // b->c
    if (front.b + front.c <= C && !visited[front.a][0][front.b + front.c]) {
      q.push({front.a, 0, front.b + front.c});
      visited[front.a][0][front.b + front.c] = true;
    }

    else if (front.b + front.c > C &&
             !visited[front.a][front.c + front.b - C][C]) {
      q.push({front.a, front.c + front.b - C, C});
      visited[front.a][front.c + front.b - C][C] = true;
    }

    // c->a

    if (front.a + front.c <= A && !visited[front.a + front.c][front.b][0]) {
      q.push({front.a + front.c, front.b, 0});
      visited[front.a + front.c][front.b][0] = true;
    }

    else if (front.a + front.c > A &&
             !visited[A][front.b][front.c + front.a - A]) {
      q.push({A, front.b, front.c + front.a - A});
      visited[A][front.b][front.c + front.a - A] = true;
    }

    // c->b

    if (front.c + front.b <= B && !visited[front.a][front.c+front.b][0]) {
      q.push({front.a, front.c+front.b, 0});
      visited[front.a][front.c+front.b][0] = true;
    }

    else if (front.c + front.b > B &&
             !visited[front.a][B][front.c + front.b - B]) {
      q.push({front.a, B, front.c + front.b - B});
      visited[front.a][B][front.c + front.b - B] = true;
    }
  }
}
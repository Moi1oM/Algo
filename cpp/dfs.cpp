#include <bits/stdc++.h>

using namespace std;

bool visited[9];
vector<int> graph[9];

// DFS �Լ� ����
void dfs(int x) {
    // ���� ��带 �湮 ó��
    visited[x] = true;
    cout << x << ' ';
    // ���� ���� ����� �ٸ� ��带 ��������� �湮
    for (int i = 0; i < graph[x].size(); i++) {
        int y = graph[x][i];
        if (!visited[y]) dfs(y);
    }
}

int main(void) {
    // ��� 1�� ����� ��� ���� ���� 
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);
    
    // ��� 2�� ����� ��� ���� ���� 
    graph[2].push_back(1);
    graph[2].push_back(7);
    
    // ��� 3�� ����� ��� ���� ���� 
    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);
    
    // ��� 4�� ����� ��� ���� ���� 
    graph[4].push_back(3);
    graph[4].push_back(5);
    
    // ��� 5�� ����� ��� ���� ���� 
    graph[5].push_back(3);
    graph[5].push_back(4);
    
    // ��� 6�� ����� ��� ���� ���� 
    graph[6].push_back(7);
    
    // ��� 7�� ����� ��� ���� ���� 
    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);
    
    // ��� 8�� ����� ��� ���� ���� 
    graph[8].push_back(1);
    graph[8].push_back(7);
    
    dfs(1);
}


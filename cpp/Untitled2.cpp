#include <iostream>
#include <vector>

using namespace std;

// 맵의 크기를 넘을 경우 예외 처리 함수 oversize()
bool oversize(int c, int r, vector<vector<int> > map)
{
	if (c >= map.size() || r >= map[0].size() || c < 0 || r < 0)
		return true;
	else
		return false;
}
bool turn(int c, int r, int& move_y, int& move_x, int& d, vector<vector<int> >& map, int &back_y, int& back_x)
{
	int cnt = 0;				// 사방이 막혀있는지 확인용 변수
	move_x = 0, move_y = 0;		// 초기화

	d = (d + 4 - 1) % 4;		// 방향 회전

	while (cnt != 4)
	{
		switch (d)
		{
		// 북쪽
		case 0:
			// 맵의 크기를 넘을 경우 예외 처리 함수 oversize()
			if (!oversize(c - 1, r, map))
			{
				if (map[c - 1][r] == 0)
				{
					move_y = -1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// 그 방향에서의 왼쪽
			back_x = 0;
			back_y = 1;
			cnt++;

			break;
		// 동쪽
		case 1:
			if (!oversize(c, r + 1, map))
			{
				if (map[c][r + 1] == 0)
				{
					move_x = 1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// 그 방향에서의 왼쪽
			back_x = -1;
			back_y = 0;
			cnt++;

			break;
		// 남쪽
		case 2:
			if (!oversize(c + 1, r, map))
			{
				if (map[c + 1][r] == 0)
				{
					move_y = 1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// 그 방향에서의 왼쪽	
			back_x = 0;
			back_y = -1;
			cnt++;

			break;
		// 서쪽
		case 3:
			if (!oversize(c, r - 1, map))
			{
				if (map[c][r - 1] == 0)
				{
					move_x = -1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// 그 방향에서의 왼쪽	
			back_x = 1;
			back_y = 0;
			cnt++;

			break;
		}
	}

	d = (d + 4 + 1) % 4;		// 한 번 더 돌았으므로 조건 2.c를 만족하기 위해 반대로 한 번 돌아준다.

	return false;
}

int main()
{
	int n, m;		// 세로(n)와 가로(m)
	cin >> n >> m;
	int r, c, d;
	cin >> c >> r >> d;
	vector<vector<int> > map;

	// map 입력
	for (int i = 0; i < n; i++)
	{
		vector<int> v(0, 0);
		for (int j = 0; j < m; j++)
		{
			int num;
			scanf("%d", &num);
			v.push_back(num);
		}
		map.push_back(v);
	}

	map[c][r] = 2;
	int clean_n = 1;				// 청소한 방의 개수

	int move_x = 0, move_y = 0;		// 이동할 거리
	int back_x = 0, back_y = 0;	// 후진할 좌표를 알려줌.
	
	// 사방이 막혔고 뒤가 벽이라면 동작을 멈춘다.
	while (map[c][r] != 1)
	{
		// 회전할 수 있다면(= 이동할 수 있다면)
		if (turn(c, r, move_y, move_x, d, map, back_y, back_x))
		{
			// 이동한다.
			c += move_y;
			r += move_x;

			map[c][r] = 2;
			clean_n++;
			cout<<c<<" "<<r<<endl;
		}
		// 사방이 막혀있거나 청소되어 있다면
		else
		{
			// 후진한다.
			if (!oversize(c + back_y, r + back_x, map))
			{
				c += back_y;
				r += back_x;
			}
			// 후진을 하면 맵에서 벗어나므로 동작 종료.
			else
				break;
		}
	}

	cout << clean_n << endl;

}

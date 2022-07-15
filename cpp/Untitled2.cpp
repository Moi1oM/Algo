#include <iostream>
#include <vector>

using namespace std;

// ���� ũ�⸦ ���� ��� ���� ó�� �Լ� oversize()
bool oversize(int c, int r, vector<vector<int> > map)
{
	if (c >= map.size() || r >= map[0].size() || c < 0 || r < 0)
		return true;
	else
		return false;
}
bool turn(int c, int r, int& move_y, int& move_x, int& d, vector<vector<int> >& map, int &back_y, int& back_x)
{
	int cnt = 0;				// ����� �����ִ��� Ȯ�ο� ����
	move_x = 0, move_y = 0;		// �ʱ�ȭ

	d = (d + 4 - 1) % 4;		// ���� ȸ��

	while (cnt != 4)
	{
		switch (d)
		{
		// ����
		case 0:
			// ���� ũ�⸦ ���� ��� ���� ó�� �Լ� oversize()
			if (!oversize(c - 1, r, map))
			{
				if (map[c - 1][r] == 0)
				{
					move_y = -1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// �� ���⿡���� ����
			back_x = 0;
			back_y = 1;
			cnt++;

			break;
		// ����
		case 1:
			if (!oversize(c, r + 1, map))
			{
				if (map[c][r + 1] == 0)
				{
					move_x = 1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// �� ���⿡���� ����
			back_x = -1;
			back_y = 0;
			cnt++;

			break;
		// ����
		case 2:
			if (!oversize(c + 1, r, map))
			{
				if (map[c + 1][r] == 0)
				{
					move_y = 1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// �� ���⿡���� ����	
			back_x = 0;
			back_y = -1;
			cnt++;

			break;
		// ����
		case 3:
			if (!oversize(c, r - 1, map))
			{
				if (map[c][r - 1] == 0)
				{
					move_x = -1;
					return true;
				}
			}

			d = (d + 4 - 1) % 4;	// �� ���⿡���� ����	
			back_x = 1;
			back_y = 0;
			cnt++;

			break;
		}
	}

	d = (d + 4 + 1) % 4;		// �� �� �� �������Ƿ� ���� 2.c�� �����ϱ� ���� �ݴ�� �� �� �����ش�.

	return false;
}

int main()
{
	int n, m;		// ����(n)�� ����(m)
	cin >> n >> m;
	int r, c, d;
	cin >> c >> r >> d;
	vector<vector<int> > map;

	// map �Է�
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
	int clean_n = 1;				// û���� ���� ����

	int move_x = 0, move_y = 0;		// �̵��� �Ÿ�
	int back_x = 0, back_y = 0;	// ������ ��ǥ�� �˷���.
	
	// ����� ������ �ڰ� ���̶�� ������ �����.
	while (map[c][r] != 1)
	{
		// ȸ���� �� �ִٸ�(= �̵��� �� �ִٸ�)
		if (turn(c, r, move_y, move_x, d, map, back_y, back_x))
		{
			// �̵��Ѵ�.
			c += move_y;
			r += move_x;

			map[c][r] = 2;
			clean_n++;
			cout<<c<<" "<<r<<endl;
		}
		// ����� �����ְų� û�ҵǾ� �ִٸ�
		else
		{
			// �����Ѵ�.
			if (!oversize(c + back_y, r + back_x, map))
			{
				c += back_y;
				r += back_x;
			}
			// ������ �ϸ� �ʿ��� ����Ƿ� ���� ����.
			else
				break;
		}
	}

	cout << clean_n << endl;

}

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int N, K;
int alp[26] = { 0 };
vector<string> words;
int ans = 0;

int CalCanReadWord()
{
	vector<int> read(words.size(), 1);

	for (int i = 0; i < words.size(); i++)
	{
		string s = words[i];

		for (int j = 0; j < s.length(); j++)
		{
			char ch = s[j];
			int a = int(ch);
			if (alp[ch-'a'] == 0)
			{
				read[i] = 0;
				break;
			}
		}
	}

	return count(read.begin(), read.end(), 1);
}

void Dfs(int cnt, int now)
{
	if (cnt == K)
	{
		int num = CalCanReadWord();
		ans = max(ans, num);
		return;
	}
	
	for (int i = now; i < 26; i++)
	{
		if (alp[i] == 1) continue;

		alp[i] = 1;
		Dfs(cnt + 1, i + 1);
		alp[i] = 0;
	}

}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N >> K;
	K -= 5;

	alp['a' - 'a'] = 1;
	alp['n' - 'a'] = 1;
	alp['t' - 'a'] = 1;
	alp['i' - 'a'] = 1;
	alp['c' - 'a'] = 1;


	for (int i = 0; i < N; i++)
	{
		string s;
		cin >> s;
		s = s.substr(4, s.length() - 4);
		s = s.substr(0, s.length() - 4);

		words.push_back(s);
	}

	if (K < 0)
	{
		cout << 0;
		return 0;
	}

	Dfs(0, 0);

	cout << ans;




	
}
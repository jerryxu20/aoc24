#include <bits/stdc++.h>
using namespace std;

#define sz(x) (int)(x).size()
typedef pair<int, int> pi;


vector<string> grid;
vector<pi> delta = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
int n, m;
vector<vector<int>> bfs(pi s) {
    queue<pi> q;
    q.push({s.first, s.second});

    vector<vector<int>> ans(n, vector<int>(m, -1));
    ans[s.first][s.second] = 0;

    int d = 0;
    while(sz(q)) {
        int z = sz(q);
        while(z--) {
            auto [i, j] = q.front();
            q.pop();

            if (grid[i][j] == '#') continue;
            for (auto &[a, b]: delta) {
                int ii = i + a;
                int jj = j + b;
                if (ii < 0 || jj < 0 || ii >= n || jj >= m) continue;

                if (ans[ii][jj] == -1) {
                    ans[ii][jj] = d + 1;
                    q.push({ii, jj});
                }
            }
        }
        d++;
    }
    return ans;
}

void solve() {
    n = grid.size();
    m = grid[0].size();

    pi s, t;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'S') {
                s = {i, j};
            }
            if (grid[i][j] == 'E') {
                t = {i, j};
            }
        } 
    }

    vector<vector<int>> from_s = bfs(s);
    vector<vector<int>> to_t = bfs(t);
    int best = from_s[t.first][t.second];
    int ans = 0;
    cout << best << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) if (grid[i][j] != '#' && from_s[i][j] != -1) {
            for (int di = -2; di <= 2; di++) {
                for (int dj = -2; dj <= 2; dj++) if (abs(di) + abs(dj) <= 2) {
                    int ii = i + di;
                    int jj = j + dj;
                    if (ii < 0 || jj < 0 || ii >= n || jj >= m) continue;
                    if (grid[ii][jj] == '#' || to_t[ii][jj] == -1) continue;
                    int cand = from_s[i][j] + to_t[ii][jj] + 2;
                    if (cand <= best - 100) {
                        ans++;
                    }
                }
            }
        }
    }

    cout << ans << endl;
}


int main() {
    string s;
    while(cin >> s) {
        grid.push_back(s);
    }
    solve();
}
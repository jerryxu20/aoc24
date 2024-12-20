#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;
typedef tuple<int, int, int, int, int> ent;
typedef tuple<int, int, int> ti;


vector<string> grid;
vector<pi> delta = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
int n, m;
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


    priority_queue<ent, vector<ent>, greater<ent>> pq;


    auto id = [&] (int i, int j) {
        return i * m + j;
    };

    vector<vector<int>> dis(n * m, vector<int>(4, INT_MAX));
    dis[id(s.first, s.second)][0] = 0;
    pq.push(ent{0, s.first, s.second, delta[0].first, delta[0].second});

    
    
    while(!pq.empty()) {
        auto [d, i, j, di, dj] = pq.top();
        pq.pop();
        // cout << i << " " << j << " " << di << " " << dj << " cost " << d << endl; 
        if (pi(i, j) == t) {
            cout << d << endl;
            return;
        }

        // rotate
        for (int k = 0; k < 4; k++) {
            pi dir = delta[k];
            if (dir == pi(-di, -dj)) continue;
            int cand = d + 1000;
            if (cand < dis[id(i, j)][k]) {
                pq.push(ent{cand, i, j, dir.first, dir.second});
                dis[id(i, j)][k] = cand;
            }
        }

        // forward
        int ii = i + di;
        int jj = j + dj;
        if (ii < 0 || jj < 0 || ii >= n || jj >= m) continue;
        if (grid[ii][jj] == '#') continue;
        int cand = d + 1;

        int k;
        for (int kk = 0; kk < 4; kk++) if (delta[kk] == pi(di, dj)) {
            k = kk;
        }


        if (cand < dis[id(ii, jj)][k]) {
            pq.push(ent{cand, ii, jj, di, dj});
            dis[id(ii, jj)][k] = cand;
        }

    }

    return;
}


int main() {
    string s;
    while(cin >> s) {
        grid.push_back(s);
    }
    solve();
}
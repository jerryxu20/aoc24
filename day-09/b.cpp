#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pi;
typedef tuple<int, int, int> ti;
typedef long long ll;
#define rep(i, a, b) for (int i=a; i<(b); i++)


#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

int solve() {
    string s; cin >> s;

    int n = sz(s);
    vector<pi> space;
    vector<ti> files;
    int N = 0;
    int tot = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 1) {
            space.pb({tot, tot + s[i] - '0' - 1});
        } else {
            files.pb({tot, s[i] - '0', N++});
        }
        tot += s[i] - '0';
    }


    reverse(all(files));
    vector<ti> placed;
    for (auto [s, len, id]: files) {
        space.pb({s, s + len - 1});
        bool found = false;
        for (auto &[a, b]: space) if (a < s) {
            if (b - a + 1 >= len) {
                placed.pb({a, a + len - 1, id});
                a += len;
                found = true;
                break;
            }
        }
        if (!found) {
            placed.pb({s, s + len - 1, id});
        }
    }

    ll ans = 0;
    for (auto &[s, t, id]: placed) {
        for (int i = s; i <= t; i++) {
            ans += i * id;
        }
    }
    cout << ans << endl;
    return 0;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    solve();
    return 0;
}
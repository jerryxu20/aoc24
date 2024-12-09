#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;

#define rep(i, a, b) for (int i=a; i<(b); i++)

#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define pb push_back

int solve() {
    string s; cin >> s;

    int n = sz(s);
    int tot = 0;
    
    vi ans;
    int N = 0;
    for (int i = 0; i < n; i++) {
        int k = s[i] - '0';
        tot += k;
        if (i % 2 == 0) {
            int id = N++;
            while(k--) {
                ans.pb(id);
            }
        } else {
            while(k--) {
                ans.pb(-1);
            }
        }
    }

    for (int i = tot - 1; i >= 0; i--) {
        if (ans[i] != -1) {
            int id = ans[i];
            ans[i] = -1;
            rep(j, 0, tot) {
                if (ans[j] == -1) {
                    ans[j] = id;
                    break;
                }
            }
        }
    }

    ll res = 0;
    for (int i = 0; i < tot; i++) {
        if (ans[i] != -1) {
            res += i * ans[i];
        }
    }
    cout << res << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    solve();
    return 0;
}
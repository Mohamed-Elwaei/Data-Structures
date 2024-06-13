
#include <iostream>
#include <vector>
#include <bit>
using namespace std;
#define lli  long long int
int n,q;
vector<lli> F;
vector<lli> V;

void add(lli d, lli i){
    
    while (i <= n){
        F[i] += d;
        i += i & -i;
    }
    
}
lli sum(lli i){
    lli s = 0LL;
    
    while (i > 0) {
        s += F[i];
        i -= i & -i;
    }
    return s;
}



/*
 1-indexed fenwick tree.
 */

int main(){
    cin >> n >> q;
    F.resize(n+1,0);
    V.resize(n);
    
    for (int i = 1; i <= n; i++){
        cin >> V[i-1];
        add( V[i-1],i);
    }
    
    while (q--){
        int t; cin >> t;
        
        if (t == 1){
            int k,u; cin >> k >> u;
            add(u - V[k-1], k);
            V[k-1] = u;
        }
        else {
            int a,b; cin >> a >> b;
            cout << sum(b) - sum(a-1) << "\n";
        }
    }
}

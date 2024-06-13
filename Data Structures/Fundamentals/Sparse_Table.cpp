#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class SparseTable {
private:
    vector<vector<int> > st; // 2D vector to store sparse table
    vector<int> arr; // Input array
    int n; // Size of the input array
    int k; // Number of rows in the sparse table

public:
    SparseTable(const vector<int>& input) {
        arr = input;
        n = arr.size();
        k = log2(n) + 1;
        st.resize(n, vector<int>(k));

        build();
    }

    void build() {
        for (int i = 0; i < n; i++) {
            st[i][0] = arr[i]; // Fill the first column of the sparse table with the input array elements
        }

        for (int j = 1; j < k; j++) {
            for (int i = 0; i <= n - (1 << j); i++) {
                // Compute the value for the current cell by combining the values from the previous two cells
                st[i][j] = combine(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }
    }

    int query(int left, int right) {
        int j = log2(right - left + 1);
        return combine(st[left][j], st[right - (1 << j) + 1][j]);
    }

    int combine(int a, int b) {
        return min(a, b); // Change this function according to your requirements
    }
};

int main() {
    vector<int> arr = {7, 2, 3, 0, 5, 8, 1};
    SparseTable sparseTable(arr);

    // Query the minimum value between indices 2 and 5 (inclusive)
    int minValue = sparseTable.query(2, 5);
    cout << minValue << endl; // Output: 0

    return 0;
}

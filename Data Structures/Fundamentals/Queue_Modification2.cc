#include <iostream>
#include <deque>

int main() {
    std::deque<std::pair<int, int> > q;
    int cnt_added = 0;
    int cnt_removed = 0;

    // Adding elements to the deque
    q.push_back(std::make_pair(5, cnt_added));
    cnt_added++;
    q.push_back(std::make_pair(2, cnt_added));
    cnt_added++;
    q.push_back(std::make_pair(7, cnt_added));
    cnt_added++;
    q.push_back(std::make_pair(1, cnt_added));
    cnt_added++;
    q.push_back(std::make_pair(3, cnt_added));
    cnt_added++;

    // Finding the minimum value
    int minimum = q.front().first;
    std::cout << "Minimum value: " << minimum << std::endl;

    // Adding a new element
    int new_element = 4;
    while (!q.empty() && q.back().first > new_element)
        q.pop_back();
    q.push_back(std::make_pair(new_element, cnt_added));
    cnt_added++;

    // Removing an element
    if (!q.empty() && q.front().second == cnt_removed) {
        q.pop_front();
    }
    cnt_removed++;

    // Displaying the updated deque
    std::cout << "Updated deque: ";
    for (const auto& element : q) {
        std::cout << "(" << element.first << ", " << element.second << ") ";
    }
    std::cout << std::endl;

    return 0;
}

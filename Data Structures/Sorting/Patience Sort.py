from bisect import bisect_left

def patience_sort(deck):
    piles = []  # Initialize an empty list to represent piles of cards

    for card in deck:
        # Find the index of the leftmost pile where the current card can be placed
        pile_index = bisect_left([pile[-1] for pile in piles], card)

        # If there's no pile where the card can be placed, create a new pile
        if pile_index == len(piles):
            piles.append([card])
        else:
            # Place the card in the appropriate pile
            piles[pile_index].append(card)

    # Merge the piles into a single sorted list
    sorted_deck = []
    while piles:
        smallest_pile_index = min(range(len(piles)), key=lambda i: piles[i][-1])
        smallest_pile = piles.pop(smallest_pile_index)
        sorted_deck.append(smallest_pile.pop())

        if smallest_pile:
            piles.append(smallest_pile)

    return sorted_deck


from bisect import bisect_left

def longest_increasing_subsequence(arr):
    piles = []  # Initialize an empty list to represent piles of cards

    for num in arr:
        pile_index = bisect_left([pile[-1] for pile in piles], num)
        if pile_index == len(piles):
            piles.append([num])
        else:
            piles[pile_index].append(num)

    # Reconstruct the longest increasing subsequence
    lis = []
    index = len(piles) - 1
    max_pile_index = len(piles) - 1

    while max_pile_index >= 0:
        lis.append(piles[max_pile_index][-1])
        while index >= 0 and piles[max_pile_index][-1] <= arr[index]:
            index -= 1
        max_pile_index = index

    return lis[::-1]

# Example usage:
arr = [3, 4, -1, 0, 6, 2, 3]
lis = longest_increasing_subsequence(arr)
print(lis)



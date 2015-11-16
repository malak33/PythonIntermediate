from collections import Counter

items = [1, 2, 3, 4, 5, 4, 4, 3, 4, 5, 2, 0, 7, 4, 5, 6]

most_common = Counter(items).most_common(1)             # 1 defines how many of the "mosts" to return

most, num_occurrences = most_common[0]                  # each returned "most" is a tuple of two values: most, num_occurrences

print(most, num_occurrences)

print(Counter(items).most_common(2))                    # [(4, 5), (5, 3)]
groceries: dict[str, int] = {}

# // Infinite to get the items
while 1:
    try:
        item: str = input()

        # // If the item doesn't already exist in
        # // the map storage, create a new key
        if item not in groceries:
            groceries[item] = 0

        # // Increase the item value
        groceries[item] += 1
    except EOFError:
        break

# // Convert the keys to a list
keys: list[str] = list(groceries.keys())
# // Sort the keys alphabetically
keys.sort()

# // Iterate over the grocery items
for k in keys:
    print(f"{groceries[k]} {k.upper()}")


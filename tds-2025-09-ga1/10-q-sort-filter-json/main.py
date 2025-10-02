import json

# Step 1: Load JSON
with open("products.json") as f:
    products = json.load(f)

# Step 2: Define sorting options
# 'asc' = ascending, 'desc' = descending
sort_by = {"category": "asc", "price": "desc", "name": "asc"}

price_threshold = 112.39

# Step 3: Filter products by price
filtered = [p for p in products if p.get("price", 0) >= price_threshold]


# Step 4: Define a dynamic sort key
def sort_key(x):
    keys = []
    for field, order in sort_by.items():
        value = x.get(field)
        # For descending order, negate numeric values
        if isinstance(value, (int, float)) and order == "desc":
            value = -value
        # For strings descending, reverse by prepending a character to invert sort order
        elif isinstance(value, str) and order == "desc":
            value = "".join(chr(255 - ord(c)) for c in value)
        keys.append(value)
    return tuple(keys)


# Step 5: Sort the filtered products
sorted_products = sorted(filtered, key=sort_key)

# Step 6: Save minified JSON
with open("sorted_filtered_products.json", "w") as f:
    json.dump(sorted_products, f, separators=(",", ":"))

print("Done! Minified JSON saved to 'sorted_filtered_products.json'.")

# 10. Sort and Filter a JSON Product Catalog (1 Marks)

## **Step 1: Save your JSON array**

* Copy the JSON array you provided into a file called `products.json`.

Example structure:

```json
[{"category":"Apparel","price":65.01,"name":"Eco Kit"}, {"category":"Home","price":123.53,"name":"Ultra Kit"}, ... ]
```

---

## **Step 2: Change the sorting options and price threshold**

```python
sort_by = {
    "category": "asc",
    "price": "desc",
    "name": "asc"
}

price_threshold = 112.39
```

---

## **Step 3: Run the script**

In terminal:

```bash
python main.py
```

---

## **Step 4: Output**

* The code will save a **single-line JSON string** (minified) in the file `sorted_filtered_products.json`.

* Copy this entire line to submit.

---

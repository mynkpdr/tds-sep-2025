# 7. Embedding Similarity (0.5 Marks)

## 1. Problem Description

Write a Python function `most_similar` that takes a dictionary of text phrases and their corresponding numerical "embedding" vectors. The function must return the two phrases that are most semantically similar by comparing their embeddings.

---

## 2. Requirements

- **Function Signature**: `def most_similar(embeddings):`
- **Input**: Dictionary with keys as strings (phrases) and values as lists of floats (embedding vectors).
- **Logic**: Compute cosine similarity for every pair of embeddings.
- **Output**: A `tuple` of the two phrases with the highest similarity.

---

## 3. Step-by-Step Solution

1. **Define Function**: `most_similar` with `embeddings` argument.
2. **Import NumPy** for vector calculations.
3. **Initialize Variables**:

   ```python
   max_similarity = -1.0
   most_similar_pair = (None, None)
   phrases = list(embeddings.keys())
   ```

4. **Iterate Through Unique Pairs**:

   ```python
   for i in range(len(phrases)):
       for j in range(i + 1, len(phrases)):
           # compare phrases[i] and phrases[j]
   ```

5. **Compute Cosine Similarity**:

   ```python
   vec1 = np.array(embeddings[phrases[i]])
   vec2 = np.array(embeddings[phrases[j]])
   similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
   ```

6. **Update Maximum**:

   ```python
   if similarity > max_similarity:
       max_similarity = similarity
       most_similar_pair = (phrases[i], phrases[j])
   ```

7. **Return Result**:

   ```python
   return most_similar_pair
   ```

---

## 4. Complete Python Code

```python
import numpy as np
from itertools import combinations

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def most_similar(embeddings):
    max_similarity = -1.0
    most_similar_pair = (None, None)

    for phrase1, phrase2 in combinations(embeddings.keys(), 2):
        sim = cosine_similarity(embeddings[phrase1], embeddings[phrase2])
        if sim > max_similarity:
            max_similarity = sim
            most_similar_pair = (phrase1, phrase2)

    return most_similar_pair
```

---

## 5. Verification

The exam platform will automatically call `most_similar` with a dictionary of embeddings and check if the returned tuple matches the correct pair of phrases.

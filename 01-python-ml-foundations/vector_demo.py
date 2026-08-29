import numpy as np

vector_one = np.array([1.0, 2.0, 3.0])
vector_two = np.array([4, 5, 6])

vector_addition = vector_one + vector_two
vector_multiplication = vector_one * vector_two
vector_dot_product = np.dot(vector_one, vector_two)

magnitude_vector_one = np.linalg.norm(vector_one)
magnitude_vector_two = np.linalg.norm(vector_two)

cosine_similarity = (vector_dot_product / (magnitude_vector_one * magnitude_vector_two))

print("****************Start*********************************")

print("Vector One: ", vector_one)
print("Vector Two: ", vector_two)
print("Vector addition: ", vector_addition)
print("Vector Multiplication: ", vector_multiplication)
print("Vector Dot Product: ", vector_dot_product)
print("Vector Magnitude Vector One: ", magnitude_vector_one)
print("Vector Magnitude Vector Two: ", magnitude_vector_two)
print("Cosine Similarity: ", cosine_similarity)

print("****************End*********************************")

"""
For embeddings, this is the fundamental idea:

similar meaning
      ↓
similar vector direction
      ↓
high cosine similarity

and:

different meaning
      ↓
different vector direction
      ↓
lower cosine similarity
"""

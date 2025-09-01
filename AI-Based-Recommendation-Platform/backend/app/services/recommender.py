from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Recommender:
    def __init__(self, item_features):
        self.item_features = item_features

    def recommend(self, item_id, top_n=5):
        if item_id not in self.item_features:
            return []

        # Get the feature vector for the specified item
        item_vector = self.item_features[item_id].reshape(1, -1)

        # Calculate cosine similarity between the specified item and all other items
        similarities = cosine_similarity(item_vector, self.item_features)

        # Get the indices of the top_n most similar items
        similar_indices = similarities.argsort()[0][-top_n-1:-1][::-1]

        # Return the recommended item IDs
        return [list(self.item_features.keys())[i] for i in similar_indices]

# Example usage:
# item_features = {
#     'item1': np.array([1, 0, 0]),
#     'item2': np.array([0, 1, 0]),
#     'item3': np.array([0, 0, 1]),
#     'item4': np.array([1, 1, 0]),
# }
# recommender = Recommender(item_features)
# recommendations = recommender.recommend('item1')
# print(recommendations)  # Output: ['item4', 'item2', 'item3']
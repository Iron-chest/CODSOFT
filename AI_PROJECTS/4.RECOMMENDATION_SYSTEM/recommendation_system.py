import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Create sample movie rating data
np.random.seed(42)

# Generate synthetic user-movie rating data
n_users = 100
n_movies = 50
n_ratings = 1000

# Create random user IDs and movie IDs
user_ids = np.random.randint(1, n_users + 1, n_ratings)
movie_ids = np.random.randint(1, n_movies + 1, n_ratings)

# Generate ratings with some underlying patterns
# Users 1-33 tend to rate action movies (1-17) higher
# Users 34-66 tend to rate drama movies (18-34) higher
# Users 67-100 tend to rate comedy movies (35-50) higher
ratings = []
for user, movie in zip(user_ids, movie_ids):
    base_rating = np.random.normal(3.5, 0.5)
    
    if user <= 33 and movie <= 17:
        # Action fans rating action movies
        rating = base_rating + np.random.normal(1, 0.3)
    elif 34 <= user <= 66 and 18 <= movie <= 34:
        # Drama fans rating drama movies
        rating = base_rating + np.random.normal(1, 0.3)
    elif user >= 67 and movie >= 35:
        # Comedy fans rating comedy movies
        rating = base_rating + np.random.normal(1, 0.3)
    else:
        # Rating movies outside their preferred genre
        rating = base_rating - np.random.normal(0.5, 0.3)
    
    ratings.append(min(max(rating, 1), 5))  # Clamp ratings between 1 and 5

# Create a DataFrame with the ratings
ratings_df = pd.DataFrame({
    'user_id': user_ids,
    'movie_id': movie_ids,
    'rating': ratings
})

class MatrixFactorizationRecommender:
    def __init__(self, n_factors=20, learning_rate=0.01, regularization=0.01):
        """
        Initialize the recommender system
        
        Parameters:
        n_factors: Number of latent factors (taste dimensions)
        learning_rate: How quickly the model updates its beliefs
        regularization: How much to penalize complex solutions
        """
        self.n_factors = n_factors
        self.learning_rate = learning_rate
        self.regularization = regularization
        
    def fit(self, ratings_df, n_epochs=100):
        """
        Train the recommender system on rating data
        """
        # Get unique users and movies
        self.user_ids = ratings_df['user_id'].unique()
        self.movie_ids = ratings_df['movie_id'].unique()
        
        # Create mapping dictionaries
        self.user_map = {user_id: idx for idx, user_id in enumerate(self.user_ids)}
        self.movie_map = {movie_id: idx for idx, movie_id in enumerate(self.movie_ids)}
        
        # Initialize latent factors randomly
        self.user_factors = np.random.normal(0, 0.1, (len(self.user_ids), self.n_factors))
        self.movie_factors = np.random.normal(0, 0.1, (len(self.movie_ids), self.n_factors))
        
        # Train the model
        for epoch in range(n_epochs):
            total_error = 0
            
            # Process each rating
            for _, row in ratings_df.iterrows():
                user_idx = self.user_map[row['user_id']]
                movie_idx = self.movie_map[row['movie_id']]
                rating = row['rating']
                
                # Predict rating
                prediction = np.dot(self.user_factors[user_idx], self.movie_factors[movie_idx])
                error = rating - prediction
                total_error += error ** 2
                
                # Update factors
                user_factors_update = error * self.movie_factors[movie_idx] - self.regularization * self.user_factors[user_idx]
                movie_factors_update = error * self.user_factors[user_idx] - self.regularization * self.movie_factors[movie_idx]
                
                self.user_factors[user_idx] += self.learning_rate * user_factors_update
                self.movie_factors[movie_idx] += self.learning_rate * movie_factors_update
            
            # Print progress every 10 epochs
            if (epoch + 1) % 10 == 0:
                rmse = np.sqrt(total_error / len(ratings_df))
                print(f"Epoch {epoch + 1}/{n_epochs}, RMSE: {rmse:.4f}")
    
    def recommend_movies(self, user_id, n_recommendations=5):
        """
        Recommend movies for a specific user
        """
        if user_id not in self.user_map:
            raise ValueError("User not found in training data")
        
        user_idx = self.user_map[user_id]
        
        # Calculate predicted ratings for all movies
        predictions = np.dot(self.movie_factors, self.user_factors[user_idx])
        
        # Get top movie indices
        top_movie_indices = np.argsort(predictions)[::-1][:n_recommendations]
        
        # Convert back to movie IDs and include predicted ratings
        recommendations = []
        for idx in top_movie_indices:
            movie_id = self.movie_ids[idx]
            predicted_rating = predictions[idx]
            recommendations.append((movie_id, predicted_rating))
        
        return recommendations

# Split data into training and testing sets
train_df, test_df = train_test_split(ratings_df, test_size=0.2, random_state=42)

# Create and train the recommender
recommender = MatrixFactorizationRecommender(n_factors=20)
recommender.fit(train_df)

# Get recommendations for different types of users
print("\nRecommendations for different user types:")
print("\nAction fan (User 1):")
recommendations = recommender.recommend_movies(1)
for movie_id, rating in recommendations:
    print(f"Movie {movie_id}: Predicted rating = {rating:.2f}")

print("\nDrama fan (User 50):")
recommendations = recommender.recommend_movies(50)
for movie_id, rating in recommendations:
    print(f"Movie {movie_id}: Predicted rating = {rating:.2f}")

print("\nComedy fan (User 100):")
recommendations = recommender.recommend_movies(100)
for movie_id, rating in recommendations:
    print(f"Movie {movie_id}: Predicted rating = {rating:.2f}")

# Calculate test set RMSE
test_predictions = []
test_actual = []
for _, row in test_df.iterrows():
    if row['user_id'] in recommender.user_map and row['movie_id'] in recommender.movie_map:
        user_idx = recommender.user_map[row['user_id']]
        movie_idx = recommender.movie_map[row['movie_id']]
        prediction = np.dot(recommender.user_factors[user_idx], recommender.movie_factors[movie_idx])
        test_predictions.append(prediction)
        test_actual.append(row['rating'])

test_rmse = np.sqrt(np.mean(np.array(test_predictions) - np.array(test_actual)) ** 2)
print(f"\nTest Set RMSE: {test_rmse:.4f}")
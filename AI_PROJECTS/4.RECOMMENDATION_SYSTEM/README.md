# Hybrid Recommendation System

A sophisticated recommendation engine that combines collaborative and content-based filtering approaches to provide personalized recommendations to users. This system can be used for recommending various items such as movies, books, products, or any items with user ratings and content features.

## Features

The recommendation system incorporates multiple advanced features to provide accurate and personalized recommendations:

- Hybrid approach combining collaborative and content-based filtering
- Configurable weights for different recommendation strategies
- Sophisticated similarity metrics for both users and items
- Rating normalization to handle different rating scales
- Efficient handling of cold start problems for new users or items
- Customizable number of recommendations
- Support for item features and user ratings

## Installation

To use this recommendation system, you'll need Python 3.7+ and several dependencies. You can install the required packages using pip:

```bash
pip install numpy scipy scikit-learn
```

## Usage

Here's a complete example of how to use the recommendation system:

```python
from recommender import HybridRecommender

# Initialize the recommender system
recommender = HybridRecommender(rating_weight=0.7, content_weight=0.3)

# Add some user ratings
recommender.add_user_rating("user1", "movie1", 5)
recommender.add_user_rating("user1", "movie2", 3)
recommender.add_user_rating("user2", "movie1", 4)
recommender.add_user_rating("user2", "movie3", 2)

# Add item features
recommender.add_item_features("movie1", {
    "genre": "action",
    "year": "2020",
    "director": "John Doe"
})
recommender.add_item_features("movie2", {
    "genre": "comedy",
    "year": "2019",
    "director": "Jane Smith"
})
recommender.add_item_features("movie3", {
    "genre": "drama",
    "year": "2021",
    "director": "Bob Wilson"
})

# Get recommendations for a user
recommendations = recommender.get_recommendations("user1", n=5)

# Print recommendations
for item_id, predicted_rating in recommendations:
    print(f"Recommended item: {item_id}, Predicted rating: {predicted_rating:.2f}")
```

## How It Works

The system uses a sophisticated hybrid approach to generate recommendations:

### Collaborative Filtering Component

The collaborative filtering component analyzes patterns in user ratings to find similarities between users. It:

1. Calculates user similarity using correlation between rating patterns
2. Identifies users with similar taste preferences
3. Predicts ratings based on how similar users rated items
4. Normalizes ratings to account for different rating scales

### Content-Based Filtering Component

The content-based component analyzes item features to find similar items. It:

1. Processes item features to create feature vectors
2. Calculates item similarity using Jaccard similarity
3. Predicts ratings based on similarity to items the user has rated
4. Considers all available item features for similarity calculation

### Hybrid Combination

The system combines both approaches using configurable weights:

1. Gets predictions from both collaborative and content-based components
2. Applies weights to each prediction (default: 70% collaborative, 30% content-based)
3. Combines predictions into a final recommendation score
4. Ranks items based on their final scores

## API Reference

### HybridRecommender Class

```python
class HybridRecommender:
    def __init__(self, rating_weight=0.7, content_weight=0.3):
        """
        Initialize the recommender system.
        
        Parameters:
            rating_weight (float): Weight for collaborative filtering (0 to 1)
            content_weight (float): Weight for content-based filtering (0 to 1)
        """

    def add_user_rating(self, user_id, item_id, rating):
        """
        Add a user rating to the system.
        
        Parameters:
            user_id: Unique identifier for the user
            item_id: Unique identifier for the item
            rating: Numerical rating (e.g., 1-5)
        """

    def add_item_features(self, item_id, features):
        """
        Add content features for an item.
        
        Parameters:
            item_id: Unique identifier for the item
            features: Dictionary of feature names and values
        """

    def get_recommendations(self, user_id, n=5):
        """
        Get top N recommendations for a user.
        
        Parameters:
            user_id: Unique identifier for the user
            n: Number of recommendations to return
            
        Returns:
            list: Top N recommended items with predicted ratings
        """
```

## Performance Optimization

To optimize the system's performance:

1. Use efficient data structures for storing ratings and features
2. Implement caching for similarity calculations
3. Use sparse matrices for large-scale applications
4. Normalize ratings to improve prediction accuracy
5. Balance weights based on your specific use case

## Contributing

Contributions are welcome! Here are some ways you can contribute to this project:

1. Report bugs
2. Suggest new features
3. Add documentation
4. Submit pull requests

Please feel free to open an issue or submit a pull request.

## Contact

For any questions or feedback, please open an issue in the GitHub repository.

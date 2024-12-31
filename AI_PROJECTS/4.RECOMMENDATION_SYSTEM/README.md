# Movie Recommendation System

## Overview
This project implements a simple movie recommendation system using collaborative filtering techniques. The recommender predicts user preferences based on past ratings and recommends movies tailored to individual tastes.

### Key Features
- **Matrix Factorization**: Utilizes latent factors to model user and movie preferences.
- **Synthetic Data Simulation**: Generates user-movie rating data with predefined patterns for action, drama, and comedy genres.
- **Training and Evaluation**: Supports training on user-provided datasets and evaluates performance using RMSE.
- **Personalized Recommendations**: Provides top movie suggestions for specific users.

---

## Project Structure
```
📂 Movie Recommendation System
├── data
│   └── ratings_data.csv       # Synthetic user-movie rating data
├── src
│   ├── recommender.py         # Matrix factorization implementation
│   └── data_processing.py     # Synthetic data generation
├── notebooks
│   └── analysis.ipynb         # Notebook for experimentation and visualization
└── README.md                  # Project documentation
```

---

## Dependencies
- Python >= 3.8
- Libraries:
  - numpy
  - pandas
  - scikit-learn

To install dependencies, run:
```bash
pip install -r requirements.txt
```

---

## How It Works
### Data Generation
The system generates synthetic user-movie rating data:
- **Users**: 100 users split into three preference groups (Action, Drama, Comedy).
- **Movies**: 50 movies categorized by genre.
- **Ratings**: Derived from user preferences with noise for realism.

### Model Training
Matrix Factorization is applied to learn latent factors for users and movies. The system:
- Maps users and movies to lower-dimensional vectors.
- Adjusts vectors iteratively to minimize prediction errors using stochastic gradient descent.

### Recommendation
For a given user, the recommender predicts ratings for all movies and ranks them. Top movies are recommended based on predicted scores.

---

## Usage
### Training
Train the recommender on the synthetic dataset:
```python
from src.recommender import MatrixFactorizationRecommender

recommender = MatrixFactorizationRecommender(n_factors=20)
recommender.fit(train_df)
```

### Getting Recommendations
Retrieve recommendations for a specific user:
```python
recommendations = recommender.recommend_movies(user_id=1, n_recommendations=5)
for movie_id, predicted_rating in recommendations:
    print(f"Movie {movie_id}: Predicted rating = {predicted_rating:.2f}")
```

---

## Results
### RMSE on Synthetic Data
- **Training Set RMSE**: Tracked during training.
- **Test Set RMSE**:  Measures accuracy of predictions on unseen data.

### Example Recommendations
#### Action Fan (User 1)
- Movie 10: Predicted Rating = 4.75
- Movie 3: Predicted Rating = 4.65

#### Drama Fan (User 50)
- Movie 20: Predicted Rating = 4.85
- Movie 25: Predicted Rating = 4.70

#### Comedy Fan (User 100)
- Movie 40: Predicted Rating = 4.90
- Movie 45: Predicted Rating = 4.80

---

## Evaluation
Test RMSE is calculated to assess the system's performance on unseen data:
```python
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(test_actual, test_predictions))
print(f"Test RMSE: {rmse:.4f}")
```

---

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.



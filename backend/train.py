import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
import os

# Load dataset
dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'crop_recommendation.csv')
data = pd.read_csv(dataset_path)

# Prepare data
X = data.drop('Crop', axis=1)
y = data['Crop']

# Train model
model = RandomForestClassifier(
    n_estimators=100,  # Increase number of estimators for better generalization
    max_depth=10,      # Limit the depth of trees
    min_samples_split=5,  # Minimum samples to split an internal node
    min_samples_leaf=2,   # Minimum samples at a leaf node
    max_features='sqrt',  # Consider sqrt(number of features) at each split
    random_state=0
)
model.fit(X, y)

# Save the model
model_path = os.path.join(os.path.dirname(__file__), 'crop_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

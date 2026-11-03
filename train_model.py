import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset/emails.csv")

# Input and output
X = data["email"]
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Create machine learning model
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("AI PHISHING EMAIL DETECTOR")
print("--------------------------")
print("Training completed successfully!")
print("Test accuracy:", round(accuracy * 100, 2), "%")

# Save model
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/phishing_model.pkl")

print("Model saved successfully!")
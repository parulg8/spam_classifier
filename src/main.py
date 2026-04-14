import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv('../data/spam.csv', sep='\t', names=['label', 'message'], encoding='latin-1')

# Convert labels to numbers
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

# Convert text to numbers
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict
y_pred = model.predict(X_test_vec)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Test custom input
sample = ["Congratulations! You won a free ticket"]
sample_vec = vectorizer.transform(sample)
prediction = model.predict(sample_vec)

if prediction[0] == 1:
    print("This message is: SPAM")
else:
    print("This message is: NOT SPAM")

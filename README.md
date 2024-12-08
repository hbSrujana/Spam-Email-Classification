# Spam Email Classification

## Description
This project uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to classify emails as **Spam** or **Ham**. It includes data preprocessing, model training, evaluation, and a web-based deployment using **Streamlit**.

---

## Features
- Preprocesses email content for classification.
- Classifies emails as spam or ham with a trained machine learning model.
- Provides a user-friendly web interface for real-time email classification.

---

## How It Works

### Step 1: Data Collection and Preprocessing
- Load the dataset and clean the data by removing unnecessary columns and handling null values.
- Map labels (`ham` and `spam`) to numerical values for machine learning.

### Step 2: Feature Engineering
- Convert email text into numerical features using **CountVectorizer** (bag-of-words approach).

### Step 3: Model Selection
- The **Multinomial Naive Bayes** algorithm is used for its efficiency in text classification tasks.

### Step 4: Model Training
- Train the Naive Bayes model using the preprocessed and vectorized data.

### Step 5: Evaluation
- Evaluate the model's accuracy on a test dataset.

### Step 6: Deployment
- Save the trained model and vectorizer using **Pickle**.
- Build and deploy the classification interface using **Streamlit**.

Run the app with the following command:
```
streamlit run SpamDetect.py




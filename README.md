#  Spam Email Classifier

##  Objective
The objective of this project is to build a simple machine learning model that can classify messages as **Spam** or **Not Spam (Ham)**.  
This project helps in understanding the basics of text classification and supervised learning.

---

##  Dataset
- **Name:** SMS Spam Collection Dataset  
- The dataset contains labeled messages:
  - `spam` → unwanted messages  
  - `ham` → normal messages  

---

##  Approach
The project follows a basic Natural Language Processing (NLP) pipeline:

1. Convert text data into numerical format using **CountVectorizer**
2. Train a classification model using **Naive Bayes**
3. Evaluate model performance using accuracy score
4. Test the model on custom user input

---

##  Steps Performed
1. Imported required libraries (Pandas, Scikit-learn)
2. Loaded and cleaned the dataset
3. Converted labels (`spam`, `ham`) into numeric values
4. Split the dataset into training and testing sets
5. Transformed text data into vectors
6. Trained the model using Multinomial Naive Bayes
7. Evaluated the model using accuracy
8. Tested the model with custom input messages

---

##  Results
- Achieved an accuracy of approximately **99%**
- Model successfully classifies most messages correctly
- Custom inputs can also be tested in real-time

---

##  Difficulties Faced
- Errors while reading the dataset due to incorrect file format
- Column name mismatch in the dataset
- Understanding how text is converted into numerical form

---

##  Resolutions
- Used correct separator (`\t`) while loading dataset
- Assigned column names manually
- Studied how CountVectorizer works for text processing

---

##  Learnings
- Basics of **machine learning workflow**
- Difference between **training and testing data**
- Importance of **data preprocessing**
- Introduction to **text vectorization**
- Working with a classification algorithm (Naive Bayes)

---

##  Conclusion
This project demonstrates how machine learning can be used to solve real-world problems like spam detection.  
It also provides a strong foundation for exploring more advanced NLP and classification techniques.

---

##  How to Run This Project

###  Prerequisites

* IDE installed
* Python installed (3.x)
* Basic knowledge of Python

### Steps to Run
1. Clone the repository:

   ```
   git clone https://github.com/parulg8/spam_classifier.git
   ```
2. Navigate to the project folder:

   ```
   cd spam-classifier
   ```
3. Install Dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Run the script:

   ```
   python src/main.py
   ```

---

## Author
Parul Ghosh
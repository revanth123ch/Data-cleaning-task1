# Data-cleaning-task1
Forwarded from Chikkala Vennela (https://www.linkedin.com/in/ACoAAEdw0pwBqRO95zVJzFMQhAxX7QDnJZ5FJYU):
DATA-CLEANING
ML_TASK1_DATA-CLEANING
This project involves cleaning and preprocessing the Titanic dataset (titanic dataset.csv) using Python in Google Colab.

📄 Files Included
titanic datast.csv – Original dataset with raw passenger information
cleaned_titanic data.csv – Cleaned and preprocessed dataset
python code.py – Python code notebook used for preprocessing
🔧 Preprocessing Steps
Dropped Irrelevant Columns

Removed columns: PassengerId, Name, Ticket, Cabin
Handled Missing Values

Filled missing Age values with the median
Filled missing Embarked values with the most frequent value (mode)
Encoded Categorical Data

Converted Sex and Embarked columns to numeric form
Created New Feature (Optional)

Added FamilySize = SibSp + Parch
Exported Cleaned Dataset

Saved the cleaned data as cleaned_titanic data.csv

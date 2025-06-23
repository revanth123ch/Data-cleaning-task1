import pandas as pd
from IPython.display import display
def clean_titanic_dataset(csv_path):
    df = pd.read_csv(csv_path)
    zero_cols = [col for col in df.columns if col.startswith('zero')]
    df = df.drop(columns=zero_cols, errors='ignore') 
    df = df.rename(columns={'2urvived': 'Survived'})
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())
    if 'Fare' in df.columns:
        df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    if 'Pclass' in df.columns:
        df['Pclass'] = df['Pclass'].astype('category')
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].astype('category')
    if 'Survived' in df.columns:
         df['Survived'] = pd.to_numeric(df['Survived'], errors='coerce')
         df['Survived'] = df['Survived'].astype('Int64') 
    if 'SibSp' in df.columns and 'Parch' in df.columns:
        df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
        if 'FamilySize' in df.columns:
            df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    if 'Age' in df.columns:
        bins = [0, 12, 18, 30, 50, 100]
        labels = ['Child', 'Teenager', 'Young Adult', 'Adult', 'Senior']
    if 'Passengerid' in df.columns:
        df = df.drop(columns=['Passengerid'])

    print(f"\nNumber of duplicates before dropping: {df.duplicated().sum()}")
    df = df.drop_duplicates()
    print(f"Number of duplicates after dropping: {df.duplicated().sum()}")


    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    print("\nData types after cleaning:")
    print(df.dtypes)

    return df
cleaned_data = clean_titanic_dataset('Titanic-Dataset.csv')
cleaned_data.to_csv('cleaned_titanic_data.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_titanic_data.csv'")
print("\nFirst few rows of cleaned data:")
print(cleaned_data.head())
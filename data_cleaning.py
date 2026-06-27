import pandas as pd

# Load dataset
df = pd.read_csv("train.csv", encoding="latin1")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print(df.isnull().sum())

# Fill missing values only in text columns
text_cols = df.select_dtypes(include=['object']).columns
for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# Fill missing values only in numeric columns
num_cols = df.select_dtypes(include=['number']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

# Save summary report
summary = df.describe(include='all')

with pd.ExcelWriter("summary_report.xlsx") as writer:
    summary.to_excel(writer, sheet_name="Summary")

print("Data Cleaning Completed Successfully!")
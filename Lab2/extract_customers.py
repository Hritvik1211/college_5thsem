import pandas as pd

# Read the customers-100.csv file
df = pd.read_csv('customers-100.csv')

# Display the original data
print("Original data:")
print(df)
print("\n" + "="*50 + "\n")

# Extract only the specified columns: index, firstname, lastname, phone_number1
selected_columns = ['index', 'firstname', 'lastname', 'phone_number1']
extracted_df = df[selected_columns]

# Display the extracted data
print("Extracted data (index, firstname, lastname, phone_number1):")
print(extracted_df)
print("\n" + "="*50 + "\n")

# Display basic information about the extracted data
print("Data shape:", extracted_df.shape)
print("Column names:", list(extracted_df.columns))
print("Data types:")
print(extracted_df.dtypes)

# Save the extracted data to a new CSV file
extracted_df.to_csv('customers_extracted.csv', index=False)
print("\nExtracted data saved to 'customers_extracted.csv'")

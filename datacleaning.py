import pandas as pd

df = pd.read_csv("Dolche Vita Reviews.csv")

print(df.head())




#Replacing value like" 5 contributions" , "1 contribution", "19 contributions" etc,  with "Unknown" in location column
df['Location'] = df['Location'].fillna("Unknown").replace(regex=r'\d+ contributions?', value="Unknown")

df.to_csv('Dolche Vita Reviews.csv', index=False)

print(df['Location'].head())





# Convert the Date column to string and remove "Written " and bring in proper date format
df['Date'] = df['Date'].astype(str).str.replace("Written ", "", regex=False)


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


if df['Date'].isnull().any():
    print("There are some dates that could not be converted:")
    print(df[df['Date'].isnull()])

df.to_csv('Dolche Vita Reviews.csv', index=False)
print(df['Date'].head())


# Extracting the numeric rating from the 'Rating' column and convert it to a numeric type coulmn
df['Rating'] = df['Rating'].str.extract(r'(\d+\.?\d*)').astype(float)

df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

df.to_csv('Dolche Vita Reviews.csv', index=False)

print(df['Rating'].head())










import pandas as pd

dataset_name = ['bundesliga.csv', 'laliga.csv', 'ligue_1.csv', 'premier_league.csv', 'serie_A.csv']

dataframes = {}

for dataset in dataset_name:
    df = pd.read_csv(dataset)

    # I ran df.isna().sum() to detect the null values. Discovered some null values in the ref column in some of the csv_s
    df['ref'] = df['ref'].fillna('Unknown')

    cols_to_convert = ['home_team', 'away_team', 'winner', 'defeat', 'ref']
    for col in cols_to_convert:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()

    df.drop_duplicates(subset=['home_team', 'away_team'], keep='first', inplace=True)

    # Save the cleaned DataFrame to a new CSV file
    cleaned_filename = f"cleaned_{dataset}"
    df.to_csv(cleaned_filename, index=False)  # Save without the index column

    # Print confirmation
    print(f"Cleaned data saved to {cleaned_filename}")
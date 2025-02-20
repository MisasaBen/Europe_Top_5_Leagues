import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_data = ['cleaned_bundesliga.csv', 'cleaned_laliga.csv', 'cleaned_ligue_1.csv', 'cleaned_premier_league.csv', 'cleaned_serie_A.csv']
dfs = []
for csv in csv_data:
    df = pd.read_csv(csv)

    df['league'] = csv.replace('cleaned_', '').replace('_', ' ').replace('.csv', '').title()
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# combined_df.to_csv('combined_table.csv', index=False)
plt.figure(figsize=(12, 8))

sns.boxplot(x='league', y='goal_diff', data=combined_df, palette='Set2', hue='league')
plt.title('Goal Difference Distribution by League', fontsize=16, fontweight='bold')
plt.gcf().set_facecolor('lightgray')
plt.xlabel('League', fontsize=12, fontweight='bold')
plt.ylabel('Goal Difference', fontsize=12, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('GD_Distribution.png', dpi=300)
plt.show()


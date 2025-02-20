import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('combined_table.csv')

df['1st Half Goals'] = df['home_score_half_time'] + df['away_score_half_time']
df['2nd Half Goals'] = df['home_score_full_time'] + df['away_score_full_time'] - df['1st Half Goals']

# Melt the dataframe to have '1st Half Goals' and '2nd Half Goals' in a single column
melted_pd = pd.melt(df, id_vars=['league'], value_vars=['1st Half Goals', '2nd Half Goals'],
                    var_name='Half', value_name='Goals')

# Plotting the grouped barplot
plt.figure(figsize=(10, 6))
sns.barplot(x='league', y='Goals', hue='Half', data=melted_pd, palette='Set2')

# Customize plot
plt.title('Goals Scored in First and Second Halves by League', fontsize=16, fontweight='bold')
plt.xlabel('League', fontsize=12, fontweight='bold')
plt.ylabel('Goals Scored', fontsize=12, fontweight='bold')
plt.xticks(rotation=45)
plt.gcf().set_facecolor('lightblue')
plt.tight_layout()
plt.grid(axis='y', linestyle='--')
plt.savefig('1st_2nd_goals.png', dpi=300)

# Show plot
plt.show()
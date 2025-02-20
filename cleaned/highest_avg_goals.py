import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_data = ['cleaned_bundesliga.csv', 'cleaned_laliga.csv', 'cleaned_ligue_1.csv', 'cleaned_premier_league.csv', 'cleaned_serie_A.csv']
highest_avg_goals = []

for csv in csv_data:
    df = pd.read_csv(csv)

    goals_per_league = (df['home_score_full_time'].sum() + df['away_score_full_time'].sum()) / df.shape[0]

    league = csv.replace('cleaned_', '').replace('.csv', '').title().replace('_', ' ')

    highest_avg_goals.append([league, round(float(goals_per_league), 2)])

dataF = pd.DataFrame(highest_avg_goals, columns=['league', 'avg_goals_per_league'])
plt.figure(figsize=(10, 10))  # Increase the figure size (width, height)
sns.barplot(x='league', y='avg_goals_per_league', data=dataF, palette='viridis', hue='league', legend=False)

# Adding the values on top of each bar
for index, row in dataF.iterrows():
    plt.text(index, row['avg_goals_per_league'] + 0.02,  # Adjust the value placement
             round(row['avg_goals_per_league'], 2), ha='center', va='bottom', fontsize=10)

plt.title('Average Goals per League', fontsize=14, fontweight='bold', color='darkblue', pad = 20)
plt.xlabel('League', fontsize=14, fontweight='bold')
plt.gcf().set_facecolor('lightgrey')
plt.xticks(rotation=45, fontsize=10)
plt.ylabel('Average Goals', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('avg_goals_per_league.png', dpi = 300)
plt.show()

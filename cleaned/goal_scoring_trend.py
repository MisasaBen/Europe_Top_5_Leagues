import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('combined_table.csv')

goal_trend = []

# Standardize team names
df['home_team'] = df['home_team'].str.replace('1.', '').str.title()
df['away_team'] = df['away_team'].str.replace('1.', '').str.title()

for team in df['home_team'].unique():
    match_days = df.loc[(df['home_team'] == team) | (df['away_team'] == team)].sort_values(by='matchday')
    for _, row in match_days.iterrows():
        if row['home_team'] == team:
            goal_trend.append([team.title(), row['matchday'], row['home_score_full_time']])
        else:
            goal_trend.append([team.title(), row['matchday'], row['away_score_full_time']])

goal_trend = pd.DataFrame(goal_trend, columns=['Team', 'Match Day', 'Goals'])
print(goal_trend.head(10))

# Pivot the data to create a matrix of teams vs matchdays
goal_trend_pivot = goal_trend.pivot_table(index='Team', columns='Match Day', values='Goals', aggfunc='sum', fill_value=0)

# Create the heatmap
plt.figure(figsize=(20, 40))
sns.heatmap(goal_trend_pivot, cmap="YlGnBu", cbar_kws={'label': 'Goals Scored'}, linewidths=0.5)

plt.title('Goal Scoring Trend Across Matchdays (Top 5 Leagues)', fontsize=16, fontweight='bold')
plt.xlabel('Matchday', fontsize=14, fontweight='bold')
plt.ylabel('Team', fontsize=14, fontweight='bold')
plt.xticks(rotation=90)  # Rotate matchday labels for clarity
plt.gcf().set_facecolor('lightgrey')
plt.tight_layout()

# plt.savefig('goal_scoring_trend.png', dpi=300)

plt.show()

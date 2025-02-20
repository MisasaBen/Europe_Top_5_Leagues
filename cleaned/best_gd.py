import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

csv_s = ['cleaned_bundesliga.csv', 'cleaned_laliga.csv', 'cleaned_ligue_1.csv', 'cleaned_premier_league.csv', 'cleaned_serie_A.csv']
gd_list = []

for csv in csv_s:
    df = pd.read_csv(csv)
    df['league'] = csv.replace('cleaned_', '').replace('_', ' ').replace('.csv', '').title()
    df['home_team'] = df['home_team'].str.replace('1.', '', regex=True).str.title()
    df['away_team'] = df['away_team'].str.replace('1.', '', regex=True).str.title()

    for team in df['home_team'].unique():
        team_rec = df.loc[(df['home_team'] == team) | (df['away_team'] == team)].sort_values(by='matchday')
        team_rec['goal_diff'] = np.where(team_rec['home_team'] == team,
                                     team_rec['home_score_full_time'] - team_rec['away_score_full_time'],
                                     team_rec['away_score_full_time'] - team_rec['home_score_full_time'])
        sum_gd = team_rec['goal_diff'].sum()
        league = df['league'].iloc[0]
        gd_list.append([league, team.title(), sum_gd])

gd_list = pd.DataFrame(gd_list, columns=['League', 'Team', 'Goal Difference']).sort_values(by='Goal Difference', ascending=False).reset_index(drop=True)


plt.figure(figsize=(12, 8))
sns.boxplot(x='League', y='Goal Difference', data=gd_list, palette='Set2', hue='League')
plt.title('Goal Difference Distribution by League', fontsize=16, fontweight='bold')
plt.gcf().set_facecolor('lightgray')
plt.xlabel('League', fontsize=12, fontweight='bold')
plt.ylabel('Goal Difference', fontsize=12, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--')
plt.savefig('best_gd.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_data = ['cleaned_bundesliga.csv', 'cleaned_laliga.csv', 'cleaned_ligue_1.csv', 'cleaned_premier_league.csv', 'cleaned_serie_A.csv']
h_v_a = []
# Compare perf of home vs away in terms of wins
for team in csv_data:
    df = pd.read_csv(team)
    league_name = team.replace('cleaned_', '').replace('.csv', '').replace('_', ' ').title()
    home_team_wins = df.loc[df['home_team'] == df['winner']].shape[0]
    away_team_wins = df.loc[df['away_team'] == df['winner']].shape[0]

    h_v_a.append([league_name, home_team_wins, away_team_wins])

new_df = pd.DataFrame(h_v_a, columns=['league_name', 'home_team_wins', 'away_team_wins'])
print(new_df)

print('---------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------')

new_df_melted = new_df.melt(id_vars=['league_name'], value_vars=['home_team_wins', 'away_team_wins'], var_name='Win Type', value_name='Wins')
new_df_melted['Win Type'] = new_df_melted['Win Type'].replace({
    'home_team_wins':'Home Team Wins',
    'away_team_wins':'Away Team Wins'
})
print(new_df_melted)

plt.figure(figsize=(12, 8))
sns.barplot(x='league_name', y='Wins', data=new_df_melted, hue='Win Type')
# Customize plot appearance
plt.title('Home vs Away Wins in Each League', fontsize=16, fontweight='bold')
plt.gcf().set_facecolor('lightgrey')
plt.xlabel('League', fontsize=14)
plt.ylabel('Number of Wins', fontsize=14)
plt.tight_layout()
plt.savefig('home_vs_away_wins.png', dpi=300)
plt.show()


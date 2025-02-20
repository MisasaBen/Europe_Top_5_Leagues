import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = ['cleaned_bundesliga.csv', 'cleaned_laliga.csv', 'cleaned_ligue_1.csv', 'cleaned_premier_league.csv', 'cleaned_serie_A.csv']
dfs = []
table1 = []

for csv in data:
    df = pd.read_csv(csv)

    df['league'] = csv.replace('cleaned_', '').replace('_', ' ').replace('.csv', '').title()
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# combined_df.to_csv('combined_table.csv', index=False)

for team in combined_df['home_team'].unique():
    no_of_wins = combined_df.loc[combined_df['winner'] == team].shape[0]
    no_of_losses = combined_df.loc[combined_df['defeat'] == team].shape[0]
    no_of_draws = combined_df.loc[(((combined_df['home_team'] == team) & (combined_df['goal_diff'] == 0)) | ((combined_df['away_team'] == team) & (combined_df['goal_diff'] == 0)))].shape[0]
    league = combined_df.loc[((combined_df['home_team'] == team) | (combined_df['away_team'] == team)), 'league'].iloc[0]

    table1.append([league, team, no_of_wins, no_of_losses, no_of_draws])

table_df = pd.DataFrame(table1, columns=['League', 'Team', 'Wins', 'Losses', 'Draws'])

# Set plot style
sns.set(style="whitegrid")
plt.figure(figsize=(20, 30))
plt.gcf().set_facecolor('lightblue')

# Top 10 teams with most wins
top_wins = table_df.sort_values(by='Wins', ascending=False).head(10)
plt.subplot(3, 1, 1)
sns.barplot(x='Team', y='Wins', hue='League', data=top_wins, dodge=False)
plt.title('Top 5 Teams with Most Wins', fontsize=20, fontweight='bold', fontname='Times New Roman')
plt.ylabel('Number of Wins', fontsize=10, fontweight='bold', fontname='Times New Roman')
plt.xlabel('Team', fontsize=10, fontweight='bold', fontname='Times New Roman')
plt.xticks(ticks=range(10), labels=[team.title() for team in top_wins['Team']], rotation=45)  # Apply title() to team names

# Top 10 teams with most draws
top_draws = table_df.sort_values(by='Draws', ascending=False).head(10)
plt.subplot(3, 1, 2)
sns.barplot(x='Team', y='Draws', hue='League', data=top_draws, dodge=False)
plt.title('Top 5 Teams with Most Draws', fontsize=20, fontweight='bold', fontname='Times New Roman')
plt.ylabel('Number of Draws', fontsize=10, fontweight='bold', fontname='Times New Roman')
plt.xlabel('Team', fontsize=10, fontweight='bold', fontname='Times New Roman')
plt.xticks(ticks=range(10), labels=[team.title() for team in top_draws['Team']], rotation=45)  # Apply title() to team names

# Top 10 teams with most losses
top_losses = table_df.sort_values(by='Losses', ascending=False).head(10)
plt.subplot(3, 1, 3)
sns.barplot(x='Team', y='Losses', hue='League', data=top_losses, dodge=False)
plt.title('Top 5 Teams with Most Losses', fontsize=20, fontweight='bold', fontname='Times New Roman')
plt.ylabel('Number of Losses', fontsize=10, fontweight='bold', fontname='Times New Roman')
plt.xlabel('Team', fontsize=10, fontweight='bold', fontname='Times New Roman')
plt.xticks(ticks=range(10), labels=[team.title() for team in top_losses['Team']], rotation=45)  # Apply title() to team names

plt.tight_layout()
plt.savefig('Top_teams.png', dpi=300)
plt.show()

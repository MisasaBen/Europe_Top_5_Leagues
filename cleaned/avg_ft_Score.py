import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('combined_table.csv')

score_counts = df.groupby(['home_score_full_time', 'away_score_full_time']).size().reset_index(name='count')


pivot_Table = score_counts.pivot(index='home_score_full_time', columns='away_score_full_time', values = 'count').fillna(0)

sns.heatmap(pivot_Table, cmap='coolwarm', annot=True, fmt='g', linewidths=.5, cbar_kws={'label': 'Frequency'})
plt.title('Average Full Time Score Across Top 5 Leagues', fontsize=30, fontweight='bold', fontdict={'fontname': 'Times New Roman'})
plt.xlabel('Away Team FT Score', fontsize=12, fontweight='bold', font = 'Times New Roman')
plt.ylabel('Home Team FT Score', fontsize=12, fontweight='bold', font = 'Times New Roman')
plt.tight_layout()
plt.savefig('avg_ft_score.png', dpi = 300)
plt.show()

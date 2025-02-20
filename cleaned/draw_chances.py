import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('combined_table.csv')

total_matches = df.shape[0]

draws = df[df['winner'] == 'draw'].shape[0]
non_Draws = total_matches - draws
draw_percentage = (draws / total_matches) * 100

print(f'Total Matches: {total_matches}')
print(f'Total Draws: {draws}')
print(f'Draw Percentage: {draw_percentage:.2f}%')

labels = ['Draws', 'Non-Draws']
sizes = [draws, non_Draws]
colors = ['gold', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140, wedgeprops={'edgecolor': 'black'})

centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Draw Percentage in Top 5 Leagues', fontsize=30, fontweight='bold', fontdict={'fontname': 'Times New Roman'})
plt.savefig('draw_percentage.png', dpi = 300)
plt.tight_layout()
plt.show()
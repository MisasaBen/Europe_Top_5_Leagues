import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

df = pd.read_csv('combined_table.csv')
ref_table = []

for ref in df['ref'].unique():
    ref_matches = df[df['ref'] == ref].shape[0]
    ref_table.append([ref.title(), ref_matches])

ref_df = pd.DataFrame(ref_table, columns=['Referee', 'Matches'])

# Create an interactive bar chart
fig = px.bar(
    ref_df,
    x='Matches',
    y='Referee',
    orientation='h',
    title='Number of Matches Officiated by Each Referee',
    labels={'Matches': 'Number of Matches', 'Referee': 'Referee'},
    color='Matches',
    color_continuous_scale='Blues'
)

# Customize the chart
fig.update_layout(
    height=800,  # Adjust height for large datasets
    xaxis_title='Number of Matches',
    yaxis_title='Referee',
    showlegend=False
)

# Save and show the plot
fig.write_image('referee_matches.png', engine='kaleido')
fig.show()

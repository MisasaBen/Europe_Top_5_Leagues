# Europe Top 5 Leagues - Match Data Analysis (2023/24)

## Overview
This project analyzes match data from the 2023/24 season of Europe's top 5 football leagues:
- English Premier League
- Spanish La Liga
- German Bundesliga
- Italian Serie A
- French Ligue 1

Using **Python (Pandas, NumPy, Matplotlib, Seaborn)**, this project explores trends, team performance, goal statistics, referee influence, and match outcomes.

## Dataset
The dataset consists of five separate CSV files (one for each league) with the following structure:
- **date**: Match date (YYYY-MM-DD)
- **matchday**: Round number in the season
- **home_team**: Name of the home team
- **away_team**: Name of the visiting team
- **home_score_full_time**: Home team's goals at full-time
- **away_score_full_time**: Away team's goals at full-time
- **goal_diff**: Goal difference
- **winner**: Winning team
- **ref**: Referee of the match

## Objectives & Questions Answered
This project covers multiple **exploratory data analysis (EDA)** and **visualization** objectives, including:
1. **Which league has the highest average goals per match?**
2. **How do home and away teams perform across leagues?**
3. **Which teams have the most wins, draws, and losses?**
4. **What are the most common full-time scores?**
5. **How does referee assignment impact match outcomes?**
6. **Which teams perform best in terms of goal difference?**

## Visualizations
The project includes various visualizations such as:
- **Bar Charts**: Total goals per league.
- **Heatmaps**: Correlations between match variables.
- **Line Plots**: Goals per matchday.
- **Box Plots**: Goal differences across leagues.
- **Pie Charts**: Match outcome distribution.

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/MisasaBen/Europe_Top_5_Leagues.git

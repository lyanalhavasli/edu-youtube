# My ChatGpt Usage Data Analysis DSA 210 Project
## Description
This project focuses on analyzing my ChatGPT usage, leveraging data exported from ChatGPT in JSON format. The primary goal of this analysis is to uncover patterns and trends in my interactions with ChatGPT, offering insights into my usage behavior. Through visualizations and statistical analyses, the project explores the frequency and timing of queries across different days of the week and hours of the day, examines query distribution among various ChatGPT model versions, and investigates relationships between conversation lengths and the time spent on them. Bar charts, scatter plots, and other visual tools are used to highlight these patterns, while statistical tests, such as chi-square tests and correlation analyses, validate the findings.

## Motivation
The increasing reliance on AI-powered tools like ChatGPT in daily activities has sparked my interest in understanding how I personally interact with such technologies. By analyzing my ChatGPT interaction data, I aimed to uncover trends in the frequency and timing of queries, preferences for specific model versions, and the nature of my conversations. Through this analysis, I hope to gain insights into how I engage with AI tools, evaluate their impact on my productivity, and explore ways to optimize my usage for better outcomes. Additionally, this project demonstrates the power of data-driven approaches to understanding behavior, encouraging others to explore similar analyses for personal growth and reflection.

## Data Source
The data for this project was sourced from ChatGPT's conversation export feature, which provides interaction logs in JSON format. The dataset includes detailed information about each query, such as timestamps, message content, conversation duration, and metadata like the ChatGPT model version used. These structured logs allowed for a comprehensive analysis of my interactions with ChatGPT. The timestamps provided insights into the temporal patterns of my usage, while the metadata offered information about my preferences for different model versions. The data was preprocessed and cleaned to extract relevant features, such as the number of messages, time spent per conversation, and query lengths, enabling a detailed exploration of my ChatGPT usage behavior. This dataset forms the foundation for the visualizations, statistical analyses, and insights generated in this project.

## Data Analysis
* The data analysis for this project involved several stages, combining various techniques to extract meaningful insights from the ChatGPT interaction dataset. The process began with data preprocessing, where the JSON data was parsed to extract relevant features such as timestamps, query content, conversation lengths, and model usage. This was followed by data cleaning, addressing any missing or inconsistent values to ensure the reliability of the analysis.

- Next, exploratory data analysis (EDA) was conducted using visualizations, such as bar charts and scatter plots, to identify trends and patterns. Temporal analysis highlighted query distributions across days of the week and hours of the day, while model-specific analysis examined the usage of different ChatGPT versions. Correlation analysis was employed to investigate relationships between conversation duration and the number of messages exchanged.

* To validate observations, statistical hypothesis testing was used, including chi-square tests for categorical distributions and Pearson correlation tests for continuous relationships. These techniques ensured that the conclusions drawn were statistically significant and data-driven. This multi-stage analysis approach provided a holistic understanding of my ChatGPT usage patterns, from raw data processing to deriving actionable insights.

## Findings
# Number of Queries Across the Time of Day
![image](https://github.com/user-attachments/assets/635c4a5b-0377-4145-a92f-efba31218ec5)

* I started by analyzing the distribution of queries throughout the day. The graph above provides an overview of my activity levels across different hours, showcasing that the most active hours I interacted with ChatGPT were late at night (11,12, and 1 A.M.). This visualization sets the foundation for a deeper dive into the trends observed on specific days of the week, revealing potential patterns in how my usage aligns with my daily schedule and routines. In the following section, I will utilize the Chi-Square goodness-of-fit test to analyze individual graphs for each day of the week to uncover more nuanced insights into my interaction patterns.

![image](https://github.com/user-attachments/assets/49a6e024-6733-4d25-abae-232133243a9b)

* Monday Query Analysis: The graph for Monday reveals a notable pattern in my ChatGPT usage across the hours of the day. A statistical analysis was performed using the Chi-Square goodness-of-fit test to determine whether the queries were uniformly distributed throughout the day. The observed data showed significant variation in activity, with peak hours around 2 AM and 8 PM. The Chi-Square test resulted in a test statistic of 136.88 and a p-value of 5.27e-19, which is far below the significance level of 0.05. This led to the rejection of the null hypothesis, indicating that my queries on Monday were not uniformly distributed. This suggests clear periods of high and low interaction, likely influenced by how it is the starting of the week.

![image](https://github.com/user-attachments/assets/7cc7eb28-9529-4df4-aab0-fe7fe832ad5d)

* Tuesday Query Analysis: A Chi-Square goodness-of-fit test was conducted to evaluate whether the queries were uniformly distributed throughout the day. The observed data revealed specific peaks, particularly around 4 PM and moderate activity during evening hours. The statistical test produced a Chi-Square value of 49.71 and a p-value of 2.55e-05, which is significantly below the significance level of 0.05. Consequently, the null hypothesis was rejected, confirming that the distribution of queries on Tuesday was not uniform.

![image](https://github.com/user-attachments/assets/34bcdf55-01d5-486e-ad79-4c42f403ab71)

* Wednesday Query Analysis: The graph above depicts the distribution of my ChatGPT usage throughout the day, showing noticeable peaks in the late evening hours, particularly at 11 PM. A Chi-Square goodness-of-fit test was conducted to examine whether the distribution of queries was uniform across the day. The statistical test yielded a Chi-Square value of 50.28 and a p-value of 6.84e-05, which is significantly below the threshold of 0.05. Therefore, the null hypothesis was once again rejected, indicating that the queries were not uniformly distributed throughout the day.

![image](https://github.com/user-attachments/assets/7bdaffb2-0bf8-47bf-9e18-23f27632e607)

* Thursday Query Analysis: The graph for Thursday reveals a pattern in ChatGPT usage, with prominent activity peaks at midnight and late evening hours around 10 PM to 11 PM. A Chi-Square goodness-of-fit test was conducted to evaluate whether the distribution of queries followed a uniform pattern throughout the day. The test resulted in a Chi-Square statistic of 46.56 and a p-value of 5.55e-06, which is significantly below the significance level of 0.05. As a result, the null hypothesis was rejected, confirming that the distribution of queries on Thursday was not uniform.

![image](https://github.com/user-attachments/assets/87b77c5d-ea98-42f9-a7a1-ac6ed3441fc7)

* Friday Query Analysis: The Friday query distribution shows significant spikes in activity around 1 AM, with secondary peaks during late afternoon hours, especially at 4 PM. A Chi-Square goodness-of-fit test was conducted to determine whether the queries were uniformly distributed throughout the day. The test resulted in a Chi-Square statistic of 92.55 and a p-value of 3.30e-13, well below the significance level of 0.05. This led to the rejection of the null hypothesis, indicating that the distribution of queries on Friday was not uniform.

![image](https://github.com/user-attachments/assets/4cf929a9-b376-453e-94bd-40b601133d15)

* Saturday Query Analysis: The query activity on Saturday reveals distinct peaks during the early hours (12 AM to 2 AM) and late evening (9 PM to 11 PM). A Chi-Square goodness-of-fit test was conducted to evaluate whether the queries were uniformly distributed across the day. The test produced a Chi-Square statistic of 74.41 and a p-value of 1.66e-09, significantly below the 0.05 threshold. Consequently, the null hypothesis of uniform distribution was rejected, confirming that the query activity on Saturday is highly concentrated in specific time intervals, indicating a late-night and evening usage patterns.

![image](https://github.com/user-attachments/assets/1642f700-2a50-48bf-a6c5-bfc499256dca)


* Sunday Query Analysis: The query activity on Sunday showed moderate usage during the early hours (12 AM to 4 AM) and a noticeable spike around 7 PM. A Chi-Square goodness-of-fit test was conducted to evaluate the uniformity of the query distribution across the day. The test yielded a Chi-Square statistic of 41.56 and a p-value of 0.000459, which is below the significance threshold of 0.05. This result leads to the rejection of the null hypothesis, confirming that the queries on Sunday are not uniformly distributed. The analysis highlights that activity is concentrated in the early morning and early evening, reflecting distinct usage patterns on Sundays.

# Number of Queries by Day of the Week 

![image](https://github.com/user-attachments/assets/1b35d7ee-daab-48ac-89a4-4fb59f7d9952)

* This graph presents the distribution of query activity across the days of the week. The analysis reveals that Monday and Saturday are the most active days, with the highest number of queries, suggesting a potential spike in usage at the beginning of the week and during the weekend. In contrast, Sunday exhibits the lowest query activity, as I usually go out on Sundays. The middle of the week, particularly Wednesday and Thursday, show moderate query activity. This analysis provides insights into weekly engagement trends, which can be useful for resource planning and understanding temporal preferences.
* To confirm these results, a Chi-Square goodness-of-fit test was conducted. The observed query counts for each day were compared against an expected uniform distribution, assuming an equal number of queries for all days. The test yielded a Chi-Square Statistic of 46.67 and a P-Value of 2.18e-08, which is significantly lower than the significance level of 0.05. As a result, the null hypothesis was rejected, indicating that the queries are not uniformly distributed throughout the week. This supports the observation that some days, such as Monday and Saturday, have significantly higher query activity, while others, like Sunday, exhibit much lower engagement.

# Analysis of Time Spent on Conversations vs. Conversation Length

![image](https://github.com/user-attachments/assets/e2c3ef8c-4a2f-40d3-9f70-57f40b729548)

* The above scatterplot visualizes the relationship between the time spent on a conversation (in minutes) and the total number of messages exchanged during that conversation. The analysis included both Pearson and Spearman correlation tests to investigate the nature of the relationship:

** Pearson Correlation: The Pearson correlation coefficient was calculated as 0.162, with a p-value of 0.148. This result suggests no significant linear relationship between conversation duration and message count, as we fail to reject the null hypothesis at the 0.05 significance level.
** Spearman Correlation: The Spearman correlation coefficient was 0.848, with a highly significant p-value of 1.687e-23. This indicates a strong monotonic relationship between the two variables, where longer conversations tend to have more messages.

While the Pearson test shows no linear correlation, the Spearman test highlights a significant monotonic relationship, suggesting that while the relationship may not be strictly linear, there is a clear trend where longer durations are associated with more messages. This highlights the complex nature of user interaction, where extended conversations often involve higher engagement.




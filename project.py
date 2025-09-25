import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
population_data=pd.read_csv("population.csv")

population_data.head(266)      #display data set
population_data.describe

data_2022=population_data.loc[:,["country name","2022"]]               #extracting the relevent colums
data_2022.dropna()    #remove rows with missing values


data_2022.head() #display the firstfew rows of the cleaned data
# set up the visual style
sns.set(style="whitegrid")
# Histogram for population distribution in 2022
plt.figure(figsize = (12, 6))
sns.histplot(data = data_2022, x='2022', bins=30, kde=True, color='blue')
plt.title('Population Distribution in 2022')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()

# Convert population column to numeric (in case it isn't already)
data_2022['2022'] = pd.to_numeric(data_2022['2022'], errors='coerce')

# Sort data by population in descending order and select top 10
top_10_countries = data_2022.sort_values(by='2022', ascending=False).head(10)

# Set up the visual style
sns.set(style="whitegrid")

# Bar chart for top 10 most populous countries in 2022
plt.figure(figsize=(12, 6))
sns.barplot(data = top_10_countries, x='Country Name', y='2022', palette='viridis')
plt.title('Top 10 Most Populous Countries in 2022')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.show()





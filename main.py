import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('metplotlib_project/netflix_titles.csv')

df =df.dropna( subset=['type','release_year','rating','country','duration'])

type_count = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index ,type_count.values, color=['blue','orange'])
plt.xlabel('Type')
plt.ylabel('counts')
plt.tight_layout()
# plt.savefig('movie_vs_shows.png')
plt.show()

rating_count = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',startangle=90)
plt.title('Percentage of Content Ratings')
plt.tight_layout()
# plt.savefig('rating_pie.png')
plt.show()

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black',rwidth=0.9)
plt.title('Movies Duration')
plt.xlabel('Duration(min)')
plt.ylabel('No. of Movies')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
# plt.savefig('Movies_duration_histogram.png')
plt.show()

release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title('Release year VS No. of Shows')
plt.xlabel('Release year')
plt.ylabel('No. of Shows')
plt.tight_layout()
# plt.savefig('release_year_scatter.png')
plt.show()

country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values, color='coral')
plt.title('Top 10 Country by Number of Shows')
plt.xlabel('No. of Shows')
plt.ylabel('country')
plt.tight_layout()
# plt.savefig('top10_country_with_most_shows.png')
plt.show()

content_by_year = df.groupby(['release_year',"type"]).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2,figsize=(12,5))

ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue', label='Movies')
ax[0].set_title('Movies released per year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('Number of Movies')
ax[0].legend(loc='upper left',fontsize=12)

ax[1].plot(content_by_year.index,content_by_year['TV Show'],color='orange', label='TV Shows')
ax[1].set_title('TV shows released per year')
ax[1].set_xlabel('year')
ax[1].set_ylabel('Number of Movies')
ax[1].legend(loc='upper left',fontsize=12)

fig.suptitle("Comparison of Movives and TV shows released over years")
plt.tight_layout()
plt.savefig('movies_tv_shows_comparison.png')

plt.show()



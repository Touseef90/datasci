import pandas as pd

metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

# print(metadata.head(20))

C = metadata['vote_average'].mean()
# print(C)

m = metadata['vote_count'].quantile(0.90)
# print(m)

q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
# print(q_movies.shape)

def weighted_rating(x, m=m, C=C):
  v = x['vote_count']
  R = x['vote_average']
  return (v/(v+m)*R) + (m/(m+v)*C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)
# print(q_movies.head())

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')

metadata['overview'] = metadata['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(metadata['overview'])
# print(tfidf_matrix.shape)

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

def get_recommendation(title, cosine_sim=cosine_sim):
  idx = indices[title]

  sim_scores = list(enumerate(cosine_sim[idx]))

  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

  sim_scores = sim_scores[1:11]

  movie_indices = [i[0] for i in sim_scores]

  return metadata['title'].iloc[movie_indices]


print(get_recommendation('The Dark Knight Rises'))


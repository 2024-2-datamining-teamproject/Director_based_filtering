# input: 감독 이름
# 해당 감독의 영화ID 리스트 찾기
# 영화ID 리스트 중 평점평균 높은 순으로 sorting
# output: 상위 10개 영화ID


import pandas as pd

file_path = "C:/Users/gemge/OneDrive/바탕 화면/Directors.csv"
movie_ratings_df = pd.read_csv("C:/Users/gemge/OneDrive/바탕 화면/ratings.csv")

def get_movie_ids_by_director(file_path, director_name):
    try:
        # CSV 파일 읽기
        df = pd.read_csv(file_path)
        
        # 감독 이름이 일치하는 행 필터링
        filtered_movies = df[df['director'] == director_name]
        
        # 해당 감독의 movieId 리스트 생성
        movie_ids = filtered_movies['movieId'].tolist()
        
        return movie_ids
    except FileNotFoundError:
        print("CSV 파일을 찾을 수 없습니다.")
        return []
    except KeyError:
        print("CSV 파일에 'director' 또는 'movieId' 열이 없습니다.")
        return []



def sort_by_avg_rates(movie_id_list):
    # avg on every movie first,
    filtered_movie_list = movie_ratings_df[movie_ratings_df['movieId'].isin(movie_id_list)]
    #print(filtered_movie_list)
    average_ratings = filtered_movie_list.groupby('movieId')['rating'].mean().reset_index()
    average_ratings.rename(columns={'rating':'avg_rating'}, inplace=True)
    
    # print("\n")
    # 각 movie의 평균 출력
    # print(average_ratings)
    # and sort it in descending order
    average_ratings = average_ratings.sort_values(by='avg_rating', ascending=False)['movieId']
    avg_list = average_ratings.tolist()
    
    return avg_list[:10] # 상위 10개만 출력



# Test
director_name = input("감독 이름을 입력하세요: ")

movie_ids = get_movie_ids_by_director(file_path, director_name)

if movie_ids:
    print(f"감독 '{director_name}'의 movieId 리스트: {movie_ids}")
else:
    print(f"감독 '{director_name}'의 영화 데이터를 찾을 수 없습니다.")

print("avg rates 높은 순으로 정렬된 상위 10개 movieId list:")
print(sort_by_avg_rates(movie_ids))

import csv

# 파일 경로 설정
input_file_path_movies = 'movies.csv'
input_file_path_movie_details = 'movie_details.csv'
input_file_path_movie_cast = 'movie_cast.csv'
input_file_path_reviews = 'movie_reviews.csv'

movie_output_file_path = 'movie.csv'
movie_details_part_output_file_path = 'movie_details_part.csv'
genre_part_output_file_path = 'genre_part.csv'

# movie_details 데이터 분리 함수
def read_and_split_csv(file_path):
    movie_details_part = []
    genre_dict = {}
    # cast = {}
    # review = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # if file_path == 'movies_details.csv':
        genre_set = []
        for row in reader:
            movie_details = {
                'id': row['movie_id'],
                'budget': row['budget'],
                'revenue': row['revenue'],
                'runtime': row['runtime'],
            }
            movie_details_part.append(movie_details)
            
            genre_list = row['genres'].split(', ')
            
            for elem in genre_list:
                genre_set += [elem]
        genre_set = set(genre_set)
        
        id = 0
        for elem in genre_set:
            id += 1
            genre = {
                'id': id,
                'name': elem
            }
            genre_dict[id] = genre
    return movie_details_part, list(genre_dict.values()), genre_list


# movies, movie_details_list 통합 함수
def read_and_unite(file_path_1, details_part):
    movie_part = []
    with open(file_path_1, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # if file_path == 'movies_details.csv':
        for row in reader:
            movie = {
                'id': row['id'],
                'release_date': row['release_date'],
                'popularity': row['popularity'],
                'budget': '',
                'revenue': '',
                'runtime': '',
                'title': row['title'],
            }
            movie_part.append(movie)
        
        for elem in details_part:
            for elem_2 in movie_part:
                if elem['id'] == elem_2['id']:
                    elem_2['budget'] = elem['budget']
                    elem_2['revenue'] = elem['revenue']
                    elem_2['runtime'] = elem['runtime']
    return movie_part

# CSV 파일로 저장
def write_csv(file_path, data, fieldnames):
    # 쓰기 모드 일때는 newline 중요하다.
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        # DictWriter의 두번째 인자에 fieldnames를 넣었다고해서,
        # 첫번째 row가 그 필드네임으로 채워지는건 아니다.
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()    # <- 필드네임을 작성
        writer.writerows(data)


def main():
    movie_details_part, genre_part, genre_list = read_and_split_csv(input_file_path_movie_details)
    movie = read_and_unite(input_file_path_movies, movie_details_part)
    
    # movie_details_part.csv 저장
    movie_details_part_fieldnames = ['id', 'budget', 'revenue', 'runtime']
    write_csv(movie_details_part_output_file_path, movie_details_part, movie_details_part_fieldnames)
    
    # movie_part.csv 저장
    movie_part_fieldnames = ['id', 'release_date', 'popularity', 'budget', 'revenue', 'runtime', 'title']
    write_csv(movie_output_file_path, movie, movie_part_fieldnames)
    
    # genre_part.csv 저장
    genre_part_fieldnames = ['id', 'name']
    write_csv(genre_part_output_file_path, genre_part, genre_part_fieldnames)
    
if __name__ == '__main__':
    main()

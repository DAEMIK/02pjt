import csv

# Input file names
movie_details_file = "movie_details.csv"  # Contains movie_id, budget, revenue, runtime, genres
# genres_output_file = "genres.csv"  # Unique genres table (with IDs)
movie_genres_output_file = "movie_genre.csv"  # Many-to-Many relationship table (movie & genre IDs)

# Data storage
unique_genres = {}  # Store unique genre names with auto-generated IDs
movie_genres = []  # Store movie-genre relationships

# Step 1: Read movie_details.csv and extract genres, then map movie_id to genre_id
genre_id_counter = 1  # Initialize genre ID counter
movie_genre_id_counter = 1  # Initialize movie-genre relationship ID counter
with open(movie_details_file, mode="r", encoding="utf-8") as f1:
    reader = csv.DictReader(f1)
    for row in reader:
        movie_id = row["movie_id"]
        
        # Extract and clean genres into a list
        genres_list = [genre.strip() for genre in row["genres"].split(",") if genre.strip()]
        
        # Assign unique IDs to genres
        for genre in genres_list:
            if genre not in unique_genres:
                unique_genres[genre] = genre_id_counter  # Assign a unique genre ID
                genre_id_counter += 1  # Increment the genre ID counter
            
            # Store movie-genre relationship (Using genre ID now)
            movie_genres.append({"id": movie_genre_id_counter, "movie_id": movie_id, "genre_id": unique_genres[genre]})
            movie_genre_id_counter += 1  # Increment the movie-genre relationship ID

# # Step 2: Save unique genres to genres.csv (WITH IDs)
# with open(genres_output_file, mode="w", newline="", encoding="utf-8") as g_file:
#     writer = csv.writer(g_file)
#     writer.writerow(["id", "name"])  # Header (now includes ID)
#     for genre_id, genre in unique_genres.items():
#         writer.writerow([genre_id, genre])

# Step 3: Save movie-genre relationships to movie_genre.csv (USING GENRE IDs)
with open(movie_genres_output_file, mode="w", newline="", encoding="utf-8") as mg_file:
    writer = csv.DictWriter(mg_file, fieldnames=["id", "movie_id", "genre_id"])
    writer.writeheader()
    writer.writerows(movie_genres)

# print(f"Genres table saved as {genres_output_file}")
print(f"Movie-Genres relationship table saved as {movie_genres_output_file}")

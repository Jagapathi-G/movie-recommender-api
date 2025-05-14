import sqlite3
import pandas as pd

def init_db():
    # Connect to SQLite database (creates if not exists)
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    
    # Create movies table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INTEGER PRIMARY KEY,
            title TEXT,
            genres TEXT
        )
    """)
    
    # Create ratings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            user_id INTEGER,
            movie_id INTEGER,
            rating FLOAT,
            timestamp INTEGER,
            FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
        )
    """)
    
    # Load MovieLens 1M data
    movies = pd.read_csv(
        "ml-1m/movies.dat",
        sep="::",
        engine="python",
        names=["movie_id", "title", "genres"],
        encoding="ISO-8859-1"
    )
    ratings = pd.read_csv(
        "ml-1m/ratings.dat",
        sep="::",
        engine="python",
        names=["user_id", "movie_id", "rating", "timestamp"]
    )
    
    # Insert data into SQLite
    movies.to_sql("movies", conn, if_exists="replace", index=False)
    ratings.to_sql("ratings", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()

def get_recommendations(genre=None, min_rating=4.0, n=10):
    conn = sqlite3.connect("movies.db")
    query = """
        SELECT m.movie_id, m.title, m.genres, AVG(r.rating) as avg_rating
        FROM movies m
        JOIN ratings r ON m.movie_id = r.movie_id
        WHERE 1=1
    """
    params = []
    
    if genre:
        query += " AND m.genres LIKE ?"
        params.append(f"%{genre}%")
    
    query += " GROUP BY m.movie_id, m.title, m.genres HAVING avg_rating >= ?"
    params.append(min_rating)
    
    query += " ORDER BY avg_rating DESC LIMIT ?"
    params.append(n)
    
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    
    return df[["title", "genres", "avg_rating"]].to_dict(orient="records")

if __name__ == "__main__":
    init_db()

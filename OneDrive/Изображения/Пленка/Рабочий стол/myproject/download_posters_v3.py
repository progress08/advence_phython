import urllib.request
import os

# Define the base directory for static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FILMS_DIR = os.path.join(BASE_DIR, 'django-project', 'static', 'films')

# Ensure the directory exists
os.makedirs(STATIC_FILMS_DIR, exist_ok=True)

# Map of filename (without extension) to image URL
films = {
    'interstellar': 'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
    'dark-knight': 'http://www.impawards.com/2008/posters/dark_knight.jpg',
    'inception': 'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg',
    'spirited-away': 'https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png',
    'matrix': 'https://image.tmdb.org/t/p/original/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg',
    'parasite': 'https://image.tmdb.org/t/p/original/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg'
}

downloaded_files = []

print(f"Downloading posters to {STATIC_FILMS_DIR}...")

for filename, url in films.items():
    output_path = os.path.join(STATIC_FILMS_DIR, f"{filename}.jpg")
    
    # Check if file already exists and has content
    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        print(f"Skipping {filename}.jpg (already exists).")
        downloaded_files.append(output_path)
        continue

    print(f"Downloading {filename}.jpg from {url}...")
    try:
        # User-Agent header is often required to avoid 403 Forbidden
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        
        with urllib.request.urlopen(req) as response:
            with open(output_path, 'wb') as out_file:
                out_file.write(response.read())
        
        print(f"Successfully downloaded {filename}.jpg")
        downloaded_files.append(output_path)
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("\nSummary of files created/verified:")
for path in downloaded_files:
    print(path)

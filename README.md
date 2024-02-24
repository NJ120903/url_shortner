# URL Shortener

This is a simple URL shortener web application built using Python and Flask.

## Features

- Converts long URLs into shorter, more manageable links
- Stores the mapping between original and shortened URLs in a SQLite database
- Handles redirection to the original URL when the shortened link is accessed

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/url-shortener.git
   ```

2. Install the dependencies:

   ```bash
   pip install Flask
   pip install db-sqlite3
   pip install strings
   pip install random2
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Access the application in your web browser at `http://localhost:5000`

## Usage

1. Enter a long URL into the input field on the home page and click the "Shorten" button.
2. Copy the shortened URL and use it to access the original URL.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests.

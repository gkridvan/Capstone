
# Botino - A Conversational News Bot

**Botino** is a Streamlit-based web application that allows users to interact with an AI-powered chatbot, which can answer questions and provide related news articles from a CSV file. The application integrates with the `OllamaLLM` model to generate responses and uses the `difflib` library to find similar news titles from the stored articles.

## Features

- **Interactive Chatbot**: Users can ask questions, and the bot will provide responses powered by a language model (`OllamaLLM`).
- **Related News Articles**: Based on the user’s input, the bot fetches and displays related news articles from a stored CSV file containing article details such as titles, images, and links.
- **Data Storage**: The bot stores news articles in a CSV file (`articles.csv`) and can fetch data from an external API to populate this file with the latest articles.
- **Web Interface**: Built using Streamlit, it offers an interactive user interface where users can input their queries and view responses in real-time.

## Requirements

Make sure you have the following libraries installed:

- `streamlit`
- `pandas`
- `langchain`
- `langchain_ollama`
- `difflib`
- `requests`
- `csv`
- `time`

You can install them using pip:

```bash
pip install streamlit pandas langchain langchain-ollama requests
```

## Project Structure

```bash
├── scrapping.py 
├── articles.csv           # Stores the fetched news articles
├── newchatbot.py                 # The main Streamlit application file
└── README.md              # Project documentation
```

## How it Works

### Step 1: Fetch and Store Articles
The application fetches news articles from the API and stores them in a CSV file (`articles.csv`). The data fetched includes the following fields:

- `ID`: Unique identifier for the article.
- `Slug`: Slug used in the URL.
- `Title`: Title of the article.
- `Summary`: Short summary of the article.
- `Published From`: Date when the article was published.
- `Image URL`: URL to the article's image.
- `Reading Time`: Estimated reading time for the article.

The data is fetched from the API in batches and stored locally.

### Step 2: User Interaction
Once the articles are loaded, users can input their questions in the provided text field. The chatbot uses the `OllamaLLM` model to generate a response based on the user's query.

### Step 3: Find Related News Articles
The chatbot uses the `difflib.get_close_matches` method to find news titles that are similar to the user's input. If any related articles are found, the bot displays them along with the article's title, image, and a link to the full article.

If no related articles are found, the bot will prompt the user to try again.

### Step 4: Display Results
The results are displayed in a chat-like interface, where:
- The user’s input is displayed as a message.
- The bot’s response is shown alongside the related articles (if any).

## How to Run

1. Clone this repository to your local machine.

2. Install the required libraries using `pip`.

3. Run the Streamlit application:

```bash
streamlit run app.py
```

4. The application will open in your default web browser. You can now interact with the chatbot by entering your questions in the input box.

### Sample Interaction

- **User:** "What is the latest news on AI?"
- **Bot:** Provides a response using the language model.
- **Bot:** Displays related articles if any are found in the dataset.

## Fetching New Articles

To fetch and store new articles from the API, the application includes a script that collects article data and writes it to the CSV file. This process is automated in the script and runs when the application is initialized.

### How to Fetch New Articles

The `write_to_csv` function will write the fetched articles to a file called `articles.csv`. To fetch articles, ensure that the script runs as intended by setting up the necessary API calls and data extraction process.

## Contributing

If you'd like to contribute to the project, feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

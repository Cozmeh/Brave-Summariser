
# Brave's Summarizer

This is a Python script that retrieves a summary of a given question using Brave's search engine and Brave's summerisation api.

## Table of Contents

- [Usage](#usage)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [Caution](#caution)


## Usage

You can use this script to obtain a summary of a question by calling the `get_summary(question)` function. Simply pass your question as a string to this function, and it will return the summary if it finds relevant information. For example:

```python
print(get_summary("what is a book?"))
```


## Dependencies

To run this script, you'll need the following dependencies:

- `requests`: Used for making HTTP requests to the Brave search engine.
- `time`: Used to introduce a delay in the script for better user experience.
- `BeautifulSoup` (from the `bs4` library): Used for parsing and extracting relevant information from the search results.

You can install these dependencies using pip:

```bash
pip install requests
pip install beautifulsoup4
```

## How It Works

1. The script takes a user's question as input.
2. It formats the question to create URLs for searching and summarization.
3. The search URL is constructed using the question with spaces replaced by '+', and an API URL for summarization is constructed with spaces replaced by '%20'.
4. The script sends a request to the search URL using the `requests` library.
5. If the request is successful (status code 200), the script proceeds to gather information.
6. It introduces a 2-second delay for a better user experience.
7. The script then makes an API request to Brave's summarizer using the API URL.
8. If it gets a response, it parses and extracts the text from the result using `BeautifulSoup`.
9. Finally, it returns the summary to the user.

## Caution

This script is provided for educational purposes only. It is not intended for commercial use cases. It utilizes Brave's search engine and Brave's summerisation api to fetch information and may be subject to the terms and conditions of Brave's services. Be sure to respect the terms of service and any applicable legal regulations when using this script.
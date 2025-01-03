# Analytics Vidhya Course Search

This is a smart search tool for finding relevant free courses on Analytics Vidhya's platform. The tool uses LangChain and sentence-transformers to create a semantic search system that helps users find the most relevant courses based on their queries.

## Features

- Natural language search queries
- Semantic understanding of course content
- Fast and accurate results
- User-friendly interface

## Technology Stack

- LangChain 0.3.x for RAG implementation
- sentence-transformers for embeddings
- ChromaDB as the vector store
- Streamlit for the web interface
- BeautifulSoup4 for web scraping

## Usage

1. Enter your search query in the text input
2. Adjust the number of results you want to see
3. View the matching courses with their details

## Development

To run this project locally:

1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the scraper: `python src/scraper.py`
4. Create embeddings: `python src/embeddings.py`
5. Start the app: `streamlit run src/app.py` 
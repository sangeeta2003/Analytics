# Analytics Vidhya Course Search - Technical Approach

## 1. Architecture Overview

Our solution uses a RAG (Retrieval Augmented Generation) system built with:
- LangChain for orchestration
- Sentence Transformers for embeddings
- ChromaDB for vector storage
- Streamlit for the user interface

## 2. Model Selection

### Embedding Model
We chose `sentence-transformers/all-MiniLM-L6-v2` because:
- Excellent performance for semantic search
- Lightweight (only 80MB)
- Fast inference speed
- Good balance of accuracy vs computational requirements

### Vector Database
ChromaDB was selected for:
- Easy integration with LangChain
- Persistence capabilities
- Efficient similarity search
- Simple deployment requirements

## 3. Implementation Details

### Data Processing
1. Course data collection (titles, descriptions, curriculum)
2. Text chunking with RecursiveCharacterTextSplitter
3. Generation of embeddings using Sentence Transformers
4. Storage in ChromaDB for efficient retrieval

### Search System
1. User query is embedded using the same model
2. ChromaDB performs similarity search
3. Results are ranked and returned based on semantic relevance

## 4. Deployment Architecture
- Streamlit for the web interface
- Hugging Face Spaces for hosting
- Persistent vector storage for quick retrieval

## 5. Future Improvements
1. Implement advanced filtering options
2. Add course difficulty levels
3. Include user feedback mechanism
4. Enhance result explanations 
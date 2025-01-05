import streamlit as st
import warnings
import logging
import os
from src.search import CourseSearch
from src.embeddings import CoursesEmbeddings

# Suppress warnings
warnings.filterwarnings('ignore')
logging.getLogger('torch.classes').setLevel(logging.ERROR)

st.set_page_config(
    page_title="Course Search",
    page_icon="📚",
    layout="wide"
)

@st.cache_resource
def initialize_search():
    # Check if vector store exists
    if not os.path.exists("data/chroma_db"):
        with st.spinner('First time setup: Creating vector store...'):
            embedder = CoursesEmbeddings()
            courses = embedder.load_courses()
            documents = embedder.prepare_documents(courses)
            vector_store = embedder.create_vector_store(documents)
            vector_store.persist()
    return CourseSearch()

def main():
    st.title("📚 Course Search")
    st.write("Search through courses using natural language!")

    search_engine = initialize_search()
    
    # Search interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        query = st.text_input(
            "Enter your search query",
            placeholder="e.g., 'machine learning for beginners' or 'python data analysis'"
        )
    
    with col2:
        k = st.slider("Number of results", min_value=1, max_value=5, value=3)
    
    if query:
        with st.spinner('Searching...'):
            results = search_engine.search(query, k=k)
            
            if not results:
                st.warning("No matching courses found.")
            else:
                for result in results:
                    lines = result.page_content.split('\n')
                    
                    # Extract and display information
                    title = next((line.replace("Title:", "").strip() 
                                for line in lines if line.startswith("Title:")), "")
                    description = next((line.replace("Description:", "").strip() 
                                     for line in lines if line.startswith("Description:")), "")
                    
                    st.markdown(f"### {title}")
                    st.markdown(f"**Description:**\n{description}")
                    
                    # Display curriculum items
                    curriculum = [line.strip() for line in lines if line.startswith("-")]
                    if curriculum:
                        st.markdown("**Curriculum:**")
                        for item in curriculum:
                            st.markdown(item)
                    
                    st.divider()

if __name__ == "__main__":
    main() 
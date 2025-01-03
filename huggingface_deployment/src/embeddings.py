from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import os

class CoursesEmbeddings:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        
    def load_courses(self, filename='data/courses.json'):
        try:
            if not os.path.exists(filename):
                print(f"Error: {filename} does not exist!")
                print("Please run the scraper first: python src/scraper.py")
                return []
                
            with open(filename, 'r') as f:
                courses = json.load(f)
                print(f"Loaded {len(courses)} courses from {filename}")
                return courses
        except json.JSONDecodeError:
            print(f"Error: {filename} is not valid JSON!")
            return []
        except Exception as e:
            print(f"Error loading courses: {str(e)}")
            return []
            
    def prepare_documents(self, courses):
        if not courses:
            print("No courses to process!")
            return []
            
        documents = []
        print(f"Processing {len(courses)} courses...")
        
        for course in courses:
            # Combine course information into a single text
            text = f"Title: {course['title']}\n"
            text += f"Description: {course['description']}\n"
            text += "Curriculum:\n"
            for item in course['curriculum']:
                text += f"- {item}\n"
            if 'level' in course:
                text += f"Level: {course['level']}\n"
            if 'duration' in course:
                text += f"Duration: {course['duration']}\n"
            if 'tags' in course:
                text += f"Tags: {', '.join(course['tags'])}\n"
            
            # Split text into chunks
            chunks = self.text_splitter.split_text(text)
            documents.extend(chunks)
            
        print(f"Created {len(documents)} document chunks")
        return documents
        
    def create_vector_store(self, documents):
        if not documents:
            print("No documents to embed!")
            return None
            
        print("Creating vector store...")
        try:
            store = Chroma.from_texts(
                texts=documents,
                embedding=self.embeddings,
                persist_directory="data/chroma_db"
            )
            print("Vector store created successfully!")
            return store
        except Exception as e:
            print(f"Error creating vector store: {str(e)}")
            return None

if __name__ == "__main__":
    print("Starting embedding process...")
    embedder = CoursesEmbeddings()
    
    courses = embedder.load_courses()
    if not courses:
        print("Exiting due to no courses found.")
        exit(1)
        
    documents = embedder.prepare_documents(courses)
    if not documents:
        print("Exiting due to no documents created.")
        exit(1)
        
    vector_store = embedder.create_vector_store(documents)
    if vector_store:
        vector_store.persist()
        print("Process completed successfully!")
    else:
        print("Failed to create vector store.")
        exit(1) 
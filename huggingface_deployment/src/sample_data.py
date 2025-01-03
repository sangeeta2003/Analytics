import json
import os

sample_courses = [
    {
        "title": "Python for Data Science",
        "description": "A comprehensive course covering Python fundamentals for data science, including pandas, numpy, and matplotlib.",
        "curriculum": [
            "Introduction to Python",
            "Data Manipulation with Pandas",
            "Numerical Computing with NumPy",
            "Data Visualization with Matplotlib",
            "Basic Statistics in Python"
        ],
        "tags": ["python", "data science", "beginner"],
        "duration": "6 weeks",
        "level": "Beginner"
    },
    {
        "title": "Machine Learning Fundamentals",
        "description": "Learn core machine learning concepts and algorithms with practical implementations.",
        "curriculum": [
            "Introduction to ML",
            "Supervised Learning",
            "Unsupervised Learning",
            "Model Evaluation",
            "Feature Engineering"
        ],
        "tags": ["machine learning", "AI", "intermediate"],
        "duration": "8 weeks",
        "level": "Intermediate"
    },
    {
        "title": "Deep Learning with PyTorch",
        "description": "Master deep learning concepts and implement neural networks using PyTorch.",
        "curriculum": [
            "Neural Networks Basics",
            "Convolutional Neural Networks",
            "Recurrent Neural Networks",
            "Transfer Learning",
            "Model Deployment"
        ],
        "tags": ["deep learning", "pytorch", "advanced"],
        "duration": "10 weeks",
        "level": "Advanced"
    }
]

def create_sample_data(filename='data/courses.json'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(sample_courses, f, indent=4, ensure_ascii=False)
    print(f"Created sample data with {len(sample_courses)} courses")

if __name__ == "__main__":
    create_sample_data() 
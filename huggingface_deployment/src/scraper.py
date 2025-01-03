import requests
import json
import os
import logging
import time
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CoursesScraper:
    def __init__(self):
        self.base_url = "https://courses.analyticsvidhya.com"
        self.api_url = "https://courses.analyticsvidhya.com/api/v1/courses"
        self.courses = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Referer': 'https://courses.analyticsvidhya.com/courses'
        }
        logger.info(f"Initializing scraper")

    def get_courses(self):
        try:
            logger.info("Fetching courses from API...")
            response = requests.get(self.api_url, headers=self.headers)
            response.raise_for_status()
            
            courses_data = response.json()
            logger.info(f"Found {len(courses_data)} courses")
            
            for course in courses_data:
                if course.get('is_free', False) or course.get('price', 0) == 0:
                    course_info = {
                        'title': course.get('name', ''),
                        'description': course.get('description', ''),
                        'curriculum': course.get('curriculum', []),
                        'url': urljoin(self.base_url, f"/courses/{course.get('slug', '')}")
                    }
                    self.courses.append(course_info)
                    logger.info(f"Added course: {course_info['title']}")
                    
            logger.info(f"Successfully processed {len(self.courses)} free courses")
            return self.courses
            
        except requests.RequestException as e:
            logger.error(f"Error fetching courses: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return []

    def save_courses(self, filename='data/courses.json'):
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.courses, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved {len(self.courses)} courses to {filename}")
        except Exception as e:
            logger.error(f"Error saving courses to file: {filename}")
            logger.error(f"Error details: {str(e)}")

if __name__ == "__main__":
    scraper = CoursesScraper()
    courses = scraper.get_courses()
    if courses:
        scraper.save_courses()
    else:
        logger.error("No courses were scraped!") 
import os
from typing import Optional
from dotenv import load_dotenv
from google import genai
from utils.config import SYSTEM_PROMPT

load_dotenv()

class LLMClient:
    """Client for interacting with Gemini API for campus event Q&A."""
    
    def __init__(self, api_key: Optional[str] = None):
        # Initialize the API key from parameter or environment variable
        gemini_api_key = api_key or os.getenv("GEMINI_API_KEY")
        
        # Raise ValueError if no API key found
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY is not set in the environment variables")
        
        # Initialize the genai Client with API key
        self.client = genai.Client(api_key=gemini_api_key)
    
    def call_api(self, user_query: str) -> str:
        """Call Gemini API with system prompt and user query."""
        try:
            # Format the prompt with user query
            full_prompt = f"{SYSTEM_PROMPT}\n\nStudent Query: {user_query}\n\nAnswer:"
            
            # Make API call to Gemini LLM
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=full_prompt
            )
            
            # Handle empty or None response
            if not response or not response.text:
                return "Error: Empty response from Gemini API. Please try again."
            
            # Return the response text
            return response.text.strip()
        
        except Exception as e:
            return f"Error: {str(e)}"


def answer_student_query(query: str) -> str:
    """Answer a student's query about campus events."""
    try:
        # Create llmClient instance
        client = LLMClient()
        
        # Call the API
        response = client.call_api(query)
        
        # Return the response
        return response
    
    except ValueError as e:
        # Handle ValueError (missing API key)
        return f"Configuration Error: {str(e)}"
    
    except Exception as e:
        # Handle all other exceptions and return error message
        return f"Error occurred while processing your query: {str(e)}"


def main():
    """Main function to run specific test queries."""
    test_queries = [
        "how is weather today?",
        "Give me detials about tech fest in september."
    ]
    
    print("Campus Event Q&A Assistant - Test Results")
    print("=" * 60)
    
    for idx, query in enumerate(test_queries, 1):
        print(f"\nTest Query {idx}:")
        print(f"Question: {query}")
        print("-" * 60)
        result = answer_student_query(query)
        print(f"Response:\n{result}")
        print("=" * 60)


if __name__ == "__main__":
    main()

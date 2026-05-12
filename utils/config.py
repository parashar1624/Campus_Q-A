"""
Configuration file for Campus Event Q&A Assistant.
Handles loading the system prompt from prompt.txt file.
"""

import os


def load_system_prompt() -> str:
    """Load the system prompt from prompt.txt file."""
    try:
        # Get the path to prompt.txt file (relative to this config.py file)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_file_path = os.path.join(os.path.dirname(current_dir), "prompt.txt")
        
        # Open and read the prompt file
        with open(prompt_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Return the content stripped of whitespace
        return content.strip()
    
    except FileNotFoundError:
        raise FileNotFoundError(f"prompt.txt file not found at {prompt_file_path}")
    
    except Exception as e:
        raise RuntimeError(f"Error reading prompt.txt file: {str(e)}")


def get_system_prompt() -> str:
    """Get the system prompt with user query placeholder."""
    # Call load_system_prompt() and return the result
    return load_system_prompt()


# Export the system prompt as SYSTEM_PROMPT
SYSTEM_PROMPT = get_system_prompt()

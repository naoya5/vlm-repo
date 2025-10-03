"""
VLM (Vision Language Model) implementation using API.
This script demonstrates how to use OpenAI's GPT-4 Vision API to analyze images.
"""

import os
import sys
import base64
from openai import OpenAI


def encode_image(image_path):
    """
    Encode an image to base64 string.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        str: Base64 encoded image string
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def analyze_image_with_api(image_path, question, api_key=None, model="gpt-4o"):
    """
    Analyze an image using OpenAI's Vision API.
    
    Args:
        image_path: Path to the image file
        question: Question to ask about the image
        api_key: OpenAI API key (if None, reads from OPENAI_API_KEY env variable)
        model: Model to use (default: gpt-4o)
        
    Returns:
        str: The model's answer
    """
    # Get API key
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY environment variable not set"
    
    # Initialize client
    client = OpenAI(api_key=api_key)
    
    # Encode image
    try:
        base64_image = encode_image(image_path)
    except Exception as e:
        return f"Error encoding image: {e}"
    
    # Create the message
    try:
        print("Sending request to OpenAI API...")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error calling API: {e}"


def main():
    """
    Main function to demonstrate VLM API usage.
    """
    print("=== VLM with API (OpenAI GPT-4 Vision) ===\n")
    
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Usage: python vlm_api.py <image_path> <question>")
        print("\nExample:")
        print('  python vlm_api.py sample.jpg "What is in this image?"')
        print("\nNote: Set OPENAI_API_KEY environment variable before running:")
        print('  export OPENAI_API_KEY="your-api-key-here"')
        return
    
    image_path = sys.argv[1]
    question = sys.argv[2]
    
    # Check if API key is set
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        print("\nPlease set your OpenAI API key:")
        print('  export OPENAI_API_KEY="your-api-key-here"')
        return
    
    # Analyze image
    print(f"Image: {image_path}")
    print(f"Question: {question}\n")
    
    answer = analyze_image_with_api(image_path, question)
    
    print("Answer:")
    print(answer)


if __name__ == "__main__":
    main()

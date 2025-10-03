"""
VLM (Vision Language Model) implementation using Transformers library.
This script demonstrates how to use a vision-language model to analyze images and answer questions.
"""

import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import sys


def load_model(model_name="microsoft/Phi-3.5-vision-instruct"):
    """
    Load a vision-language model and its processor.
    
    Args:
        model_name: The name of the model to load from HuggingFace Hub
        
    Returns:
        processor: The model processor
        model: The loaded model
    """
    print(f"Loading model: {model_name}...")
    processor = AutoProcessor.from_pretrained(
        model_name,
        trust_remote_code=True
    )
    model = AutoModelForVision2Seq.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        trust_remote_code=True,
        device_map="auto" if torch.cuda.is_available() else None
    )
    print("Model loaded successfully!")
    return processor, model


def analyze_image(image_path, question, processor, model):
    """
    Analyze an image and answer a question about it.
    
    Args:
        image_path: Path to the image file
        question: Question to ask about the image
        processor: The model processor
        model: The loaded model
        
    Returns:
        str: The model's answer
    """
    # Load image
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        return f"Error loading image: {e}"
    
    # Prepare the prompt
    messages = [
        {
            "role": "user",
            "content": f"<|image_1|>\n{question}"
        }
    ]
    
    # Process inputs
    prompt = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = processor(
        prompt,
        [image],
        return_tensors="pt"
    )
    
    # Move to the same device as the model
    if torch.cuda.is_available():
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
    # Generate response
    print("Generating response...")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=500,
            do_sample=False
        )
    
    # Decode the response
    response = processor.decode(outputs[0], skip_special_tokens=True)
    
    # Extract the assistant's response
    if "<|assistant|>" in response:
        response = response.split("<|assistant|>")[-1].strip()
    
    return response


def main():
    """
    Main function to demonstrate VLM usage.
    """
    print("=== VLM with Transformers ===\n")
    
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Usage: python vlm_transformers.py <image_path> <question>")
        print("\nExample:")
        print('  python vlm_transformers.py sample.jpg "What is in this image?"')
        print("\nNote: This will download a large model (several GB) on first run.")
        return
    
    image_path = sys.argv[1]
    question = sys.argv[2]
    
    # Load model
    try:
        processor, model = load_model()
    except Exception as e:
        print(f"Error loading model: {e}")
        print("\nNote: This requires a model that supports vision-language tasks.")
        print("You may need to install additional dependencies or use a different model.")
        return
    
    # Analyze image
    print(f"\nImage: {image_path}")
    print(f"Question: {question}\n")
    
    answer = analyze_image(image_path, question, processor, model)
    
    print("Answer:")
    print(answer)


if __name__ == "__main__":
    main()

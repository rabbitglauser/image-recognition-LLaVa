"""
The script conducts a series of interactions with the `ollama` language model to generate descriptions and perform visual analysis on images.
Also it uses two different models for two different tasks

Requirements:
The script uses the `ollama` library.

Execution:
Run the script in a Python environment where the `ollama` library is installed.
"""

import ollama  # Import the ollama library


def interact_with_model(model, messages, stream=False):
    """
    Function to interact with different models

    Parameters:
        model (str): The model's name
        messages (list): List of dictionaries each representing a user's interaction
        stream (boolean): Whether to stream the response, default is False

    Returns:
        Response from the interaction
    """

    response = ollama.chat(model=model, messages=messages, stream=stream)

    if stream:  # If it's a streaming response, join the chunks and return
        return ''.join(chunk['message']['content'] for chunk in response if 'content' in chunk['message'])

    return response  # Return the standard response otherwise


# Messages to be used for the interactions
messages = [
    {'role': 'user',
     'content': 'How many houses are in this image?',
     'image': ['./image1.jpg']},
    {'role': 'user',
     'content': 'Describe this image',
     'image': ['./image1.jpg']},
    {'role': 'user',
     'content': 'Provide five keywords describing the image (separated by commas)',
     'image': ['./image1.jpg']},
    {'role': 'user',
     'content': 'Describe the colors in the image',
     'image': ['./image1.jpg']}
]

# Interact with the 'llava:13b' model
res = interact_with_model('llava:13b', messages)

# Interact with the 'llama2' model with a stream
stream_res = interact_with_model('llama2', [{'role': 'user', 'content': 'Why is the sky blue?'}], True)

# Single interaction with 'llama2' model
single_chat_res = interact_with_model('llama2', [{'role': 'user', 'content': 'Why is the sky blue?'}])

# Print responses
print(f"Content from model 'llava:13b': {res.get('message', {}).get('content')}")
print(f"Image from model 'llava:13b': {res.get('message', {}).get('image')}")



print(f"Stream response from model 'llama2': {stream_res}")
print(f"Single chat response from model 'llama2': {single_chat_res['message'].get('content')}")


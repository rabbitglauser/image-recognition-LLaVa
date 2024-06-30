"""
The script conducts a series of interactions with the `ollama` language model to generate descriptions and perform visual analysis of provided images.

Requirements:
The script uses the `ollama` library.

Execution:
Run the script in a Python environment where the `ollama` library is installed.

Here's a brief explanation of what the code does:

"""

import ollama  # Import the ollama library.

# Call the `ollama` chat API with various requests. The 'messages' argument contains a list of dictionaries.
# Each dictionary represents an interaction with the `ollama` model.
res = ollama.chat(
    model='llava:13b',  # Specify the model.
    messages=[
        # Ask the model to count the number of houses in the image.
        {'role': 'user',
         'content': 'How many houses are in this image?',
         'image': ['./image1.jpg']},

        # Ask the model to describe the image.
        {'role': 'user',
         'content': 'Describe this image',
         'image': ['./image1.jpg']},

        # Ask the model to provide five keywords that describe the image.
        {'role': 'user',
         'content': 'Provide five keywords describing the image (separated by commas)',
         'image': ['./image1.jpg']},

        # Ask the model to describe the colors in the image.
        {'role': 'user',
         'content': 'Describe the colors in the image',
         'image': ['./image1.jpg']},
    ]
)

# Print the 'content' and 'image' keys from the response to the console.
# As these keys may not always be present, we use the .get() method to avoid KeyErrors.
# If the keys are not present, None will be printed instead.
print(res['message'].get('content'))
print(res['message'].get('image'))

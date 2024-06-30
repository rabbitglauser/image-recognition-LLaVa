import ollama

res = ollama.chat(
    model='llava:13b',
    messages=[
        {'role': 'user',
         'content': 'How many houses are in this image?',
         'image': ['./image1.jpg']},

        {'role': 'user',
         'content': 'Describe this image',
         'image': ['./image1.jpg']},

        {'role': 'user',
         'content': 'Provide five keywords describing the image (separated by comas)',
         'image': ['./image1.jpg']},
    ]
)

print(res['message'].get('content'))
print(res['message'].get('image'))



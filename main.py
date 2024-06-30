import ollama

res = ollama.chat(
    model='llava',
    messages=[
        {'role': 'user',
         'content': 'How many houses are in this image?',
         'image': ['./image1.jpg']},

        {'role': 'user',
         'content': 'Describe this image',
         'image': ['./image1.jpg']}
    ]
)

print(res['message']['content'])
print(res['message']['image'])


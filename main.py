import ollama

res = ollama.chat(
    model='llava:13b',
    messages=[{'role': 'user',
               'content': 'Describe this image',
               'image': ['./image1.jpg']}
              ]
)

print(res['message']['content'])


import ollama

response = ollama.chat(
    model='llava:7b', 
    messages=[{
        'role': 'user', 
        'content': 'Crée moi une histoire pour enfants inspirée de mon image',
        'images': ["static/Images/23.jpg"]  
    }]
)

print(response.message.content)


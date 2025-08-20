from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
# import ollama
from openai import OpenAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chat")
def chat(question: str = Query(...)):
    print('***********',question)

    client = OpenAI(api_key="sk-6b79b883eabe436aa42d4ea8bdda0b84", base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Who is PM of India?"},
        ],
        stream=False
    )
    return StreamingResponse(response.choices[0].message.content, media_type="text/plain")
    
    def generate():
        print('***********',question)
        stream = ollama.chat(
            model='smollm:latest',
            messages=[
                {
                    'role': 'user',
                    'content': question,
                },
            ],
            options={
                'num_predict': 50
            },
            stream=True
        )
        for chunk in stream:
            print('$$$$$$$$$$', chunk['message']['content'])
            yield chunk['message']['content']
    # print('@@@@@@@@@@@',StreamingResponse(generate(), media_type="text/plain")) 
    return StreamingResponse(generate(), media_type="text/plain")

# import ollama

# # Start streaming chat response from the model
# stream = ollama.chat(
#     model='smollm:latest',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Tell me only name of the current PM of India?',
#         },
#     ],
#     options={
#         'num_predict': 50
#     },
#     stream=True
# )

# # Read each streamed chunk and print immediately
# for chunk in stream:
#     content = chunk['message']['content']
#     print(content, end='', flush=True)

# print()  # final newline

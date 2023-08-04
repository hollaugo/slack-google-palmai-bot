import vertexai
from vertexai.preview.language_models import ChatModel

vertexai.init(project="prompt-circle-learn", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0,
    "max_output_tokens": 1024
}
chat = chat_model.start_chat()
response = chat.send_message("""Hello there""", **parameters)
print(f"Response from Model: {response.text}")
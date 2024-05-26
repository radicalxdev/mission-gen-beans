import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession

vertexai.init()

system_instruction = ["Don't use technical terms in your response"]
model = GenerativeModel(model_name="gemini-1.0-pro-002", system_instruction=system_instruction)

chat = model.start_chat()


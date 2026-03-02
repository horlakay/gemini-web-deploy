# The code snippet is loading a pre-trained AI model called Gemini (model-id) on Vertex AI.
# The code calls the send_message method of the loaded Gemini model.
# The code uses Gemini's ability to chat. It uses the text provided in the prompt to chat.

from google import genai
from google.genai.types import HttpOptions

import logging
from google.cloud import logging as gcp_logging

# ------  Below cloud logging code is for Qwiklab's internal use, do not edit/remove it. --------
# Initialize GCP logging

gcp_logging_client = gcp_logging.Client()
gcp_logging_client.setup_logging()

client = genai.Client(
    vertexai=True,
    project='"project-id"',
    location='"REGION"',
    http_options=HttpOptions(api_version="v1")
)
chat = client.chats.create(model="model-id")
response_text = ""

for chunk in chat.send_message_stream("What are all the colors in a rainbow?"):
    print(chunk.text, end="")
    response_text += chunk.text

# The code snippet is loading a pre-trained AI model called Gemini (model-id) on Vertex AI.
# The code calls the send_message_stream method of the loaded Gemini model.
# The code uses Gemini's ability to understand prompts and have a stateful chat conversation.

from google import genai
from google.genai.types import HttpOptions

import logging
from google.cloud import logging as gcp_logging

# ------  Below cloud logging code is for Qwiklab's internal use, do not edit/remove it. --------
# Initialize GCP logging
gcp_logging_client = gcp_logging.Client()
gcp_logging_client.setup_logging()

client = genai.Client(
    vertexai=True,
    project='"project-id"',
    location='"REGION"',
    http_options=HttpOptions(api_version="v1")
)
chat = client.chats.create(model="model-id")
response_text = ""

for chunk in chat.send_message_stream("What are all the colors in a rainbow?"):
    print(chunk.text, end="")
    response_text += chunk.text


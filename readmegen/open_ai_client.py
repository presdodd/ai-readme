from openai import OpenAI
from readmegen.scanner import build_context

class OpenAiClient():
    def __init__(self, key):
        if key:
            self.client = OpenAI(api_key=key)
        else :
            self.client = OpenAI()

    # response = client.responses.create(
    #     model="gpt-4.1",
    #     input="Write a one-sentence bedtime story about a unicorn."
    # )

    # print(response.output_text)

    def prompt(self, p :str):
        response = self.client.request.create(
            model="gpt-4.1",
            input=p
        )

        return response
    

    def generate_readme(self, directory :str):
        file_texts = build_context(directory)

        response = self.client.responses.create(
            model="gpt-4.1",
            input=[
                {
                    "role": "developer",
                    "content": ("You are a senior developer tasked with writing a README.md file. "
                                "Respond only in the .md format. "
                                "Use the following context to understand the project structure, purpose, and dependencies.")
                },
                {
                    "role": "user",
                    "content": file_texts
                }
            ]
        )

        return response


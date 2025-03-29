from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_answer(client, file, question):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_id": file.id,
                    },
                    {
                        "type": "input_text",
                        "text": question,
                    },
                ]
            }
        ]
    )
    return response.output_text


def main():
    client = OpenAI()
    file = client.files.create(
        file=open("1-s2.0-S8756328225000341-main.pdf", "rb"),
        purpose="user_data"
    )

    print(get_answer(client, file, "How were detection channels set up?"))


if __name__ == "__main__":
    main()

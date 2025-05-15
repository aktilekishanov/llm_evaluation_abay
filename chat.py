from openai import OpenAI
import json

client = OpenAI()


def translate_text_kazakh_to_english(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional translator that translates text from Kazakh to English."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def translate_json_file(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        for entry in data["texts"]:
            print(f"Translating passage ID {entry['id']}...")
            translated_text = translate_text_kazakh_to_english(
                entry["content"])
            entry["translated_content"] = translated_text

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Translation completed! Translated JSON saved to {output_file}")

    except Exception as e:
        print(f"Error: {str(e)}")


input_file = "kazakh.json"
output_file = "kazakh_translated.json"
translate_json_file(input_file, output_file)

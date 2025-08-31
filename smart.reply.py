import openai

openai.api_key = "YOUR_OPENAI_KEY"

def generate_reply(comment):
    prompt = f"رد قصير وودود على التعليق التالي: {comment}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print(generate_reply("الفيديو رائع جدًا!"))

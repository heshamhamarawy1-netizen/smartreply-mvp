from flask import Flask, render_template, request
from youtube_comments import get_comments
from sentiment import classify_comment
from smart_reply import generate_reply
import re

app = Flask(__name__)

# دالة لاستخراج video_id من رابط اليوتيوب
def extract_video_id(url):
    pattern = r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

@app.route("/", methods=["GET", "POST"])
def home():
    data = []
    if request.method == "POST":
        video_url = request.form.get("video_url")
        video_id = extract_video_id(video_url)
        if video_id:
            comments = get_comments(video_id)
            for c in comments:
                label, score = classify_comment(c)
                reply = generate_reply(c)
                data.append({"comment": c, "label": label, "reply": reply})
        else:
            data.append({"comment": "Invalid YouTube URL", "label": "ERROR", "reply": ""})
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)



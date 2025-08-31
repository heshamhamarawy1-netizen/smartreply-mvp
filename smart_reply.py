# smart_reply.py
def generate_reply(comment: str) -> str:
    comment = comment.lower()
    if "thanks" in comment or "thank you" in comment:
        return "You're welcome! 😊"
    elif "love" in comment or "great" in comment:
        return "Glad you enjoyed it! 🙌"
    elif "question" in comment or "how" in comment:
        return "Thanks for the question! We'll get back to you soon."
    else:
        return "Thanks for sharing your thoughts!"

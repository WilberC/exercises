def generate_hashtag(s):
    return False if len(s) <= 0 or len(s) > 144 else f"#{s.title().replace(' ', '')}"

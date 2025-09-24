def validate_post(title, content, category):
    return bool(title and content and category)

CATEGORIES = ["Technology", "Lifestyle", "Education", "Other"]

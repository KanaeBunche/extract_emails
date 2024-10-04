import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    unique_emails = list(set(emails))
    return unique_emails

# Example usage
text = "Contact us at support@example.com or sales@example.com. You can also reach john.doe@company.com for more info."
print(extract_emails(text))

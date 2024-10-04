import re
from collections import defaultdict

def extract_emails(text):
    # Regular expression to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the given text
    found_emails = re.findall(email_pattern, text)
    
    # Use a set to store unique emails
    unique_emails = set(found_emails)
    
    # Dictionary to categorize emails by domain
    categorized_emails = defaultdict(list)

    # Categorize emails by their domain
    for email in unique_emails:
        domain = email.split('@')[1]  # Get the domain part of the email
        categorized_emails[domain].append(email)  # Append the email to the appropriate domain list

    return categorized_emails

# Example usage
text = """
    Here are some emails: user@example.com, admin@test.com, support@example.com, user@example.com
    Don't forget to contact info@domain.com or feedback@test.com.
"""
categorized_result = extract_emails(text)

# The function returns a dictionary where keys are domains and values are lists of unique emails
print(categorized_result)

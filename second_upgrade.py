import re
from collections import defaultdict

def extract_emails(text):
    # Regular expression for validating email format, accounting for special characters
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Dictionary to hold email categories by domain
    emails_by_domain = defaultdict(lambda: {'emails': set(), 'count': 0})
    invalid_emails = []  # List to log invalid emails

    # Find all emails in the text
    found_emails = re.findall(email_pattern, text)

    for email in found_emails:
        domain = email.split('@')[1]
        emails_by_domain[domain]['emails'].add(email)  # Store unique emails
        emails_by_domain[domain]['count'] += 1         # Increment count

    # Check for any email formats that do not match the valid pattern
    all_found_emails = text.split()  # Split text into words to find potentially invalid emails
    for word in all_found_emails:
        if '@' in word and not re.match(email_pattern, word):
            invalid_emails.append(word)  # Log invalid email formats

    # Convert sets back to lists for final output
    for domain in emails_by_domain:
        emails_by_domain[domain]['emails'] = list(emails_by_domain[domain]['emails'])

    # Print or handle invalid emails as necessary
    if invalid_emails:
        print("Invalid emails found:", invalid_emails)

    return emails_by_domain

# Example usage
text = "Contact us at support@example.com or sales@example.com. Also, reach out to invalid_email@.com."
result = extract_emails(text)
print(result)

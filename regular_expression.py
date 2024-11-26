import re
def extract_emails(text):
    email_pattern=r'[a_zA_Z0_9_%+-]+@[a_ZA_Z0_a_]+\[a_zA-Z]{2,}'
    return re.findall(email_pattern,text)
sample_text="Please contact us at support@example.com or sales@example.org."
emails=extract_emails(sample_text)
print("Extracted email:",emails)


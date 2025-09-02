# List of spam phrases
spam_phrases = ["buy now", "follow me", "like this", "subscribe"]

# Take input and convert to lowercase
comment = input("Enter your comment: ").lower()

# Check for spam
found_spam = None
for phrase in spam_phrases:
    if phrase in comment:
        found_spam = phrase
        break

# Output result
if found_spam:
    print(f"This is a spam comment (contains: '{found_spam}')")
else:
    print("This is not a spam comment")

import os

TEXT = "The reply-all button should come with a warning label, because one person says 'thanks!' to four hundred strangers and suddenly my inbox is a group chat of people I have never met, all agreeing loudly about lunch."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    content = TEXT
    f.write(content)

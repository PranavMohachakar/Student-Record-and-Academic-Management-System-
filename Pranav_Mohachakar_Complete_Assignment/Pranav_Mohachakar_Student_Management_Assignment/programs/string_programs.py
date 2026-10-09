"""String exercises: name formatting, email validation, and word counting."""
def main():
    name = input("Enter student name: ").strip()
    print("Formatted name:", name.title())
    email = input("Enter email: ").strip()
    print("Email contains @:", "@" in email and "." in email.split("@")[-1])
    sentence = input("Enter a sentence: ").strip()
    print("Word count:", len(sentence.split()))
if __name__ == "__main__":
    main()

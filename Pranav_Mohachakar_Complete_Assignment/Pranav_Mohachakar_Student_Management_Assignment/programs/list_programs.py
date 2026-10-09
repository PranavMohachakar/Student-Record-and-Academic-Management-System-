"""List exercises for student marks."""
def main():
    raw = input("Enter marks separated by commas: ")
    try:
        marks = [float(x.strip()) for x in raw.split(",") if x.strip()]
        if not marks or any(x < 0 or x > 100 for x in marks):
            raise ValueError
    except ValueError:
        print("Enter one or more marks between 0 and 100.")
        return
    print("Marks:", marks)
    print("Sorted marks:", sorted(marks))
    print("Average:", sum(marks) / len(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
if __name__ == "__main__":
    main()

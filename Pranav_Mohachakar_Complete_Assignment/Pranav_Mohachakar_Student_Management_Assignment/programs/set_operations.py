"""Set operations: unique departments and subjects."""
def main():
    departments = {"AI & ML", "Computer", "IT", "AI & ML"}
    subjects_sem1 = {"Python", "Maths", "Physics"}
    subjects_sem2 = {"Python", "Data Science", "Maths"}
    print("Unique departments:", departments)
    print("All subjects:", subjects_sem1 | subjects_sem2)
    print("Common subjects:", subjects_sem1 & subjects_sem2)
    print("Only semester 1:", subjects_sem1 - subjects_sem2)
if __name__ == "__main__":
    main()

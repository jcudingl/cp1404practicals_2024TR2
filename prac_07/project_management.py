from prac_07.project import Project
import datetime
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    projects = load_projects(FILENAME, projects)
    display_menu()
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename, projects)
        elif choice == "s":
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)  # Pass the 'projects' list to the function
        elif choice == 'f':
            start_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(start_date, projects)  # Pass 'start_date' and 'projects' list to the function
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        display_menu()
        choice = input(">>> ").lower()
    if input(f"Would you like to save to {FILENAME}? (yes/no): ").lower() == "yes":
        save_projects(FILENAME, projects)  # Pass "projects.txt" and projects
    print("Thank you for using the project management software.")


def display_menu():
    """Print menu"""
    print(MENU)


def load_projects(filename, projects):
    """Load projects from a file"""
    try:
        with open(filename, "r") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')  # Assuming tab-separated values
                project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
                projects.append(project)
        print(f"Loaded {len(projects)} projects from projects.txt")
        return projects
    except FileNotFoundError:
        print("File not found.")


def save_projects(filename, projects):
    """Save projects in a file"""
    with open(filename, "w")as out_file:
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display all projects, separated into incomplete and completed categories."""
    # Separating projects based on their completion status
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    # Displaying incomplete projects
    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):  # Sort by priority
        # Assuming project object has a string representation method defined (__str__)
        # Otherwise, format the print statement according to project attributes
        print(project)

    # Displaying completed projects
    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):  # Similarly sorting by priority
        print(project)


def filter_projects_by_date(start_date, projects):
    """Filter projects in list by start date"""
    filtered_projects = [project for project in projects if project.start_date >
                         datetime.datetime.strptime(start_date, "%d/%m/%Y").date()]
    print("Projects starting after", start_date)
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)  # You might want to adjust the print format here


def add_new_project(projects):
    """Add a new project."""
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    # Convert start date from string to datetime.date object
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    # Create and add the new project
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]

    new_percentage = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()

    if new_percentage:
        selected_project.completion_percentage = int(new_percentage)
    if new_priority:
        selected_project.priority = int(new_priority)


main()

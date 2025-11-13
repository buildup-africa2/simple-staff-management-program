"""Utility functions for the application."""
from database import staff_db
import sqlite3


def validate_role(role):
    """Validate if the given role is valid."""
    valid_roles = [
        "admin",
        "cleaner",
        "manager",
        "cook",
        "driver",
        "personal_assistant",
        "security",
        "accountant",
        "receptionist"
    ]
    if role.lower() in valid_roles:
        return True
    else:
        return False

def check_email_exists(email):
    """Check if an email already exists in the database."""
    email= email.lower()
    for staff in staff_db:
        if staff["email"] == email.lower():
            return True
    return False



def add_staff_member(name, role, email,password = "1234"):
    """Add a new staff member to the database."""
    # check if the user exists
    if check_email_exists(email):
        raise ValueError("User with this email already exists.")
    
    # validate the role
    if not validate_role(role):
        raise ValueError("Invalid role provided.")
    
    user_default = {
        "password": password,
        "salary": None,
        "hire_date": None,
        "is_active": True,
        "age": None,
        "address": None,
        "phone_number": None
    }
    
    data = {
        "id": len(staff_db) + 1,
        "name": name,
        "role": role,
        "email": email.lower()
    }

    new_staff = data | user_default

    staff_db.append(new_staff)
    return "Staff member added successfully."


def get_all_staff():
    """Retrieve all staff members from the database."""
    return staff_db


def filter_staff_by_role(role):
    """Filter staff members by their role."""
    users = []
    for staff in staff_db:
        if staff["role"] == role.lower():
            users.append(staff)
    return users


def get_single_staff_member(staff_id):
    """Retrieve a single staff member by their ID."""
    for staff in staff_db:
        if staff["id"] == int(staff_id):
            return staff
    raise ValueError(f"Staff member with this ID '{staff_id}' does not exist.")


def suspend_staff_member(staff_id):
    """Sack a staff member by their ID."""
    staff_to_suspend = None
    get_single_staff_member(staff_id)
    
    if staff_to_suspend["role"] == "admin":
        raise PermissionError("Admin cannot be suspended.")
    staff_to_suspend["is_active"] = False
    return staff_to_suspend
   

def update_staff_member(staff_id, **kwargs):
    """Update details of a staff member."""
    
    staff_update = None
    for staff in staff_db:
        if staff["id"] == int(staff_id):
            staff_update = staff
            break
        if staff_update:
            for key, value in kwargs.items():
                if key in staff_update:
                    staff_update[key] = value
                return staff_update
    raise ValueError(f"Staff member with this ID '{staff_id}'does not exist.")



def delete_staff_member(staff_id):
    """Delete a staff member by their ID."""
    for index, staff in enumerate(staff_db):
        if staff["id"] == int(staff_id):
            del staff_db[index]
            return f"Staff member with ID '{staff_id}' has been deleted."
    raise ValueError(f"Staff member with this ID '{staff_id}' does not exist.")

def admin_login(email, password):
    """Authenticate an admin user."""
    # check if the email exists
    for staff in staff_db:
        if staff["email"] == email.lower():
            user = staff
            if user is None:
                raise ValueError("User with this email does not exist")        
                    
                    # check if password is correct
            if staff["password"] != password:
                raise ValueError("Incorrect password.")
                
                # check if user is admin
            if staff["role"] != "admin":
                raise PermissionError("User is not an admin.")
            return staff 
    raise ValueError("User with this email does not exist")

def login_user(email,password):
    # login any user by email and password
    for staff in staff_db:
        if staff["email"] == email.lower():
            if staff["password"] != password:
                raise ValueError("Incorrect password.")
            return staff
    raise ValueError("User with this email does not exist")




def show_menu(role,permissions):
# menu display based on role 
    allowed_actions = permissions.get(role, [])
    while True:
        print("\n What would you like to do?")
        for i, func in enumerate(allowed_actions, start=1):
            print(f"{i}. {func.__name__}")
        print(f"{len(allowed_actions)+1}. Logout")
        choice = input("Enter your choice: ")
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        choice = int(choice)
        if 1 <= choice <= len(allowed_actions):
            allowed_actions[choice - 1]()
        elif choice == len(allowed_actions) + 1:
            print("Logging out...")
            break   
        else:
            print("Invalid choice. Please try again.")
    

          

            







    
"""Utility functions for the application."""
from database import staff_db


def validate_role(role):
    """Validate if the given role is valid."""
    valid_roles = [
        "admin",
        "cleaner",
        "manager",
        "cook",
        "driver",
        "personal_assistant",
        "security"
    ]
    if role.lower() in valid_roles:
        return True
    else:
        return False

def check_email_exists(email):
    """Check if an email already exists in the database."""
    for staff in staff_db:
        if staff["email"] == email.lower():
            return True
    return False



def add_staff_member(name, role, email):
    """Add a new staff member to the database."""
    # check if the user exists
    if check_email_exists(email):
        raise ValueError("User with this email already exists.")
    
    # validate the role
    if not validate_role(role):
        raise ValueError("Invalid role provided.")
    
    user_default = {
        "password": None,
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
    pass


def get_single_staff_member(staff_id):
    """Retrieve a single staff member by their ID."""
    for staff in staff_db:
        if staff["id"] == int(staff_id):
            return staff
    raise ValueError(f"Staff member with this ID '{staff_id}' does not exist.")


def suspend_staff_member(staff_id):
    """Sack a staff member by their ID."""
    staff_to_suspend = None
    for staff in staff_db:
        if staff["id"] == int(staff_id):
            staff_to_suspend = staff
            break
    if staff_to_suspend:
        if staff_to_suspend["role"] == "admin":
            raise PermissionError("Admin cannot be suspended.")
        staff_to_suspend["is_active"] = False
        return staff_to_suspend
    else:
        raise ValueError(f"Staff member with this ID '{staff_id}' does not exist.")

def update_staff_member(staff_id, **kwargs):
    """Update details of a staff member."""
    pass

def delete_staff_member(staff_id):
    """Delete a staff member by their ID."""
    pass

def admin_login(email, password):
    """Authenticate an admin user."""
    # check if the email exists
    for staff in staff_db:
        if not staff["email"] == email.lower():
            raise ValueError("User with this email does not exist.")
        
        # check if password is correct
        if not staff["password"] == password:
            raise ValueError("Incorrect password.")
        
        # check if user is admin
        if staff["role"] != "admin":
            raise PermissionError("User is not an admin.")
        
        return staff
    



    
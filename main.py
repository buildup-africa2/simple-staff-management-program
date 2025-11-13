"""Main module for the application."""
import json

from utils import (
    add_staff_member,
    
    get_all_staff,
    get_single_staff_member,
    suspend_staff_member,
    filter_staff_by_role,
    update_staff_member,
    delete_staff_member,
    show_menu,
    login_user
)
print("=====================================================")
print("     Welcome to the Staff Management System")
print("=====================================================")


def handle_get_all_staff():
    # allow admin to get all staff members
    action = input("Do you want to view all staff members? (yes/no): ")
    if action.lower() == "yes":
        staff_members = get_all_staff()
        print(json.dumps(staff_members, indent=2))
    else:
        print("Exiting the application.")

def handle_add_staff_member():
    # add staffs to the db
    action = input("Do you want to add a new staff member? (yes/no): ")
    if action.lower() == "yes":
        name = input("Enter staff member's name: ")
        role = input("Enter staff member's role: ")
        email = input("Enter staff member's email: ")
        try:
            resp = add_staff_member(name, role, email)
            print(resp)

            print("\n\n")
            staff_members = get_all_staff()
            print(json.dumps(staff_members, indent=2))

        except ValueError as e:
            print(f"Failed to add staff member: {e}")
    else:
        print("No new staff member added.")

def handle_get_a_single_staff():   
     # get a single staff member by id
    action = input("Do you want to view a single staff member? (yes/no): ")
    if action.lower() == "yes":
        staff_id = input("Enter staff member's ID: ")
        try:
            staff_member = get_single_staff_member(staff_id)
            print(json.dumps(staff_member, indent=2))
        except ValueError as e:
            print(f"Failed to retrieve staff member: {e}")
    else:
        print("Exiting the application.")

def handle_suspend_staff_member():
    # suspend a staff member by id
    action = input("Do you want to suspend a staff member? (yes/no): ")
    if action.lower() == "yes":
        staff_id = input("Enter staff member's ID: ")
        try:
            suspended_staff = suspend_staff_member(staff_id)
            print(f"Staff member with ID {staff_id} has been suspended. \n\n")
            print(json.dumps(suspended_staff, indent=2))
        except ValueError as e:
            print(f"Failed to suspend staff member: {e}")
        except PermissionError as e:
            print(e)
    else:
        print("Exiting the application.")

def handle_filter_staff():
    # filter staff members by role
    action = input("Do you want to filter staff members by role? (yes/no): ")
    if action.lower() == "yes":
        role = input("Enter staff member's role: ")
        try:
            staff_members = filter_staff_by_role(role)
            print(json.dumps(staff_members, indent=2))
        except ValueError as e:
            print(f"Failed to filter staff members: {e}")
    else:
        print("Exiting the application.")

def handle_update_staff_details():
    # update staff member details
    action = input("Do you want to update a staff member's details? (yes/no): ")
    if action.lower() == "yes":
        staff_id = input("Enter staff member's ID: ")
        name = input("Enter new name (no new name? leave blank): ")
        role = input("Enter new role (no new role? leave blank): ")
        email = input("Enter new email (no new email? leave blank): ")
        try:
            update_staff = update_staff_member(staff_id)
            print(f"Staff member with ID {staff_id} has been updated. \n\n")
            print(json.dumps(update_staff, indent = 2))
        except ValueError as e:
            print(f"Faild to update staff member: {e}")
        else:
            print("Exiting the application. ")

def handle_delete_staff_member():
    # delete a staff member by id
    action = input("Do you want to delete a staff member? (yes/no): ")  
    if action.lower() == "yes":
        staff_id = input("Enter staff member's ID: ")
        try:
            resp = delete_staff_member(staff_id)
            print(resp)
        except ValueError as e:
            print(f"Failed to delete staff member: {e}")
    else:
        print("Exiting the application.") 
# Role permissions  
permissions = {
    "admin" : [
        handle_add_staff_member,
        handle_get_all_staff,
        handle_get_a_single_staff,
        handle_suspend_staff_member,
        handle_filter_staff,
        handle_update_staff_details,
        handle_delete_staff_member
     ],
    "driver" : [
        handle_get_all_staff,
        handle_filter_staff,
        handle_get_a_single_staff
    ],
    "cook" : [
        handle_get_all_staff,
        handle_filter_staff,
        handle_get_a_single_staff
    ],
    "accountant" : [
        handle_get_all_staff,
        handle_filter_staff,
        handle_get_a_single_staff
    ],
    "receptionist" : [
        handle_get_all_staff,
        handle_filter_staff,
        handle_get_a_single_staff
    ]
} 

def main():
    """Main function to run the application."""
    
    
    # login the user
    try:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = login_user(email,password)
        print(f"Login successful!, welcome back {user['name']}  you are logged in as {user['role']}")
        print("\n")
        show_menu(role= user['role'], permissions=permissions)
    except ValueError as e:
        print(f"Login failed: {e}")



if __name__ == "__main__":
    main()

    
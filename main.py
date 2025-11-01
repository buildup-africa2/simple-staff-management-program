"""Main module for the application."""
import json

from utils import (
    add_staff_member,
    admin_login,
    get_all_staff,
    get_single_staff_member,
    suspend_staff_member,
    filter_staff_by_role
)


def main():
    """Main function to run the application."""
    # login the user
    # try:
    #     email = input("Enter your email: ")
    #     password = input("Enter your password: ")
    #     user = admin_login(email, password)
    #     print(f"Login successful!, welcome back sir!.{user['name']} {user['role']}")
    #     print("\n\n\n\n\n")
    # except ValueError as e:
    #     print(f"Login failed: {e}")

    # # allow admin to get all staff members
    # action = input("Do you want to view all staff members? (yes/no): ")
    # if action.lower() == "yes":
    #     staff_members = get_all_staff()
    #     print(json.dumps(staff_members, indent=2))
    # else:
    #     print("Exiting the application.")

    # # add staffs to the db
    # action = input("Do you want to add a new staff member? (yes/no): ")
    # if action.lower() == "yes":
    #     name = input("Enter staff member's name: ")
    #     role = input("Enter staff member's role: ")
    #     email = input("Enter staff member's email: ")
    #     try:
    #         resp = add_staff_member(name, role, email)
    #         print(resp)

    #         print("\n\n")
    #         staff_members = get_all_staff()
    #         print(json.dumps(staff_members, indent=2))

    #     except ValueError as e:
    #         print(f"Failed to add staff member: {e}")
    # else:
    #     print("No new staff member added.")

    # # get a single staff member by id
    # action = input("Do you want to view a single staff member? (yes/no): ")
    # if action.lower() == "yes":
    #     staff_id = input("Enter staff member's ID: ")
    #     try:
    #         staff_member = get_single_staff_member(staff_id)
    #         print(json.dumps(staff_member, indent=2))
    #     except ValueError as e:
    #         print(f"Failed to retrieve staff member: {e}")
    # else:
    #     print("Exiting the application.")

    # suspend a staff member by id
    # action = input("Do you want to suspend a staff member? (yes/no): ")
    # if action.lower() == "yes":
    #     staff_id = input("Enter staff member's ID: ")
    #     try:
    #         suspended_staff = suspend_staff_member(staff_id)
    #         print(f"Staff member with ID {staff_id} has been suspended. \n\n")
    #         print(json.dumps(suspended_staff, indent=2))
    #     except ValueError as e:
    #         print(f"Failed to suspend staff member: {e}")
    #     except PermissionError as e:
    #         print(e)
    # else:
    #     print("Exiting the application.")

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




if __name__ == "__main__":
    main()
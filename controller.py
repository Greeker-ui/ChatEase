import database as db
from CTkMessagebox import CTkMessagebox

class Controller:
    def __init__(self, view=None):
        self.view = view

    def submit_action(self):
        username = self.view.username.get().strip()
        password = self.view.password.get().strip()

        if not username or not password:
            CTkMessagebox(title="Error", message="Please fill out all fields!", icon="cancel")
            return False  # Return False on failure

        if db.login_user(username, password):
            CTkMessagebox(title="Success", message="Login Successful!", icon="check")
            print("Logged in as:", username)
            return self.view.open_dashboard()
            
        else:
            return self.view.display_message("Incorrect username/password", "red")
            

    def register_user(self):
        username = self.view.createUsername.get().strip()
        password = self.view.createPassword.get().strip()

        if not username or not password:
            self.view.display_message("Please fill out all fields!", "red")
            return

        if db.register_user(username, password):
            self.view.display_message("Registration Successful!", "green")
        else:
            self.view.display_message("Username already exists", "red")

    def change_password(self, username, old_password, new_password):
        if not username or not old_password or not new_password:
            return False
        elif old_password == new_password:  # Fixed: If same, fail
            return False  # New password cannot be the same as old
        else:
            return db.change_password(username, old_password, new_password)  # Assume DB method takes these args
    
    def message(self, msg):  # Fixed: Added self, made it an instance method
        return db.get_answer(msg)
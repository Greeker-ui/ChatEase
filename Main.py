import database as db
from view import Login_Signup  # Only import what you need
def main():
    db.init_db()
    app = Login_Signup()  # This creates its own controller internally
    app.mainloop()
    
if __name__ == "__main__":
    main()
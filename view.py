import customtkinter as ctk
from PIL import Image, ImageTk, ImageSequence
from CTkMessagebox import CTkMessagebox
from controller import Controller



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class Login_Signup(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controller = Controller(view=self) # Instantiate controller and pass self as view
        self.title("ChatEase")
        self.geometry('1100x700')
        self.minsize(1100, 700)
        self.maxsize(1100, 700)
        self.login_frame()

    def login_frame(self):
        main_frame = ctk.CTkFrame(self, width=1100, height=700, fg_color="#0D1B2A")
        main_frame.pack()
        try:
            self.bg_img = Image.open("main.png")
            self.bg = ctk.CTkImage(light_image=self.bg_img, size=(600, 600))
            self.bg_label = ctk.CTkLabel(main_frame, image=self.bg, text="")
            self.bg_label.place(x=350, y= 100)
        except FileNotFoundError:
            print("Background image not found. Skipping.")

    
        #Main Frame
        self.frame = ctk.CTkFrame(self, 
                                  width=400, 
                                  height=500, 
                                  corner_radius=1, 
                                  fg_color="#13283d")
        self.frame.place(relx=0.4, rely=0.54, anchor="e")

        self.bubble_frame = ctk.CTkFrame(self.frame, width=400, height=100, fg_color="transparent")
        self.bubble_frame.place(x=170, y=6)

        self.another_bubble_frame = ctk.CTkFrame(self.frame, width=400, height=100, fg_color="transparent")
        self.another_bubble_frame.place(x=170, y=70)

        # --- Labels inside bubbles ---
        typing_font = ctk.CTkFont(family="Segoe UI", size=45, weight="bold", slant="italic")
        self.typing_label = ctk.CTkLabel(
            self.bubble_frame,
            text="",
            font=typing_font,
            wraplength=350,
            justify="center",
            text_color="#00BFA5"
        )
        self.typing_label.pack(padx=15, pady=15)

        another_typing_font = ctk.CTkFont(family="Segoe UI", size=15, weight="bold", slant="italic")
        self.another_label = ctk.CTkLabel(
            self.another_bubble_frame,  # <-- place in another bubble
            text="",
            font=another_typing_font,
            wraplength=350,
            justify="center",
            text_color="#00BFA5"
        )
        self.another_label.pack(padx=15, pady=15)

        # --- Typing Text Setup ---
        self.message = "ChatEase"
        self.another_message = "Your Personal\nHelpdesk Companion"
        self.current_index = 0
        self.another_index = 0

        self.type_text()


        self.gif = Image.open("logo.gif")
        self.frames = [ImageTk.PhotoImage(frame.copy(), master=self) for frame in ImageSequence.Iterator(self.gif)]

        self.label = ctk.CTkLabel(self.frame, text="")
        self.label.place(x=10, y= 10)

        self.index = 0
        self.animate()
    
        self.text1 = "What is ChatEase?"
        self.out1 = ""
        self.idx1 = 0
        self.y1 = 200

        img = Image.open("chat_bubble.png")
        self.ctk_img1 = ctk.CTkImage(light_image=img, size=(250, 60))
        label1_font = ctk.CTkFont(family="Times New Romans", size= 15, slant="italic")
        self.label1 = ctk.CTkLabel(self, width=150, height=50, fg_color="#0D1B2A", text="", font=label1_font, corner_radius=4, text_color="#00BFA5", image=self.ctk_img1, compound="center")
        self.label1.place(x= 730, y=self.y1)

        self.animate_up_1()
        self.type_1()

        # ---------------------- LABEL 2 (HIDDEN FIRST) ----------------------
        self.text2 = "A simple computer-based\n application designed\n to help people "
        self.out2 = ""
        self.idx2 = 0
        self.y2 = 250

        img2 = Image.open("chat_bubble.png")
        self.ctk_img2 = ctk.CTkImage(light_image=img2, size=(220, 140))
        label2_font = ctk.CTkFont(family="Times New Romans", size= 13, slant="italic")
        self.label2 = ctk.CTkLabel(self, text="", font=label2_font, width= 170, height= 110, fg_color= "#0D1B2A", corner_radius=5, text_color="#00BFA5", image=self.ctk_img2, compound="center")
        # DON'T PLACE YET — wait until Label 1 finishes

        # ---------------------- LABEL 3 (HIDDEN FIRST) ----------------------
        self.text3 = "This App \ndoesn't need\n Internet."
        self.out3 = ""
        self.idx3 = 0
        self.y3 = 500
        
        img3 = Image.open("chat_bubble.png")
        self.ctk_img3 = ctk.CTkImage(light_image=img3, size=(220, 120))
        label3_font = ctk.CTkFont(family="Times New Romans", size= 13, slant="italic")
        self.label3 = ctk.CTkLabel(self, width= 150, height= 70, fg_color="#0D1B2A", text="", font=label3_font,text_color="#00BFA5", image=self.ctk_img3, compound="center")



        #SignUP
        self.sign_up_font_style = ctk.CTkFont(family="Times New Roman", size=15, slant="italic")
        self.sign_up_label = ctk.CTkLabel(self.frame, text="Doesn't have an Account?", text_color="white", font=self.sign_up_font_style)
        self.sign_up_label.place(x=58, y=180)

        sign_up_underline_font = ctk.CTkFont(underline=True)
        sign_up_btn = ctk.CTkButton(self.frame, 
                                    text="Sign Up",
                                    width=49, 
                                    height=40,
                                    border_width=0,
                                    fg_color="transparent",
                                    hover_color="#13283d", 
                                    font=sign_up_underline_font, 
                                    command=self.sign_up_frame)
        sign_up_btn.place(x=230, y=175.4)

        # LOGIN USERNAME
        self.username = ctk.CTkEntry(self.frame,
                                      width=250, 
                                      height=35, 
                                      fg_color="transparent", 
                                      corner_radius=10, 
                                      text_color="white")
        self.username.place(x=80, y=250)

        # LOGIN PASSWORD
        self.password = ctk.CTkEntry(self.frame, 
                                     width=250, 
                                     height=35, 
                                     corner_radius=10, 
                                     fg_color="transparent", 
                                     text_color="white", 
                                     show="•")
        self.password.place(x=80, y=330)
        
        #LOGIN
        submitButton = ctk.CTkButton(self.frame,
                                      text="Log In", 
                                      width=200, 
                                      height=40, 
                                      corner_radius=20, 
                                      border_width=0,
                                     bg_color="transparent",
                                       fg_color="#0E66B3", 
                                       hover_color="#00BFA5",
                                     command=self.controller.submit_action)  # Fixed: Call instance method
        submitButton.place(x=100, y=400)

        underline_font = ctk.CTkFont(underline=True)
        
        #Forgot Password
        forgotPassword = ctk.CTkButton(self.frame, 
                                       text="Forgot Password?", 
                                       width=200,
                                        height=40,
                                        border_width=0,
                                       fg_color="transparent", 
                                       hover_color="#13283d", 
                                       font=underline_font,
                                       command=lambda: ForgotPasswordUI())
        forgotPassword.place(x=163, y=440)
        self.icons()

        #Show Password
        self.show_pass_checkbox = ctk.CTkCheckBox(self.frame, text="Show Password", command=self.toggle_password)
        self.show_pass_checkbox.place(x= 90, y= 370)


    def open_dashboard(self):
        self.withdraw()  # Close the login window
        dashboard = Dashboard(master=self)
        dashboard.set_controller(self.controller)
        
        
    def toggle_password(self):
        if self.show_pass_checkbox.get() == 1:       # Checked → show password
            self.password.configure(show="")
        else:                                   # Unchecked → hide password
            self.password.configure(show="•")

    def sign_up_frame(self):
        self.frame.destroy()
        try:
            self.bg_img = Image.open("bg_img.png")
            self.bg = ctk.CTkImage(light_image=self.bg_img, size=(1090, 690))
            self.bg_label = ctk.CTkLabel(self, image=self.bg, text="")
            self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Background image not found. Skipping.")

        self.frame = ctk.CTkFrame(self, width=400, height=500, corner_radius=1, fg_color="#151922")
        self.frame.place(relx=0.4, rely=0.54, anchor="e")

        self.sign_up_font_style = ctk.CTkFont(family="Times New Roman", size=15, slant="italic")
        self.sign_up_label = ctk.CTkLabel(self.frame, text="Already have an Account?", text_color="white", font=self.sign_up_font_style)
        self.sign_up_label.place(x=58, y=130)

        sign_in_underline_font = ctk.CTkFont(underline=True)
        signIn = ctk.CTkButton(self.frame, text="Sign In", width=49, height=40, border_width=0, fg_color="transparent",
                               hover_color="#151922", font=sign_in_underline_font, command=self.login_frame)
        signIn.place(x=230, y=124.5)

        self.font_style = ctk.CTkFont(family="Times New Roman", size=42, weight="bold", slant="italic")
        self.logo_label = ctk.CTkLabel(self.frame, text="ChatEase", font=self.font_style, text_color="white")
        self.logo_label.place(x=68, y=28)

        # FIRST NAME
        self.firstName = ctk.CTkEntry(self.frame, width=140, height=35, fg_color="transparent", corner_radius=10, text_color="white")
        self.firstName.place(x=44, y=200)
        font_style = ctk.CTkFont(family="Arial", size=13, slant="italic")
        Firstname_label = ctk.CTkLabel(self.frame, text="Firstname", text_color="white", font=font_style)
        Firstname_label.place(x=55, y=170)

        # LAST NAME
        self.lastName = ctk.CTkEntry(self.frame, width=140, height=35, corner_radius=10, fg_color="transparent", text_color="white")
        self.lastName.place(x=214, y=200)
        Lastname_label = ctk.CTkLabel(self.frame, text="Lastname", text_color="white", font=font_style)
        Lastname_label.place(x=220, y=170)

        # USERNAME
        self.createUsername = ctk.CTkEntry(self.frame, width=240, height=35, corner_radius=10, fg_color="transparent", text_color="white")
        self.createUsername.place(x=74, y=290)
        username_label = ctk.CTkLabel(self.frame, text="Username", text_color="white", font=font_style)
        username_label.place(x=85, y=260)

        # PASSWORD
        self.createPassword = ctk.CTkEntry(self.frame, width=240, height=35, corner_radius=10, fg_color="transparent", text_color="white", show="*")
        self.createPassword.place(x=74, y=357)
        password_label = ctk.CTkLabel(self.frame, text="Password", text_color="white", font=font_style)
        password_label.place(x=85, y=325)

        createButton = ctk.CTkButton(self.frame, text="Create Account", width=200, height=40, corner_radius=20, border_width=0,
                                     bg_color="transparent", fg_color="#0E66B3", hover_color="#071647",
                                     command=self.controller.register_user)  # Added command
        createButton.place(x=100, y=420)

    def icons(self):
        try:
            # EMAIL ICON
            self.email_icon = ctk.CTkImage(light_image=Image.open("email.png"), size=(20, 20))
            self.email_icon_label = ctk.CTkLabel(self.frame, image=self.email_icon, text="")
            self.email_icon_label.place(x=80, y=219)

            font_style = ctk.CTkFont(family="Arial", size=13, slant="italic")
            username_label = ctk.CTkLabel(self.frame, text="Username", text_color="White", font=font_style)
            username_label.place(x=105, y=220)

            # PASSWORD ICON
            password_icon_img = Image.open("lock.png")
            self.password_icon = ctk.CTkImage(light_image=password_icon_img, size=(23, 23))
            self.password_icon_label = ctk.CTkLabel(self.frame, image=self.password_icon, text="")
            self.password_icon_label.place(x=80, y=300)

            password_label = ctk.CTkLabel(self.frame, text="Password", text_color="white", font=font_style)
            password_label.place(x=105, y=300)
        except FileNotFoundError:
            print("Icon images not found. Skipping.")

    def display_message(self, message, color):
        # Simple method to display messages (e.g., in a label or popup)
        msg_label = ctk.CTkLabel(self.frame, text=message, text_color=color, font=("Arial", 12))
        msg_label.place(x=80, y=450)  # Adjust position as needed
        self.after(3000, msg_label.destroy)  # Auto-remove after 3 seconds
    def animate_up_1(self):
        self.y1 -= 2
        self.label1.place(y=self.y1)

        if self.y1 > 120:
            self.after(10, self.animate_up_1)
        else:
            self.start_label2()  # 👉 Start Label 2 when Label 1 reaches final position

    def type_1(self):
        if self.idx1 < len(self.text1):
            self.out1 += self.text1[self.idx1]
            self.label1.configure(text=self.out1)
            self.idx1 += 1
            self.after(60, self.type_1)

    # ---------------------- LABEL 2 ----------------------
    def start_label2(self):
        """Show Label 2 and start its animation"""
        self.label2.place(x= 770, y=self.y2)
        self.animate_up_2()
        self.type_2()

    def animate_up_2(self):
        self.y2 -= 2
        self.label2.place(y=self.y2)

        if self.y2 > 200:
            self.after(10, self.animate_up_2)
        else:
            self.start_label3()  # 👉 Start Label 3 when Label 2 reaches final position

    def type_2(self):
        if self.idx2 < len(self.text2):
            self.out2 += self.text2[self.idx2]
            self.label2.configure(text=self.out2)
            self.idx2 += 1
            self.after(60, self.type_2)

    # ---------------------- LABEL 3 ----------------------
    def start_label3(self):
        """Show Label 3 and start its animation"""
        self.label3.place(x= 880, y=self.y3)
        self.animate_up_3()
        self.type_3()

    def animate_up_3(self):
        self.y3 -= 2
        self.label3.place(y=self.y3)

        if self.y3 > 350:
            self.after(10, self.animate_up_3)

    def type_3(self):
        if self.idx3 < len(self.text3):
            self.out3 += self.text3[self.idx3]
            self.label3.configure(text=self.out3)
            self.idx3 += 1
            self.after(60, self.type_3)
    
    def animate(self):
        frame = self.frames[self.index]
        self.label.configure(image=frame)

        self.index = (self.index + 1) % len(self.frames)
        self.after(30, self.animate)  # Change speed here

    
    def type_text(self):
        updated = False

        if self.current_index < len(self.message):
            self.typing_label.configure(
                text=self.typing_label.cget("text") + self.message[self.current_index]
            )
            self.current_index += 1
            updated = True

        elif self.another_index < len(self.another_message):  # use elif so it types sequentially
            self.another_label.configure(
                text=self.another_label.cget("text") + self.another_message[self.another_index]
            )
            self.another_index += 1
            updated = True

        if updated:
            self.after(100, self.type_text)


class ForgotPasswordUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controller = Controller(view=self) # Instantiate controller
        self.title("Forgot Password")
        self.geometry('400x450')
        self.minsize(400, 450)
        self._set_appearance_mode("system")
        self.fp_frame()
        self.fp_inputs()
        self.fp_button()
        self.mainloop()

    def fp_frame(self):
        self.frame = ctk.CTkFrame(self, width=390, height=440, corner_radius=1, fg_color="#151922")
        self.frame.pack(fill="both", expand=True)

    def fp_inputs(self):
        # Username
        self.username = ctk.CTkEntry(self.frame, width=200, height=30, fg_color="transparent", corner_radius=10, text_color="white")
        self.username.place(x=100, y=130)
        font_style = ctk.CTkFont(family="Arial", size=13, slant="italic")
        username_label = ctk.CTkLabel(self.frame, text="Username", text_color="white", font=font_style)
        username_label.place(x=105, y=100)

        # Old Password
        self.password = ctk.CTkEntry(self.frame, width=200, height=30, fg_color="transparent", text_color="white", corner_radius=10, show="*")
        self.password.place(x=100, y=200)
        password_label = ctk.CTkLabel(self.frame, text="Old Password", text_color="white", font=font_style)
        password_label.place(x=105, y=170)

        # New Password
        self.new_password = ctk.CTkEntry(self.frame, width=200, height=30, fg_color="transparent", text_color="white", corner_radius=10, show="*")
        self.new_password.place(x=100, y=270)
        new_password_label = ctk.CTkLabel(self.frame, text="New Password", text_color="white", font=font_style)
        new_password_label.place(x=105, y=240)

    def fp_button(self):
        submitButton = ctk.CTkButton(self.frame, text="Update Password", width=200, height=40, corner_radius=20, border_width=0,
                                     bg_color="transparent", fg_color="#0E66B3", hover_color="#182A53",
                                     command=self.fp_submit_action)
        submitButton.place(x=100, y=330)

    def fp_submit_action(self):
        username = self.username.get().strip()
        old_password = self.password.get().strip()
        new_password = self.new_password.get().strip()

        if self.controller.change_password(username, old_password, new_password):
            CTkMessagebox(title="Success", message="Password Updated Successfully!", icon="check")
             # Close the popup
        else:
            CTkMessagebox(title="Error", message="Update Failed! Check credentials or ensure new password differs.", icon="cancel")






from PIL import Image, ImageTk

class Dashboard(ctk.CTkToplevel):

    def __init__(self, master):
        super().__init__(master)
        self.title("ChatEase")
        self.geometry("1200x650")
        
        self.minsize(1200, 650)
        self.maxsize(1200, 650)
        self._fg_color = "#0D1B2A"

        # Chat session storage
        self.chats = []
        self.active_chat = None
        self.bg_greeting = None
        self.bg_preview = None
        self.enter_icon = None
        self.chat_icon = None
        self.ticket_icon = None
        self.logout_icon = None
        self.user_icon = None
        self.ai_icon = None

        self.load_images()
        self.main_frame()
        self.buttons()
        self.controller = None

        

    
    def set_controller(self, controller):
        self.controller = controller
    # ------------------------------------------------------
    # MAIN FRAME
    # ------------------------------------------------------
    def load_images(self):
        try:
            self.bg = ctk.CTkImage(light_image=Image.open("greeting.png"), size=(300, 400))
            self.bg_preview = ctk.CTkImage(light_image=Image.open("chat_preview.png"), size=(400, 300))
            self.enter_icon = ctk.CTkImage(light_image=Image.open("Enter.png"), size=(20, 20))
            self.chat_icon = ctk.CTkImage(light_image=Image.open("new_chat.png"), size=(30, 30))
            self.ticket_icon = ctk.CTkImage(light_image=Image.open("ticket.png"), size=(30, 30))
            self.logout_icon = ctk.CTkImage(light_image=Image.open("logout.png"), size=(30, 30))
            self.user_icon = ctk.CTkImage(light_image=Image.open("users_icon.png"), size=(40, 40))
            self.ai_icon = ctk.CTkImage(light_image=Image.open("ai_icons.png"), size=(40, 40))
        except Exception as e:
            print("Error loading images:", e)


    def main_frame(self):
        main_frame = ctk.CTkFrame(self, width=1200, height=700, fg_color="#0D1B2A")
        main_frame.pack()

        # Main chat frame
        self.mainframe = ctk.CTkFrame(self, width=820, height=620, fg_color="#13283d", corner_radius=20)
        self.mainframe.place(x=360, y=10)

        try:
            # Background image
            bg_img = Image.open("greeting.png")
            self.bg = ctk.CTkImage(light_image=bg_img, size=(300, 400))
            self.bg_label = ctk.CTkLabel(self.mainframe, image=self.bg, text="")
            self.bg_label.place(x=20, y=50)

        except (FileNotFoundError, Exception) as e:
            print(f"Image loading failed: {e}. Skipping.")
        # Text under image
        words_font = ctk.CTkFont(family="Arial", size=15, slant="italic")
        words = ctk.CTkLabel(self.mainframe, width=150, height=50,
                            text="Select New Chat to Initiate Conversation",
                            font=words_font, text_color="#00BFA5")
        words.place(x=490, y=460)


        try: 
            bg_img = Image.open("chat_preview.png")
            self.bg_preview = ctk.CTkImage(light_image=bg_img, size=(400, 300))
            self.bg_label = ctk.CTkLabel(self.mainframe, image=self.bg_preview, text="")
            self.bg_label.place(x=400, y=170)
        except FileNotFoundError:
            print("Chat preview image not found. Skipping.")

        #Total Response
        response_frame = ctk.CTkFrame(self.mainframe, width=250, height=170, fg_color= "#0D1B2A" )
        response_frame.place(x = 90, y =435)

        #Words Inside Response
        response_font = ctk.CTkFont(family="Arial", size= 25, weight="bold")
        response_words = ctk.CTkLabel(response_frame, text="Total Response",text_color="#00BFA5", font=response_font)
        response_words.place(x= 20, y= 20)

        over_font = ctk.CTkFont(family="Arial", size= 10, weight="bold")
        over_words = ctk.CTkLabel(response_frame, text="Over",text_color="white", font=over_font)
        over_words.place(x= 20, y= 60)

        number_font = ctk.CTkFont(family="Arial", size= 40, weight="bold", slant="italic")
        number_words = ctk.CTkLabel(response_frame, text="1000+",text_color="#00BFA5", font=number_font)
        number_words.place(x= 20, y= 90)

        # Typing Text
        self.bubble_frame = ctk.CTkFrame(self.mainframe, width=400, height=100, fg_color="transparent")
        self.bubble_frame.place(x=330, y=80)

        self.another_bubble_frame = ctk.CTkFrame(self.mainframe, width=400, height=100, fg_color="transparent")
        self.another_bubble_frame.place(x=330, y=150)

        # Labels inside bubbles
        typing_font = ctk.CTkFont(family="Segoe UI", size=45, weight="bold")
        self.typing_label = ctk.CTkLabel(self.bubble_frame, text="", font=typing_font,
                                        wraplength=350, justify="center", text_color="#00BFA5")
        self.typing_label.pack(padx=15, pady=15)

        another_typing_font = ctk.CTkFont(family="Segoe UI", size=20, weight="bold", slant="italic")
        self.another_label = ctk.CTkLabel(self.another_bubble_frame, text="", font=another_typing_font,
                                        wraplength=350, justify="center", text_color="#00BFA5")
        self.another_label.pack(padx=15, pady=15)

        # Typing messages
        self.message = "Hi, I'm ChatEase"
        self.another_message = "Your Personal Helpdesk Companion"
        self.current_index = 0
        self.another_index = 0

        self.type_text()

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=320, height=630, fg_color="#13283d", corner_radius=10)
        self.sidebar_frame.place(x=10, y=10)

        self.side_scrollbar = ctk.CTkScrollableFrame(self.sidebar_frame, width=320, height=780, fg_color="transparent")
        self.side_scrollbar.place(x=0, y=200)

        self.recent_chats = ctk.CTkLabel(self.sidebar_frame, text="Recent Chats",
                                        font=("Arial", 20, "bold"), text_color="white")
        self.recent_chats.place(x=35, y=40)

    def type_text(self):
        updated = False

        if self.current_index < len(self.message):
            self.typing_label.configure(
                text=self.typing_label.cget("text") + self.message[self.current_index]
            )
            self.current_index += 1
            updated = True

        elif self.another_index < len(self.another_message):  # use elif so it types sequentially
            self.another_label.configure(
                text=self.another_label.cget("text") + self.another_message[self.another_index]
            )
            self.another_index += 1
            updated = True

        if updated:
            self.after(100, self.type_text)
    # ------------------------------------------------------
    # ENTRY BOX
    # ------------------------------------------------------
    def entry_box(self):
    # Entry
        self.input_entry = ctk.CTkEntry(
            self.mainframe, width=450, height=50,
            corner_radius=100,
            text_color="white",
            fg_color="transparent",
            placeholder_text="Ask Anything?"
        )
        self.input_entry.place(x=200, y=550)

        try:
            # Enter Button MUST be recreated here
            enter_icon_img = Image.open("Enter.png")
            self.enter_icon = ctk.CTkImage(light_image=enter_icon_img, size=(20, 20))

            self.input_button = ctk.CTkButton(
                self.mainframe, width=40, height=40,
                text="", fg_color="transparent", hover_color="#009688",
                cursor="hand2", image=self.enter_icon, corner_radius=30,
                command=self.add_message
            )
            self.input_button.place(x=573, y=555)
        except FileNotFoundError:
            print("Enter icon not found. Skipping button image.")
            # Fallback: Create button without image
            self.input_button = ctk.CTkButton(
                self.mainframe, width=40, height=40,
                text=">", fg_color="transparent", hover_color="#009688",
                cursor="hand2", corner_radius=30,
                command=self.add_message
            )
            self.input_button.place(x=573, y=555)

    # ------------------------------------------------------
    # BUTTONS
    # ------------------------------------------------------
    def logout(self):
        # Close current dashboard window
        self.master.deiconify()
        self.destroy()
        # Reopen login/signup window
        Login_Signup()

    def buttons(self):
        self.new_chat_font = ctk.CTkFont(family="Arial", size=17)





        try:
            chat_icon_img = Image.open("new_chat.png")
            self.chat_icon = ctk.CTkImage(light_image=chat_icon_img, size=(30, 30))
            self.new_chat_button = ctk.CTkButton(
                self.sidebar_frame, width=200, height=40, 
                text="New Chat", fg_color="transparent",
                hover_color="#182f4d", text_color="white",
                cursor="hand2", font=self.new_chat_font,
                image= self.chat_icon, anchor="w",
                command=self.new_chat
            )
            self.new_chat_button.place(x=20, y=80)

        except FileNotFoundError:
            print("New chat icon not found. Skipping button image.")
            # Fallback: Create button without image
            self.new_chat_button = ctk.CTkButton(
                self.sidebar_frame, width=200, height=40, 
                text="New Chat", fg_color="transparent",
                hover_color="#182f4d", text_color="white",
                cursor="hand2", font=self.new_chat_font,
                anchor="w", command=self.new_chat
            )
            self.new_chat_button.place(x=20, y=80)

        try:
            # Ticket button
            ticket_icon_img = Image.open("ticket.png")
            self.ticket_icon = ctk.CTkImage(light_image=ticket_icon_img, size=(30, 30))
            ticket_font = ctk.CTkFont(family="Arial", size=17)
            self.ticket_button = ctk.CTkButton(
                self.sidebar_frame, width=200, height=40,
                text="Ticket", fg_color="transparent",
                hover_color="#182f4d", cursor="hand2", anchor="w",
                image=self.ticket_icon, corner_radius=10,
                font=ticket_font,
                command=self.open_ticket_window
                )
            self.ticket_button.place(x=15, y=120)

        except FileNotFoundError:
            print("Ticket icon not found. Skipping button image.")
            # Fallback: Create button without image
            ticket_font = ctk.CTkFont(family="Arial", size=17)
            self.ticket_button = ctk.CTkButton(
                self.sidebar_frame, width=200, height=40,
                text="Ticket", fg_color="transparent",
                hover_color="#182f4d", cursor="hand2", anchor="w",
                corner_radius=10, font=ticket_font, command=self.open_ticket_window
            )
            self.ticket_button.place(x=15, y=120)

        try:
            # Logout button
            logout_icon_img = Image.open("logout.png")
            self.logout_icon = ctk.CTkImage(light_image=logout_icon_img, size=(30, 30))
        
            logout_font = ctk.CTkFont(family="Arial", size=17)
            self.logout_button = ctk.CTkButton(
                self.sidebar_frame, width=200, height=40,
                text="Logout", fg_color="transparent",
                hover_color="#182f4d", cursor="hand2", anchor="w",
                image=self.logout_icon, corner_radius=10,
                font=logout_font,
                command=self.logout,
            )
            self.logout_button.place(x=15, y=160)

        except FileNotFoundError:
            print("Logout icon not found. Skipping button image.")
            # Fallback: Create button without image
            logout_font = ctk.CTkFont(family="Arial", size=17)
            self.logout_button = ctk.CTkButton(
                self.sidebar_frame, width=200, height=40,
                text="Logout", fg_color="transparent",
                hover_color="#182f4d", cursor="hand2", anchor="w",
                corner_radius=10, font=logout_font,
                command=self.logout
            )
            self.logout_button.place(x=15, y=160)

    # ------------------------------------------------------
    # CHAT LOGIC
    # ------------------------------------------------------
    def new_chat(self):

        self.main_scrollbar = ctk.CTkScrollableFrame( self.mainframe, width=820, height=620, fg_color="#13283d" ) 
        self.main_scrollbar.place(x=0, y=0)
        # Create a new empty chat session
        new_session = {"title": "", "messages": []}
        self.chats.append(new_session)
        self.active_chat = len(self.chats) - 1

        self.entry_box()
        # Clear input box
        self.input_entry.delete(0, "end")

        # Clear existing chat bubbles only
        for widget in self.main_scrollbar.winfo_children():
            widget.destroy()

        # Update sidebar
        self.update_recent_chats()


    def add_message(self, event=None):
        msg = self.input_entry.get()
        if not msg or self.active_chat is None:
            return

        self.chats[self.active_chat]["messages"].append(("user", msg))
        ai_response = self.controller.message(msg)
        self.chats[self.active_chat]["messages"].append(("ai", ai_response))
        if self.chats[self.active_chat]["title"] == "":
            self.chats[self.active_chat]["title"] = msg[:50]

        
        self.update_recent_chats()
        self.input_entry.delete(0, "end")

        self.load_chat_messages()
    

    def chat_click(self, index):
        self.active_chat = index
        self.load_chat_messages()



    def load_chat_messages(self):
        for widget in self.main_scrollbar.winfo_children():
            widget.destroy()

        if self.active_chat is None:
            return

        try:
            # Load user and AI icons
            user_icon_img = Image.open("users_icon.png").resize((40, 40))
            self.user_icon = ctk.CTkImage(light_image=user_icon_img, size=(40, 40))
        except FileNotFoundError:
            print("User icon not found. Skipping.")
            user_icon = None

        try:
            ai_icon_img = Image.open("ai_icons.png").resize((40, 40))
            self.ai_icon = ctk.CTkImage(light_image=ai_icon_img, size=(40, 40))
        except FileNotFoundError:
            print("AI icon not found. Skipping.")
            self.ai_icon = None

        for sender, msg in self.chats[self.active_chat]["messages"]:
            # Horizontal frame to hold icon + bubble
            frame = ctk.CTkFrame(self.main_scrollbar, fg_color="transparent")
            frame.pack(fill="x", pady=5, padx=50)

            bubble_font = ctk.CTkFont(family="Segoe UI", size=15)

            if sender == "user":
                # Right-aligned frame for user
                if self.user_icon:
                    icon_label = ctk.CTkLabel(frame, image=self.user_icon, text="")
                    icon_label.pack(side="right", padx=(10, 0))

                bubble = ctk.CTkLabel(
                    frame, text=msg, fg_color="#0D6EFD",
                    text_color="white", corner_radius=10,
                    anchor="center", justify="center", font=bubble_font,
                    wraplength=300, padx=15, pady=10
                )
                bubble.pack(side="right", padx=5,pady= 60)
            else:

                if self.ai_icon:
                    # Left-aligned frame for AI
                    icon_label = ctk.CTkLabel(frame, image=self.ai_icon, text="")
                    icon_label.pack(side="left", padx=(0, 10))

                bubble = ctk.CTkLabel(
                    frame, text=msg, fg_color="#1B263B",
                    text_color="white", corner_radius=10,
                    anchor="center", justify="center", font=bubble_font,
                    wraplength=300, padx=15, pady=10
                )
                bubble.pack(side="left", padx=(10, 0))


    def update_recent_chats(self):
        self.label_font = ctk.CTkFont(family="Arial", size=15)
        for widget in self.side_scrollbar.winfo_children():
            widget.destroy()

        for i, chat in enumerate(self.chats):
            title = chat["title"] if chat["title"] else f"Chat {i+1}"
            label = ctk.CTkLabel(
                self.side_scrollbar, text=title, width=300, height=65,
                anchor="w", text_color="white", fg_color="#182f4d",
                cursor="hand2", font=self.label_font, corner_radius=10
            )
            label.pack(padx=5, pady=5)
            label.bind("<Button-1>", lambda e, idx=i: self.chat_click(idx))

    def open_ticket_window(self):
        # Create a popup window
        self.ticket_window = ctk.CTkToplevel(self)
        self.ticket_window.title("Submit a Ticket")
        self.ticket_window.geometry("400x450")
        self.ticket_window.resizable(False, False)
        self.ticket_window.grab_set()  # Focus on popup

        # Title
        title_font = ctk.CTkFont(family="Arial", size=22, weight="bold")
        title_label = ctk.CTkLabel(self.ticket_window, text="Submit a Ticket", font=title_font)
        title_label.pack(pady=15)

        # Name Field
        self.name_entry = ctk.CTkEntry(self.ticket_window, placeholder_text="Your Name", width=300)
        self.name_entry.pack(pady=10)

        # Email Field
        self.email_entry = ctk.CTkEntry(self.ticket_window, placeholder_text="Your Email", width=300)
        self.email_entry.pack(pady=10)

        # Issue Type
        self.issue_type = ctk.CTkOptionMenu(self.ticket_window, values=["Bug", "Account Issue", "Feature Request", "Other"])
        self.issue_type.pack(pady=10)

        # Description box
        self.desc_box = ctk.CTkTextbox(self.ticket_window, width=300, height=120)
        self.desc_box.insert("0.0", "Describe your issue here...")
        self.desc_box.pack(pady=10)

        submit_btn = ctk.CTkButton(self.ticket_window, text="Submit Ticket", command=self.submit_ticket)
        submit_btn.place(x= 120, y= 350)


        # Submit button
    def submit_ticket(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        issue = self.issue_type.get()
        description = self.desc_box.get("0.0", "end").strip()

        if not name or not email or not description:
            CTkMessagebox(title="Error", message="Please fill in all fields.", icon="cancel")
            return
        
        CTkMessagebox(
            title="Ticket Submitted",
            message="Your ticket has been successfully submitted!",
            icon="check"
        )
        self.ticket_window.destroy()





# ------------------------------------------------------
# RUN APP
# ------------------------------------------------------

app = Login_Signup()  # This creates its own controller internally
app.mainloop()
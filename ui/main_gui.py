"""
Before using this GUI, install CustomTkinter:
    pip install customtkinter
"""

try:
    import customtkinter as ctk
    from tkinter import messagebox
    from controllers import RegistrationSystem
    
    CTK_AVAILABLE = True
except ImportError:
    CTK_AVAILABLE = False
    print("CustomTkinter not installed. Run: pip install customtkinter")


class MainGUI:
    """
    Ultra-modern GUI using CustomTkinter.
    
    Provides:
    - Clean layout with centered UI
    - Modern design system with rounded components
    - Clear separation of views (Login, Signup, Main Menu, Course List)
    - Smooth UI transitions
    """

    def __init__(self, system: RegistrationSystem):
        if not CTK_AVAILABLE:
            raise ImportError("CustomTkinter is required for this GUI.")
        
        self.system = system
        
        # Set global appearance and color theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Create the main window
        self.root = ctk.CTk()
        self.root.title("Course Registration System")
        self.root.geometry("1100x700")
        
        # Center the main window on the screen
        self.center_window(1100, 700)
        
        # A placeholder for the active UI frame
        self.current_frame = None
        
        # Status bar at the bottom
        self.status_label = ctk.CTkLabel(
            self.root,
            text="Welcome! Please login to continue",
            font=("Segoe UI", 11),
            text_color="gray"
        )
        self.status_label.pack(side="bottom", fill="x", pady=10, padx=20)
        
        # Show login screen first
        self.show_login_view()
    
    def center_window(self, width: int, height: int):
        """Center the main window on the screen."""
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = int((screen_w - width) / 2)
        y = int((screen_h - height) / 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def clear_frame(self):
        """Destroy the current frame and create a fresh one."""
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.current_frame.pack(fill="both", expand=True, padx=40, pady=30)
    
    def set_status(self, msg: str):
        """Update the bottom status bar message."""
        self.status_label.configure(text=msg)
    
    # =============================================================
    # Login View
    # =============================================================
    def show_login_view(self):
        """Render the login screen."""
        self.clear_frame()
        
        # Container centered in the screen
        center = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        center.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        ctk.CTkLabel(
            center,
            text="🎓 Course Registration",
            font=("Segoe UI", 32, "bold")
        ).pack(pady=(0, 10))
        
        ctk.CTkLabel(
            center,
            text="Welcome back! Please login to your account",
            font=("Segoe UI", 12),
            text_color="gray"
        ).pack(pady=(0, 40))
        
        # Login card container
        card = ctk.CTkFrame(center, width=400, height=350, corner_radius=15)
        card.pack_propagate(False)
        card.pack()
        
        # Student ID
        ctk.CTkLabel(
            card,
            text="Student ID",
            font=("Segoe UI", 12, "bold"),
            anchor="w"
        ).pack(fill="x", padx=30, pady=(30, 5))
        
        sid_entry = ctk.CTkEntry(
            card,
            placeholder_text="Enter your student ID",
            height=40,
            font=("Segoe UI", 11)
        )
        sid_entry.pack(fill="x", padx=30, pady=(0, 20))
        
        # Password
        ctk.CTkLabel(
            card,
            text="Password",
            font=("Segoe UI", 12, "bold"),
            anchor="w"
        ).pack(fill="x", padx=30, pady=(0, 5))
        
        pwd_entry = ctk.CTkEntry(
            card,
            placeholder_text="Enter your password",
            show="●",
            height=40,
            font=("Segoe UI", 11)
        )
        pwd_entry.pack(fill="x", padx=30, pady=(0, 25))
        
        # Login button handler
        def handle_login():
            sid = sid_entry.get().strip()
            pwd = pwd_entry.get().strip()
            _, msg = self.system.login(sid, pwd)
            
            if self.system.current_user:
                self.set_status("✓ Login successful!")
                self.show_main_menu()
            else:
                messagebox.showerror("Login Failed", msg)
                self.set_status(f"⚠ {msg}")
        
        # Login button
        ctk.CTkButton(
            card,
            text="Login",
            height=40,
            font=("Segoe UI", 12, "bold"),
            command=handle_login
        ).pack(fill="x", padx=30, pady=(0, 15))
        
        # Signup link area
        link_frame = ctk.CTkFrame(card, fg_color="transparent")
        link_frame.pack()
        
        ctk.CTkLabel(
            link_frame,
            text="Don't have an account?",
            font=("Segoe UI", 11),
            text_color="gray"
        ).pack(side="left", padx=(0, 5))
        
        ctk.CTkButton(
            link_frame,
            text="Create one",
            font=("Segoe UI", 11),
            fg_color="transparent",
            text_color=("blue", "lightblue"),
            hover=False,
            command=self.show_signup_view,
            width=80
        ).pack(side="left")
        
        sid_entry.focus()

    # =============================================================
    # Signup View
    # =============================================================
    def show_signup_view(self):
        """Render the signup screen."""
        self.clear_frame()
        
        center = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        center.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(
            center,
            text="Create Account",
            font=("Segoe UI", 32, "bold")
        ).pack(pady=(0, 10))
        
        ctk.CTkLabel(
            center,
            text="Join us to start your academic journey",
            font=("Segoe UI", 12),
            text_color="gray"
        ).pack(pady=(0, 40))
        
        card = ctk.CTkFrame(center, width=400, height=420, corner_radius=15)
        card.pack_propagate(False)
        card.pack()
        
        # Student ID
        ctk.CTkLabel(
            card,
            text="Student ID",
            font=("Segoe UI", 12, "bold"),
            anchor="w"
        ).pack(fill="x", padx=30, pady=(30, 5))
        
        sid_entry = ctk.CTkEntry(
            card,
            placeholder_text="Enter student ID",
            height=40,
            font=("Segoe UI", 11)
        )
        sid_entry.pack(fill="x", padx=30, pady=(0, 20))
        
        # Full Name
        ctk.CTkLabel(
            card,
            text="Full Name",
            font=("Segoe UI", 12, "bold"),
            anchor="w"
        ).pack(fill="x", padx=30, pady=(0, 5))
        
        name_entry = ctk.CTkEntry(
            card,
            placeholder_text="Enter your full name",
            height=40,
            font=("Segoe UI", 11)
        )
        name_entry.pack(fill="x", padx=30, pady=(0, 20))
        
        # Password
        ctk.CTkLabel(
            card,
            text="Password",
            font=("Segoe UI", 12, "bold"),
            anchor="w"
        ).pack(fill="x", padx=30, pady=(0, 5))
        
        pwd_entry = ctk.CTkEntry(
            card,
            placeholder_text="Create a password",
            show="●",
            height=40,
            font=("Segoe UI", 11)
        )
        pwd_entry.pack(fill="x", padx=30, pady=(0, 25))
        
        # Signup logic
        def handle_create():
            sid = sid_entry.get().strip()
            name = name_entry.get().strip()
            pwd = pwd_entry.get().strip()
            
            if not sid or not name or not pwd:
                messagebox.showwarning("Sign Up", "All fields are required.")
                return
            
            _, msg = self.system.register_student(sid, name, pwd)
            if "exists" in msg:
                messagebox.showerror("Sign Up Failed", msg)
            else:
                messagebox.showinfo("Success", "Account created! Please login.")
                self.show_login_view()
        
        ctk.CTkButton(
            card,
            text="Create Account",
            height=40,
            font=("Segoe UI", 12, "bold"),
            fg_color="#10b981",
            hover_color="#059669",
            command=handle_create
        ).pack(fill="x", padx=30, pady=(0, 15))
        
        # Login link
        link_frame = ctk.CTkFrame(card, fg_color="transparent")
        link_frame.pack()
        
        ctk.CTkLabel(
            link_frame,
            text="Already have an account?",
            font=("Segoe UI", 11),
            text_color="gray"
        ).pack(side="left", padx=(0, 5))
        
        ctk.CTkButton(
            link_frame,
            text="Login here",
            font=("Segoe UI", 11),
            fg_color="transparent",
            text_color=("blue", "lightblue"),
            hover=False,
            command=self.show_login_view,
            width=80
        ).pack(side="left")

    # =============================================================
    # Main Menu
    # =============================================================
    def show_main_menu(self):
        """Render the main dashboard after login."""
        self.clear_frame()
        
        user = self.system.current_user
        credits = user.credits_remaining()
        
        # Navigation bar
        nav = ctk.CTkFrame(self.current_frame, height=80, corner_radius=15)
        nav.pack(fill="x", pady=(0, 30))
        nav.pack_propagate(False)
        
        # Left side
        left = ctk.CTkFrame(nav, fg_color="transparent")
        left.pack(side="left", padx=20, pady=15)
        
        ctk.CTkLabel(
            left,
            text="🎓 Course Registration",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            left,
            text=f"Welcome back, {user.name}",
            font=("Segoe UI", 11),
            text_color="gray"
        ).pack(anchor="w")
        
        # Right side
        right = ctk.CTkFrame(nav, fg_color="transparent")
        right.pack(side="right", padx=20, pady=15)
        
        ctk.CTkLabel(
            right,
            text=f"📚 {credits} Credits",
            font=("Segoe UI", 12, "bold")
        ).pack(side="left", padx=(0, 15))
        
        ctk.CTkButton(
            right,
            text="Logout",
            width=100,
            height=35,
            fg_color="#64748b",
            hover_color="#475569",
            command=self.handle_logout
        ).pack(side="left")
        
        # Cards area
        cards = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        cards.pack(expand=True)
        
        # Course List Card
        course_card = ctk.CTkFrame(cards, width=350, height=250, corner_radius=15)
        course_card.pack_propagate(False)
        course_card.grid(row=0, column=0, padx=20, pady=20)
        
        ctk.CTkLabel(course_card, text="📖", font=("Segoe UI", 60)).pack(pady=(40, 10))
        ctk.CTkLabel(course_card, text="View Courses", font=("Segoe UI", 20, "bold")).pack()
        ctk.CTkLabel(
            course_card,
            text="Browse and register for courses",
            font=("Segoe UI", 11),
            text_color="gray"
        ).pack(pady=(5, 20))
        
        ctk.CTkButton(
            course_card,
            text="Browse Courses",
            height=40,
            command=self.show_course_list_window
        ).pack(padx=30, pady=(0, 20), fill="x")
        
        # My Schedule Card
        schedule_card = ctk.CTkFrame(cards, width=350, height=250, corner_radius=15)
        schedule_card.pack_propagate(False)
        schedule_card.grid(row=0, column=1, padx=20, pady=20)
        
        ctk.CTkLabel(schedule_card, text="📅", font=("Segoe UI", 60)).pack(pady=(40, 10))
        ctk.CTkLabel(schedule_card, text="My Schedule", font=("Segoe UI", 20, "bold")).pack()
        ctk.CTkLabel(
            schedule_card,
            text="View and manage your courses",
            font=("Segoe UI", 11),
            text_color="gray"
        ).pack(pady=(5, 20))
        
        ctk.CTkButton(
            schedule_card,
            text="View Schedule",
            height=40,
            command=self.show_schedule_window
        ).pack(padx=30, pady=(0, 20), fill="x")

    # =============================================================
    # Course List Window
    # =============================================================
    def show_course_list_window(self):
        """Open a window listing all available courses."""
        courses = self.system.get_all_courses()
        
        if not courses:
            messagebox.showinfo("Courses", "No courses available.")
            return
        
        win = ctk.CTkToplevel(self.root)
        win.title("Course List")
        win.geometry("1100x600")
        
        header = ctk.CTkFrame(win, height=70)
        header.pack(fill="x")
        
        ctk.CTkLabel(
            header,
            text="📖 Available Courses",
            font=("Segoe UI", 20, "bold")
        ).pack(side="left", padx=20, pady=20)
        
        content = ctk.CTkFrame(win)
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        table_frame = ctk.CTkScrollableFrame(content)
        table_frame.pack(fill="both", expand=True)
        
        # Header - Only Course Name and Action
        header_row = ctk.CTkFrame(table_frame, fg_color="#e2e8f0")
        header_row.pack(fill="x", pady=(0, 5))
        
        ctk.CTkLabel(
            header_row,
            text="Course Name",
            font=("Segoe UI", 11, "bold"),
            width=500,
            anchor="w"
        ).grid(row=0, column=0, padx=20, pady=10)
        
        ctk.CTkLabel(
            header_row,
            text="Action",
            font=("Segoe UI", 11, "bold"),
            width=100,
            anchor="center"
        ).grid(row=0, column=1, padx=20, pady=10)
        
        # Data rows - Show only course title and register button
        for c in courses:
            row = ctk.CTkFrame(table_frame, fg_color="transparent")
            row.pack(fill="x", pady=2)
            
            def make_detail_handler(course):
                def handler():
                    self.show_course_detail_window(course)
                return handler
            
            # Clickable course title
            course_btn = ctk.CTkButton(
                row,
                text=c.title,
                width=500,
                height=40,
                anchor="w",
                fg_color="transparent",
                text_color=("blue", "lightblue"),
                hover_color="#f0f0f0",
                font=("Segoe UI", 12),
                command=make_detail_handler(c)
            )
            course_btn.grid(row=0, column=0, padx=20, pady=5, sticky="w")
            
            def make_register_handler(course):
                def handler():
                    ok, msg = self.system.register_course(course.course_id)
                    if ok:
                        messagebox.showinfo("Success", msg)
                        win.destroy()
                        self.show_main_menu()
                    else:
                        messagebox.showwarning("Failed", msg)
                return handler
            
            ctk.CTkButton(
                row,
                text="Register",
                width=100,
                height=35,
                command=make_register_handler(c)
            ).grid(row=0, column=1, padx=20, pady=5)
    
    def show_course_detail_window(self, course):
        """Show detailed information about a course."""
        detail_win = ctk.CTkToplevel(self.root)
        detail_win.title("Course Details")
        detail_win.geometry("600x500")
        
        # Header
        header = ctk.CTkFrame(detail_win, height=70)
        header.pack(fill="x")
        
        ctk.CTkLabel(
            header,
            text="📚 Course Details",
            font=("Segoe UI", 20, "bold")
        ).pack(side="left", padx=20, pady=20)
        
        # Content
        content = ctk.CTkFrame(detail_win)
        content.pack(fill="both", expand=True, padx=40, pady=30)
        
        # Course details card
        card = ctk.CTkFrame(content, corner_radius=15)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Course Title
        ctk.CTkLabel(
            card,
            text=course.title,
            font=("Segoe UI", 24, "bold"),
            wraplength=500
        ).pack(pady=(30, 20))
        
        # Details frame
        details = ctk.CTkFrame(card, fg_color="transparent")
        details.pack(fill="both", expand=True, padx=40, pady=10)
        
        # Course ID
        info_row = ctk.CTkFrame(details, fg_color="transparent")
        info_row.pack(fill="x", pady=10)
        ctk.CTkLabel(
            info_row,
            text="Course ID:",
            font=("Segoe UI", 13, "bold"),
            anchor="w",
            width=150
        ).pack(side="left")
        ctk.CTkLabel(
            info_row,
            text=course.course_id,
            font=("Segoe UI", 13),
            anchor="w"
        ).pack(side="left")
        
        # Instructor
        info_row = ctk.CTkFrame(details, fg_color="transparent")
        info_row.pack(fill="x", pady=10)
        ctk.CTkLabel(
            info_row,
            text="Instructor:",
            font=("Segoe UI", 13, "bold"),
            anchor="w",
            width=150
        ).pack(side="left")
        ctk.CTkLabel(
            info_row,
            text=course.instructor,
            font=("Segoe UI", 13),
            anchor="w"
        ).pack(side="left")
        
        # Credits
        info_row = ctk.CTkFrame(details, fg_color="transparent")
        info_row.pack(fill="x", pady=10)
        ctk.CTkLabel(
            info_row,
            text="Credits:",
            font=("Segoe UI", 13, "bold"),
            anchor="w",
            width=150
        ).pack(side="left")
        ctk.CTkLabel(
            info_row,
            text=str(course.credits),
            font=("Segoe UI", 13),
            anchor="w"
        ).pack(side="left")
        
        # Capacity
        info_row = ctk.CTkFrame(details, fg_color="transparent")
        info_row.pack(fill="x", pady=10)
        ctk.CTkLabel(
            info_row,
            text="Capacity:",
            font=("Segoe UI", 13, "bold"),
            anchor="w",
            width=150
        ).pack(side="left")
        ctk.CTkLabel(
            info_row,
            text=str(course.capacity),
            font=("Segoe UI", 13),
            anchor="w"
        ).pack(side="left")
        
        # Number of Enrolled Students
        info_row = ctk.CTkFrame(details, fg_color="transparent")
        info_row.pack(fill="x", pady=10)
        ctk.CTkLabel(
            info_row,
            text="Enrolled Students:",
            font=("Segoe UI", 13, "bold"),
            anchor="w",
            width=150
        ).pack(side="left")
        ctk.CTkLabel(
            info_row,
            text=f"{len(course.enrolled_students)} / {course.capacity}",
            font=("Segoe UI", 13),
            anchor="w"
        ).pack(side="left")
        
        # Close button
        ctk.CTkButton(
            card,
            text="Close",
            width=120,
            height=40,
            command=detail_win.destroy
        ).pack(pady=(20, 30))

    # =============================================================
    # Schedule Window
    # =============================================================
    def show_schedule_window(self):
        """Open a window displaying the user's schedule."""
        schedule = self.system.get_my_schedule()
        
        if not schedule:
            messagebox.showinfo("My Schedule", "You have no registered courses.")
            return
        
        win = ctk.CTkToplevel(self.root)
        win.title("My Schedule")
        win.geometry("900x500")
        
        header = ctk.CTkFrame(win, height=70)
        header.pack(fill="x")
        
        ctk.CTkLabel(
            header,
            text="📅 My Schedule",
            font=("Segoe UI", 20, "bold")
        ).pack(side="left", padx=20, pady=20)
        
        total = sum(c.credits for c in schedule)
        ctk.CTkLabel(
            header,
            text=f"Total: {total} Credits",
            font=("Segoe UI", 12),
            text_color="gray"
        ).pack(side="right", padx=20, pady=20)
        
        content = ctk.CTkFrame(win)
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        table = ctk.CTkScrollableFrame(content)
        table.pack(fill="both", expand=True)
        
        header_row = ctk.CTkFrame(table, fg_color="#e2e8f0")
        header_row.pack(fill="x")
        
        col_widths = [140, 320, 180, 120]
        headers = ["Course ID", "Title", "Instructor", "Credits"]
        
        for i, h in enumerate(headers):
            ctk.CTkLabel(
                header_row,
                text=h,
                font=("Segoe UI", 11, "bold"),
                width=col_widths[i],
                anchor="center" if i == 3 else "w"
            ).grid(row=0, column=i, padx=10, pady=10)
        
        for c in schedule:
            row = ctk.CTkFrame(table)
            row.pack(fill="x", pady=2)
            
            values = [c.course_id, c.title, c.instructor, str(c.credits)]
            for i, val in enumerate(values):
                ctk.CTkLabel(
                    row,
                    text=val,
                    width=col_widths[i],
                    anchor="center" if i == 3 else "w"
                ).grid(row=0, column=i, padx=10, pady=8)
            
            def make_drop(course):
                def handler():
                    ok, msg = self.system.drop_course(course.course_id)
                    if ok:
                        messagebox.showinfo("Success", msg)
                        win.destroy()
                        self.show_main_menu()
                    else:
                        messagebox.showwarning("Failed", msg)
                return handler
            
            ctk.CTkButton(
                row,
                text="Drop",
                fg_color="#ef4444",
                hover_color="#dc2626",
                width=80,
                height=30,
                command=make_drop(c)
            ).grid(row=0, column=4, padx=10)

    # =============================================================
    # Logout
    # =============================================================
    def handle_logout(self):
        """Log the user out of the system."""
        self.system.logout()
        self.set_status("Successfully logged out")
        self.show_login_view()
    
    def run(self):
        """Start the event loop."""
        self.root.mainloop()

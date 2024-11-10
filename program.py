import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox, ttk, Text
from datetime import datetime
from tkcalendar import DateEntry
import ctypes  # Added for DPI awareness

# Set DPI awareness (Windows only)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # SYSTEM_DPI_AWARE
except Exception:
    pass  # DPI awareness not set

# Ensure you have installed tkcalendar and Pillow:
# pip install tkcalendar Pillow openpyxl

EXCEL_FILE = 'todo_tracker.xlsx'
HEADERS = ["Subject", "Part", "Section", "Task", "Description", "Status", "Date Added"]

def initialize_excel():
    """Initialize the Excel file with headers if it doesn't exist."""
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=HEADERS)
        df.to_excel(EXCEL_FILE, index=False)

def load_data():
    """Load data from Excel file."""
    try:
        return pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        initialize_excel()
        return pd.read_excel(EXCEL_FILE)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data: {e}")
        return pd.DataFrame(columns=HEADERS)

def save_data(df):
    """Save data to Excel file."""
    try:
        df.to_excel(EXCEL_FILE, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

class Tooltip:
    """
    It creates a tooltip for a given widget as the mouse goes on it.
    """
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.text = ""
        self.widget.bind("<Motion>", self.motion)
        self.widget.bind("<Leave>", self.leave)

    def motion(self, event):
        item = self.widget.identify_row(event.y)
        column = self.widget.identify_column(event.x)
        if item and column:
            col = int(column.replace('#', '')) - 1
            cell_value = self.widget.set(item, column)
            if len(cell_value) > 20:  # Show tooltip only if text is long
                self.text = cell_value
                if self.tipwindow:
                    self.tipwindow.destroy()
                x, y, cx, cy = self.widget.bbox(item, column)
                x += self.widget.winfo_rootx() + 25
                y += self.widget.winfo_rooty() + 20
                self.tipwindow = tw = tk.Toplevel(self.widget)
                tw.wm_overrideredirect(True)
                tw.wm_geometry(f"+{x}+{y}")
                label = tk.Label(tw, text=self.text, justify='left',
                                 background="#ffffe0", relief='solid', borderwidth=1,
                                 font=("arial", "10", "normal"))
                label.pack(ipadx=1)

    def leave(self, event):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do Tracker")
        self.root.geometry("1200x720")
        self.root.configure(bg="#2e2e2e")  # Darker background for night theme
        self.root.resizable(True, True)
        
        # Set DPI scaling to 1.5 for high-resolution displays
        self.root.tk.call('tk', 'scaling', 1.5)

        # Initialize Excel file
        initialize_excel()

        # Setup GUI styling
        self.setup_style()

        # Main GUI layout
        self.create_widgets()
        self.load_tasks()

        # Bind keyboard shortcuts
        self.bind_shortcuts()

    def setup_style(self):
        """Define custom styles."""
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#2e2e2e",
                        fieldbackground="#2e2e2e",
                        foreground="white",
                        font=("arial", 11),
                        rowheight=40,
                        bordercolor="#444444",
                        borderwidth=1)
        style.map('Treeview', background=[('selected', '#4a90e2')])
        style.configure("Treeview.Heading",
                        background="#444444",
                        foreground="white",
                        font=("arial", 12, "bold"))
        style.configure("TButton",
                        font=("arial", 11),
                        background="#5a5a5a",
                        foreground="white",
                        padding=5)
        style.map("TButton",
                  background=[('active', '#6a6a6a')])

    def create_widgets(self):
        """Create and arrange GUI widgets."""
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#1e1e1e")
        header_frame.pack(fill="x")

        header_label = tk.Label(header_frame, text="To-Do Tracker", font=("arial", 20, "bold"), fg="white", bg="#1e1e1e")
        header_label.pack(pady=10)

        # Filter Frame
        filter_frame = tk.LabelFrame(self.root, text="Filters", bg="#2e2e2e", fg="white", font=("arial", 12, "bold"))
        filter_frame.pack(fill="x", padx=15, pady=10)

        # Status filter
        tk.Label(filter_frame, text="Status:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.status_filter = ttk.Combobox(filter_frame, values=["All", "Incomplete", "In Progress", "Complete"], state="readonly")
        self.status_filter.set("All")
        self.status_filter.grid(row=0, column=1, padx=10, pady=5)

        # Date filter
        tk.Label(filter_frame, text="Date Added:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.date_filter = DateEntry(filter_frame, date_pattern='yyyy-mm-dd', background="#2e2e2e", foreground="white", borderwidth=2)
        self.date_filter.set_date(datetime.today())
        self.date_filter.grid(row=0, column=3, padx=10, pady=5)

        # Keyword filter
        tk.Label(filter_frame, text="Keyword:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=0, column=4, padx=10, pady=5, sticky="w")
        self.keyword_filter = tk.Entry(filter_frame, font=("arial", 11), width=25, bg="#4e4e4e", fg="white", insertbackground="white")
        self.keyword_filter.grid(row=0, column=5, padx=10, pady=5)

        # Apply and Clear Filter Buttons
        apply_filter_button = ttk.Button(filter_frame, text="Apply Filter", command=self.apply_filter)
        apply_filter_button.grid(row=0, column=6, padx=10, pady=5)

        clear_filter_button = ttk.Button(filter_frame, text="Clear Filters", command=self.clear_filters)
        clear_filter_button.grid(row=0, column=7, padx=10, pady=5)

        # Treeview and Scrollbar
        tree_frame = tk.Frame(self.root, bg="#2e2e2e")
        tree_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=HEADERS, show="headings", selectmode="browse")
        for col in HEADERS:
            if col == "Description":
                self.tree.column(col, width=300, anchor="w")  # Increased width for Description
            else:
                self.tree.column(col, width=150, anchor="center")
            self.tree.heading(col, text=col, command=lambda _col=col: self.sort_treeview(_col, False))
        self.tree.bind("<Double-1>", self.on_double_click)

        # Scrollbar for Treeview
        tree_scroll_y = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
        tree_scroll_y.pack(side="right", fill="y")
        tree_scroll_x.pack(side="bottom", fill="x")
        self.tree.pack(fill="both", expand=True)

        # Style tags for color coding
        self.tree.tag_configure("incomplete", background="#ff9999")
        self.tree.tag_configure("in_progress", background="#ffcc66")
        self.tree.tag_configure("complete", background="#99ff99")

        # Add Tooltip to Treeview
        self.tooltip = Tooltip(self.tree)

        # Button Frame without Icons
        button_frame = tk.Frame(self.root, bg="#2e2e2e")
        button_frame.pack(fill="x", padx=15, pady=10)

        # Buttons without icons
        add_button = ttk.Button(button_frame, text="Add Task", command=self.add_task)
        add_button.pack(side="left", padx=5)

        complete_button = ttk.Button(button_frame, text="Mark as Complete", command=self.mark_task_complete)
        complete_button.pack(side="left", padx=5)

        edit_button = ttk.Button(button_frame, text="Edit Task", command=self.edit_task)
        edit_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.pack(side="left", padx=5)

        refresh_button = ttk.Button(button_frame, text="Refresh", command=self.load_tasks)
        refresh_button.pack(side="left", padx=5)

        quit_button = ttk.Button(button_frame, text="Quit", command=self.root.quit)
        quit_button.pack(side="right", padx=5)

        # Details Text Widget Below Treeview
        details_frame = tk.Frame(self.root, bg="#2e2e2e")
        details_frame.pack(fill="x", padx=15, pady=10)

        self.details_text = Text(details_frame, height=10, wrap="word", bg="#4e4e4e", fg="white", font=("arial", 11), state="disabled")
        self.details_text.pack(fill="both", expand=True)

        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.show_task_details)

    def bind_shortcuts(self):
        """Bind keyboard shortcuts for better usability."""
        self.root.bind('<Control-n>', lambda event: self.add_task())
        self.root.bind('<Control-q>', lambda event: self.root.quit())
        self.root.bind('<Control-r>', lambda event: self.load_tasks())
        self.root.bind('<Control-c>', lambda event: self.mark_task_complete())

    def add_task(self):
        """Add a new task through a dialog."""
        add_popup = tk.Toplevel(self.root)
        add_popup.title("Add New Task")
        add_popup.configure(bg="#2e2e2e")
        add_popup.grab_set()  # Make the popup modal

        tk.Label(add_popup, text="Add New Task", font=("arial", 14, "bold"), fg="white", bg="#2e2e2e").pack(pady=10)

        form_frame = tk.Frame(add_popup, bg="#2e2e2e")
        form_frame.pack(padx=20, pady=10)

        entries = {}
        for idx, header in enumerate(HEADERS[:-2]):  # Exclude 'Status' and 'Date Added'
            tk.Label(form_frame, text=f"{header}:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=idx, column=0, pady=5, sticky="e")
            if header == "Description":
                # Use Text widget for multi-line Description
                description_text = Text(form_frame, font=("arial", 11), width=30, height=5, wrap="word", bg="#4e4e4e", fg="white", insertbackground="white")
                description_text.grid(row=idx, column=1, pady=5, padx=10)
                # Add scrollbar to Description
                desc_scroll = ttk.Scrollbar(form_frame, orient="vertical", command=description_text.yview)
                description_text.configure(yscrollcommand=desc_scroll.set)
                desc_scroll.grid(row=idx, column=2, sticky="ns", pady=5)
                entries[header] = description_text
            else:
                entry = tk.Entry(form_frame, font=("arial", 11), width=30, bg="#4e4e4e", fg="white", insertbackground="white")
                entry.grid(row=idx, column=1, pady=5, padx=10)
                entries[header] = entry

        # Status is set to 'Incomplete' by default
        status_var = tk.StringVar(value="Incomplete")
        tk.Label(form_frame, text="Status:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=len(HEADERS[:-2]), column=0, pady=5, sticky="e")
        status_combo = ttk.Combobox(form_frame, values=["Incomplete", "In Progress", "Complete"], state="readonly", textvariable=status_var)
        status_combo.grid(row=len(HEADERS[:-2]), column=1, pady=5, padx=10)

        # Date Added defaults to today
        date_added = datetime.today().strftime('%Y-%m-%d')

        def submit_task():
            task_data = {}
            for header, widget in entries.items():
                if header == "Description":
                    task_data[header] = widget.get("1.0", "end-1c").strip()
                else:
                    task_data[header] = widget.get().strip()
            task_data["Status"] = status_var.get()
            task_data["Date Added"] = date_added

            if not all(task_data.values()):
                messagebox.showwarning("Input Error", "All fields must be filled out.")
                return

            try:
                df = load_data()
                df = df.append(task_data, ignore_index=True)
                save_data(df)
                self.load_tasks()
                add_popup.destroy()
                messagebox.showinfo("Success", "Task added successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add task: {e}")

        submit_button = ttk.Button(add_popup, text="Add Task", command=submit_task)
        submit_button.pack(pady=10)

    def load_tasks(self):
        """Load tasks from the Excel file and display in the table with color coding."""
        try:
            df = load_data()
            self.display_tasks(df)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading tasks: {e}")

    def display_tasks(self, df):
        """Display tasks from DataFrame in the Treeview with color coding."""
        # Clear previous rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert rows with color coding based on status
        for index, row in df.iterrows():
            tags = ()
            if row["Status"] == "Incomplete":
                tags = ("incomplete",)
            elif row["Status"] == "In Progress":
                tags = ("in_progress",)
            elif row["Status"] == "Complete":
                tags = ("complete",)

            values = list(row)
            self.tree.insert("", "end", iid=index, values=values, tags=tags)

    def apply_filter(self):
        """Apply advanced filtering based on status, date, and keyword."""
        try:
            df = load_data()

            # Filter by status
            status = self.status_filter.get()
            if status != "All":
                df = df[df["Status"] == status]

            # Filter by date
            date = self.date_filter.get_date().strftime('%Y-%m-%d')
            if date:
                df = df[df["Date Added"] == date]

            # Filter by keyword in Task or Description
            keyword = self.keyword_filter.get().strip().lower()
            if keyword:
                df = df[df["Task"].str.lower().str.contains(keyword) | df["Description"].str.lower().str.contains(keyword)]

            self.display_tasks(df)
        except Exception as e:
            messagebox.showerror("Error", f"Error applying filters: {e}")

    def clear_filters(self):
        """Clear all filters and reload tasks."""
        self.status_filter.set("All")
        self.date_filter.set_date(datetime.today())
        self.keyword_filter.delete(0, tk.END)
        self.load_tasks()

    def mark_task_complete(self):
        """Mark the selected task as complete."""
        try:
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showwarning("Select Task", "Please select a task to mark as complete.")
                return
            task_index = int(selected_item[0])

            # Update the task status in the Excel file
            df = load_data()
            current_status = df.at[task_index, "Status"]
            if current_status == "Complete":
                messagebox.showinfo("Info", "Task is already marked as complete.")
                return
            df.at[task_index, "Status"] = "Complete"
            save_data(df)
            self.load_tasks()
            messagebox.showinfo("Success", "Task marked as complete.")
        except Exception as e:
            messagebox.showerror("Error", f"Error marking task as complete: {e}")

    def edit_task(self):
        """Edit the selected task."""
        try:
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showwarning("Select Task", "Please select a task to edit.")
                return
            task_index = int(selected_item[0])
            df = load_data()
            task_data = df.loc[task_index].to_dict()

            edit_popup = tk.Toplevel(self.root)
            edit_popup.title("Edit Task")
            edit_popup.configure(bg="#2e2e2e")
            edit_popup.grab_set()  # Make the popup modal

            tk.Label(edit_popup, text="Edit Task", font=("arial", 14, "bold"), fg="white", bg="#2e2e2e").pack(pady=10)

            form_frame = tk.Frame(edit_popup, bg="#2e2e2e")
            form_frame.pack(padx=20, pady=10)

            entries = {}
            for idx, header in enumerate(HEADERS[:-2]):  # Exclude 'Status' and 'Date Added'
                tk.Label(form_frame, text=f"{header}:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=idx, column=0, pady=5, sticky="e")
                if header == "Description":
                    # Use Text widget for multi-line Description
                    description_text = Text(form_frame, font=("arial", 11), width=30, height=5, wrap="word", bg="#4e4e4e", fg="white", insertbackground="white")
                    description_text.insert("1.0", task_data[header])
                    description_text.grid(row=idx, column=1, pady=5, padx=10)
                    # Add scrollbar to Description
                    desc_scroll = ttk.Scrollbar(form_frame, orient="vertical", command=description_text.yview)
                    description_text.configure(yscrollcommand=desc_scroll.set)
                    desc_scroll.grid(row=idx, column=2, sticky="ns", pady=5)
                    entries[header] = description_text
                else:
                    entry = tk.Entry(form_frame, font=("arial", 11), width=30, bg="#4e4e4e", fg="white", insertbackground="white")
                    entry.insert(0, task_data[header])
                    entry.grid(row=idx, column=1, pady=5, padx=10)
                    entries[header] = entry

            # Status Combobox
            status_var = tk.StringVar(value=task_data["Status"])
            tk.Label(form_frame, text="Status:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=len(HEADERS[:-2]), column=0, pady=5, sticky="e")
            status_combo = ttk.Combobox(form_frame, values=["Incomplete", "In Progress", "Complete"], state="readonly", textvariable=status_var)
            status_combo.grid(row=len(HEADERS[:-2]), column=1, pady=5, padx=10)

            # Date Added (read-only)
            tk.Label(form_frame, text="Date Added:", font=("arial", 11), fg="white", bg="#2e2e2e").grid(row=len(HEADERS[:-2])+1, column=0, pady=5, sticky="e")
            date_label = tk.Label(form_frame, text=task_data["Date Added"], font=("arial", 11), fg="white", bg="#2e2e2e")
            date_label.grid(row=len(HEADERS[:-2])+1, column=1, pady=5, padx=10, sticky="w")

            def submit_edit():
                updated_data = {}
                for header, widget in entries.items():
                    if header == "Description":
                        updated_data[header] = widget.get("1.0", "end-1c").strip()
                    else:
                        updated_data[header] = widget.get().strip()
                updated_data["Status"] = status_var.get()

                if not all(updated_data.values()):
                    messagebox.showwarning("Input Error", "All fields must be filled out.")
                    return

                try:
                    for key, value in updated_data.items():
                        df.at[task_index, key] = value
                    df.at[task_index, "Status"] = updated_data["Status"]
                    save_data(df)
                    self.load_tasks()
                    edit_popup.destroy()
                    messagebox.showinfo("Success", "Task updated successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to update task: {e}")

            submit_button = ttk.Button(edit_popup, text="Save Changes", command=submit_edit)
            submit_button.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Error editing task: {e}")

    def delete_task(self):
        """Delete the selected task."""
        try:
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showwarning("Select Task", "Please select a task to delete.")
                return
            task_index = int(selected_item[0])

            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected task?")
            if not confirm:
                return

            df = load_data()
            df = df.drop(task_index).reset_index(drop=True)
            save_data(df)
            self.load_tasks()
            messagebox.showinfo("Success", "Task deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting task: {e}")

    def on_double_click(self, event):
        """Display full task details in a separate window on double-click."""
        selected_item = self.tree.selection()
        if not selected_item:
            return
        task_index = int(selected_item[0])
        df = load_data()
        task_data = df.loc[task_index].to_dict()

        view_popup = tk.Toplevel(self.root)
        view_popup.title("View Task Details")
        view_popup.configure(bg="#2e2e2e")
        view_popup.grab_set()  # Make the popup modal

        tk.Label(view_popup, text="Task Details", font=("arial", 14, "bold"), fg="white", bg="#2e2e2e").pack(pady=10)

        details_frame = tk.Frame(view_popup, bg="#2e2e2e")
        details_frame.pack(padx=20, pady=10)

        for idx, (header, value) in enumerate(task_data.items()):
            tk.Label(details_frame, text=f"{header}:", font=("arial", 12, "bold"), fg="white", bg="#2e2e2e").grid(row=idx, column=0, pady=5, sticky="e")
            tk.Label(details_frame, text=value, font=("arial", 12), fg="white", bg="#2e2e2e", wraplength=400, justify="left").grid(row=idx, column=1, pady=5, sticky="w")

    def show_task_details(self, event):
        """Display selected task's details in the details_text widget."""
        selected_item = self.tree.selection()
        if not selected_item:
            return
        task_index = int(selected_item[0])
        df = load_data()
        task_data = df.loc[task_index].to_dict()

        self.details_text.configure(state="normal")
        self.details_text.delete("1.0", tk.END)
        for header, value in task_data.items():
            self.details_text.insert(tk.END, f"{header}: {value}\n")
        self.details_text.configure(state="disabled")

    def sort_treeview(self, col, reverse):
        """Sort the treeview by a given column."""
        try:
            df = load_data()
            df_sorted = df.sort_values(by=col, ascending=not reverse)
            self.display_tasks(df_sorted)
            # Reverse sort next time
            self.tree.heading(col, command=lambda: self.sort_treeview(col, not reverse))
        except Exception as e:
            messagebox.showerror("Error", f"Error sorting tasks: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


from forensic.suspicious_scanner import scan_directory
from forensic.case_manager import (
    initialize_database,
    save_case,
    get_all_cases,
    get_case_count
)
from forensic.report_generator import generate_report
from forensic.timeline_analyzer import generate_timeline
from forensic.pdf_analyzer import analyze_pdf
from forensic.exif_analyzer import get_exif_data
from forensic.metadata_analyzer import get_metadata
import tkinter as tk
from tkinter import filedialog
import hashlib

root = tk.Tk()
initialize_database()
root.title("Digital Forensic Analysis Toolkit")
root.geometry("1200x700")

# -------- Functions --------

def hash_analysis():

    for widget in content.winfo_children():
        widget.destroy()

    title = tk.Label(
        content,
        text="File Hash Analysis",
        font=("Arial", 18, "bold"),
        bg="white"
    )
    title.pack(pady=10)

    result_box = tk.Text(content, width=100, height=20)
    result_box.pack(pady=20)

    def analyze_file():

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                md5.update(chunk)
                sha1.update(chunk)
                sha256.update(chunk)

        result_box.delete("1.0", tk.END)

        result_box.insert(tk.END, f"File: {file_path}\n\n")
        result_box.insert(tk.END, f"MD5:\n{md5.hexdigest()}\n\n")
        result_box.insert(tk.END, f"SHA1:\n{sha1.hexdigest()}\n\n")
        result_box.insert(tk.END, f"SHA256:\n{sha256.hexdigest()}\n")

    tk.Button(
        content,
        text="Select File",
        command=analyze_file
    ).pack()
def metadata_analysis():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Metadata Analysis",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(content,width=100,height=20)
    result_box.pack(pady=20)

    def select_file():

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        metadata = get_metadata(file_path)

        result_box.delete("1.0",tk.END)

        for key,value in metadata.items():
            result_box.insert(tk.END,f"{key}: {value}\n")

    tk.Button(
        content,
        text="Select File",
        command=select_file
    ).pack()
def exif_analysis():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="EXIF Image Analysis",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(content,width=100,height=25)
    result_box.pack(pady=20)

    def select_image():

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Images","*.jpg *.jpeg *.png")
            ]
        )

        if not file_path:
            return

        exif_data = get_exif_data(file_path)

        result_box.delete("1.0",tk.END)

        if not exif_data:
            result_box.insert(tk.END,"No EXIF Data Found")

        else:
            for key,value in exif_data.items():
                result_box.insert(
                    tk.END,
                    f"{key}: {value}\n"
                )

    tk.Button(
        content,
        text="Select Image",
        command=select_image
    ).pack()
def pdf_analysis():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="PDF Metadata Analysis",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(content,width=100,height=25)
    result_box.pack(pady=20)

    def select_pdf():

        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files","*.pdf")]
        )

        if not file_path:
            return

        data = analyze_pdf(file_path)

        result_box.delete("1.0",tk.END)

        for key,value in data.items():
            result_box.insert(
                tk.END,
                f"{key}: {value}\n"
            )

    tk.Button(
        content,
        text="Select PDF",
        command=select_pdf
    ).pack()
def timeline_analysis():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Forensic Timeline Analysis",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(content,width=100,height=25)
    result_box.pack(pady=20)

    def select_file():

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        events = generate_timeline(file_path)

        result_box.delete("1.0",tk.END)

        result_box.insert(tk.END,"=== Timeline Events ===\n\n")

        for event,time_stamp in events:
            result_box.insert(
                tk.END,
                f"{event}: {time_stamp}\n"
            )

    tk.Button(
        content,
        text="Select File",
        command=select_file
    ).pack()
    from tkinter import filedialog
def case_management():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Case Management",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    tk.Label(content,text="Case ID",bg="white").pack()

    case_id_entry = tk.Entry(content,width=50)
    case_id_entry.pack()

    tk.Label(content,text="Investigator",bg="white").pack()

    investigator_entry = tk.Entry(content,width=50)
    investigator_entry.pack()

    tk.Label(content,text="Case Title",bg="white").pack()

    title_entry = tk.Entry(content,width=50)
    title_entry.pack()

    result_label = tk.Label(
        content,
        text="",
        bg="white"
    )

    result_label.pack(pady=10)

    def save_current_case():

        save_case(
            case_id_entry.get(),
            investigator_entry.get(),
            title_entry.get()
        )

        result_label.config(
            text="Case Saved Successfully"
        )

    tk.Button(
        content,
        text="Save Case",
        command=save_current_case
    ).pack(pady=10)
def view_cases():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Saved Investigation Cases",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(
        content,
        width=100,
        height=25
    )

    result_box.pack(pady=20)

    records = get_all_cases()

    if not records:
        result_box.insert(
            tk.END,
            "No Cases Found"
        )

    else:

        for case in records:

            result_box.insert(
                tk.END,
                f"Case ID: {case[0]}\n"
            )

            result_box.insert(
                tk.END,
                f"Investigator: {case[1]}\n"
            )

            result_box.insert(
                tk.END,
                f"Title: {case[2]}\n"
            )

            result_box.insert(
                tk.END,
                "-"*50 + "\n"
            )
def suspicious_file_scanner():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Suspicious File Scanner",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(
        content,
        width=100,
        height=25
    )

    result_box.pack(pady=20)

    def select_folder():

        folder = filedialog.askdirectory()

        if not folder:
            return

        result_box.delete("1.0", tk.END)

        files = scan_directory(folder)

        if not files:

            result_box.insert(
                tk.END,
                "No Suspicious Files Found"
            )

        else:

            result_box.insert(
                tk.END,
                "Suspicious Files Detected\n\n"
            )

            for file in files:

                result_box.insert(
                    tk.END,
                    f"{file}\n"
                )

    tk.Button(
        content,
        text="Select Folder",
        command=select_folder
    ).pack()
def dashboard():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Forensic Dashboard",
        font=("Arial",22,"bold"),
        bg="white"
    ).pack(pady=20)

    total_cases = get_case_count()

    tk.Label(
        content,
        text=f"Total Cases: {total_cases}",
        font=("Arial",16),
        bg="white"
    ).pack(pady=10)

    tk.Label(
        content,
        text="Total Reports: Available",
        font=("Arial",16),
        bg="white"
    ).pack(pady=10)

    tk.Label(
        content,
        text="Modules Active: 8",
        font=("Arial",16),
        bg="white"
    ).pack(pady=10)

    tk.Label(
        content,
        text="Status: Ready",
        font=("Arial",16),
        bg="white"
    ).pack(pady=10)
# -------- Header --------

header = tk.Frame(root, bg="#1e1e1e", height=80)
header.pack(fill="x")

tk.Label(
    header,
    text="Digital Forensic Analysis Toolkit",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 22, "bold")
).pack(pady=20)
def report_generation():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Evidence Report Generator",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(content,width=100,height=20)
    result_box.pack(pady=20)

    result_box.insert(
        tk.END,
        """Investigator: Maria Tariq

Case ID: CASE-001

Evidence Summary:
- File Hash Analysis Completed
- Metadata Analysis Completed
- PDF Analysis Completed
- Timeline Analysis Completed

Status:
Evidence Successfully Collected
"""
    )

def report_generation():

    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(
        content,
        text="Evidence Report Generator",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=10)

    result_box = tk.Text(content,width=100,height=20)
    result_box.pack(pady=20)

    result_box.insert(
        tk.END,
        "Forensic Report Content"
    )

    def save_report():

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files","*.pdf")]
        )

        if not file_path:
            return

        generate_report(
            file_path,
            result_box.get("1.0", tk.END)
        )

    tk.Button(
        content,
        text="Generate PDF Report",
        command=save_report
    ).pack()

# -------- Sidebar --------

# Sidebar

sidebar = tk.Frame(root, bg="#2d2d2d", width=250)
sidebar.pack(side="left", fill="y")

tk.Button(
    sidebar,
    text="Hash Analysis",
    width=25,
    height=2,
    command=hash_analysis
).pack(pady=10)

tk.Button(
    sidebar,
    text="Metadata Analysis",
    width=25,
    height=2,
    command=metadata_analysis
).pack(pady=10)
tk.Button(
    sidebar,
    text="EXIF Analysis",
    width=25,
    height=2,
    command=exif_analysis
).pack(pady=10)
tk.Button(
    sidebar,
    text="PDF Analysis",
    width=25,
    height=2,
    command=pdf_analysis
).pack(pady=10)
tk.Button(
    sidebar,
    text="Timeline Analysis",
    width=25,
    height=2,
    command=timeline_analysis
).pack(pady=10)
tk.Button(
    sidebar,
    text="Generate Report",
    width=25,
    height=2,
    command=report_generation
).pack(pady=10)
tk.Button(
    sidebar,
    text="Case Management",
    width=25,
    height=2,
    command=case_management
).pack(pady=10)
tk.Button(
    sidebar,
    text="View Cases",
    width=25,
    height=2,
    command=view_cases
).pack(pady=10)
tk.Button(
    sidebar,
    text="Suspicious Scanner",
    width=25,
    height=2,
    command=suspicious_file_scanner
).pack(pady=10)
tk.Button(
    sidebar,
    text="Dashboard",
    width=25,
    height=2,
    command=dashboard
).pack(pady=10)
# -------- Content --------

content = tk.Frame(root, bg="white")
content.pack(side="right", fill="both", expand=True)

tk.Label(
    content,
    text="Welcome to the Digital Forensic Analysis Toolkit",
    bg="white",
    font=("Arial", 18)
).pack(pady=50)

root.mainloop()
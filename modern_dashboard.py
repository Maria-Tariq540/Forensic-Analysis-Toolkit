from PIL import Image
from forensic.timeline_analyzer import generate_timeline
from forensic.report_generator import generate_report
from forensic.suspicious_scanner import scan_directory
from forensic.pdf_analyzer import analyze_pdf
from forensic.exif_analyzer import get_exif_data
from forensic.metadata_analyzer import get_metadata
import hashlib
from tkinter import filedialog
from forensic.case_manager import save_case, get_all_cases
import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Digital Forensic Analysis Toolkit")
app.geometry("1400x800")


# ---------------- Functions ----------------

def clear_content():
    for widget in content.winfo_children():
        widget.destroy()


def show_dashboard():

    clear_content()

    ctk.CTkLabel(
        content,
        text="🔍 Digital Forensic Investigation Platform",
        font=("Arial", 34, "bold")
    ).pack(pady=20)

    ctk.CTkLabel(
        content,
        text="Professional Cybersecurity & Digital Forensics Toolkit",
        font=("Arial", 16)
    ).pack(pady=10)

    # Cards Container
    cards = ctk.CTkFrame(content)
    cards.pack(pady=20)

    # Card 1
    card1 = ctk.CTkFrame(cards, width=220, height=120)
    card1.grid(row=0, column=0, padx=15, pady=15)

    ctk.CTkLabel(
        card1,
        text="Total Cases",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    ctk.CTkLabel(
        card1,
        text="12",
        font=("Arial", 32)
    ).pack()

    # Card 2
    card2 = ctk.CTkFrame(cards, width=220, height=120)
    card2.grid(row=0, column=1, padx=15, pady=15)

    ctk.CTkLabel(
        card2,
        text="Reports",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    ctk.CTkLabel(
        card2,
        text="8",
        font=("Arial", 32)
    ).pack()

    # Card 3
    card3 = ctk.CTkFrame(cards, width=220, height=120)
    card3.grid(row=1, column=0, padx=15, pady=15)

    ctk.CTkLabel(
        card3,
        text="Evidence",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    ctk.CTkLabel(
        card3,
        text="25",
        font=("Arial", 32)
    ).pack()

    # Card 4
    card4 = ctk.CTkFrame(cards, width=220, height=120)
    card4.grid(row=1, column=1, padx=15, pady=15)

    ctk.CTkLabel(
        card4,
        text="Alerts",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    ctk.CTkLabel(
        card4,
        text="3",
        font=("Arial", 32)
    ).pack()
    ctk.CTkLabel(
    content,
    text="Developed by Maria Tariq | Cybersecurity & Digital Forensics",
    font=("Arial", 14)
    ).pack(side="bottom", pady=20)

def show_case_management():

    clear_content()

    ctk.CTkLabel(
        content,
        text="Case Management",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    case_id = ctk.CTkEntry(
        content,
        width=300,
        placeholder_text="Case ID"
    )
    case_id.pack(pady=10)

    investigator = ctk.CTkEntry(
        content,
        width=300,
        placeholder_text="Investigator Name"
    )
    investigator.pack(pady=10)

    case_title = ctk.CTkEntry(
        content,
        width=300,
        placeholder_text="Case Title"
    )
    case_title.pack(pady=10)

    status_label = ctk.CTkLabel(
        content,
        text=""
    )
    status_label.pack(pady=10)

    def save_current_case():

        save_case(
            case_id.get(),
            investigator.get(),
            case_title.get()
        )

        status_label.configure(
            text="Case Saved Successfully ✅"
        )

    ctk.CTkButton(
        content,
        text="Save Case",
        command=save_current_case
    ).pack(pady=20)

def show_view_cases():

    clear_content()

    ctk.CTkLabel(
        content,
        text="Saved Cases",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    textbox = ctk.CTkTextbox(
        content,
        width=900,
        height=500
    )

    textbox.pack(pady=20)

    records = get_all_cases()

    if not records:

        textbox.insert(
            "end",
            "No Cases Found"
        )

    else:

        for case in records:

            textbox.insert(
                "end",
                f"Case ID: {case[0]}\n"
            )

            textbox.insert(
                "end",
                f"Investigator: {case[1]}\n"
            )

            textbox.insert(
                "end",
                f"Title: {case[2]}\n"
            )

            textbox.insert(
                "end",
                "-" * 50 + "\n\n"
            )

def show_hash_analysis():

    clear_content()

    ctk.CTkLabel(
        content,
        text="Hash Analysis",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    textbox = ctk.CTkTextbox(
        content,
        width=900,
        height=450
    )
    textbox.pack(pady=20)

    def select_file():

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

        textbox.delete("1.0", "end")

        textbox.insert(
            "end",
            f"File: {file_path}\n\n"
        )

        textbox.insert(
            "end",
            f"MD5:\n{md5.hexdigest()}\n\n"
        )

        textbox.insert(
            "end",
            f"SHA1:\n{sha1.hexdigest()}\n\n"
        )

        textbox.insert(
            "end",
            f"SHA256:\n{sha256.hexdigest()}"
        )

    ctk.CTkButton(
        content,
        text="Select File",
        command=select_file
    ).pack(pady=10)

def show_metadata_analysis():

    clear_content()

    ctk.CTkLabel(
        content,
        text="Metadata Analysis",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    textbox = ctk.CTkTextbox(
        content,
        width=900,
        height=450
    )
    textbox.pack(pady=20)

    def select_file():

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        metadata = get_metadata(file_path)

        textbox.delete("1.0", "end")

        for key, value in metadata.items():

            textbox.insert(
                "end",
                f"{key}: {value}\n"
            )

    ctk.CTkButton(
        content,
        text="Select File",
        command=select_file
    ).pack(pady=10)
def show_exif_analysis():

    clear_content()

    ctk.CTkLabel(
        content,
        text="EXIF Analysis",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    textbox = ctk.CTkTextbox(
        content,
        width=900,
        height=450
    )
    textbox.pack(pady=20)

    def select_image():

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Images", "*.jpg *.jpeg *.png")
            ]
        )

        if not file_path:
            return

        exif_data = get_exif_data(file_path)

        textbox.delete("1.0", "end")

        if not exif_data:

            textbox.insert(
                "end",
                "No EXIF Data Found"
            )

        else:

            for key, value in exif_data.items():

                textbox.insert(
                    "end",
                    f"{key}: {value}\n"
                )

    ctk.CTkButton(
        content,
        text="Select Image",
        command=select_image
    ).pack(pady=10)
def show_pdf_analysis():

    clear_content()

    ctk.CTkLabel(
        content,
        text="PDF Analysis",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    textbox = ctk.CTkTextbox(
        content,
        width=900,
        height=450
    )
    textbox.pack(pady=20)

    def select_pdf():

        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not file_path:
            return

        data = analyze_pdf(file_path)

        textbox.delete("1.0", "end")

        textbox.insert(
            "end",
            "PDF FORENSIC REPORT\n"
        )

        textbox.insert(
            "end",
            "=" * 40 + "\n\n"
        )

        for key, value in data.items():

            textbox.insert(
                "end",
                f"{key}\n"
            )

            textbox.insert(
                "end",
                f"{value}\n\n"
            )

    ctk.CTkButton(
        content,
        text="Select PDF",
        command=select_pdf
    ).pack(pady=10)
def show_suspicious_scanner():

    clear_content()

    ctk.CTkLabel(
        content,
        text="Suspicious File Scanner",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    textbox = ctk.CTkTextbox(
        content,
        width=900,
        height=450
    )
    textbox.pack(pady=20)

    def select_folder():

        folder = filedialog.askdirectory()

        if not folder:
            return

        files = scan_directory(folder)

        textbox.delete("1.0", "end")

        if not files:

            textbox.insert(
                "end",
                "No Suspicious Files Found"
            )

        else:

            textbox.insert(
                "end",
                "Suspicious Files Detected\n\n"
            )

            for file in files:

                textbox.insert(
                    "end",
                    f"{file}\n"
                )

    ctk.CTkButton(
        content,
        text="Select Folder",
        command=select_folder
    ).pack(pady=10)

def show_report_generator():

    clear_content()

    textbox = ctk.CTkTextbox(content)
    textbox.pack()

    textbox.insert(
    "1.0",
    """
Investigator: Maria Tariq

Case ID: CASE-001

Case Title:
Digital Forensic Investigation

Completed Analysis:

✓ Hash Analysis

✓ Metadata Analysis

✓ EXIF Analysis

✓ PDF Analysis

✓ Timeline Analysis

✓ Suspicious File Scan

Evidence Status:

✓ Evidence Collected

✓ Evidence Examined

✓ Report Generated

Final Verdict:

Investigation Completed Successfully
"""
)

    textbox.pack(pady=20)

    textbox.insert(
        "1.0",
        """Digital Forensic Investigation Report

Investigator: Maria Tariq

Case Summary:
- Hash Analysis Completed
- Metadata Analysis Completed
- PDF Analysis Completed
- Timeline Analysis Completed

Status:
Investigation Completed Successfully
"""
    )

    def save_pdf():

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not file_path:
            return

        generate_report(
            file_path,
            textbox.get("1.0", "end")
        )

    ctk.CTkButton(
        content,
        text="Generate PDF Report",
        command=save_pdf
    ).pack(pady=10)
def show_timeline_analysis():

    clear_content()

    ctk.CTkLabel(
        content,
        text="Timeline Analysis",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    textbox = ctk.CTkTextbox(
        content,
        width=900,
        height=450
    )
    textbox.pack(pady=20)

    def select_file():

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        events = generate_timeline(file_path)

        textbox.delete("1.0", "end")

        textbox.insert(
            "end",
            "=== Timeline Events ===\n\n"
        )

        for event, timestamp in events:

            textbox.insert(
                "end",
                f"{event}: {timestamp}\n"
            )

    ctk.CTkButton(
        content,
        text="Select File",
        command=select_file
    ).pack(pady=10)
# ---------------- Sidebar ----------------

sidebar = ctk.CTkFrame(app, width=250)
sidebar.pack(side="left", fill="y")
logo_image = ctk.CTkImage(
    light_image=Image.open("assets/logo.png"),
    dark_image=Image.open("assets/logo.png"),
    size=(100, 100)
)

logo_label = ctk.CTkLabel(
    sidebar,
    image=logo_image,
    text=""
)

logo_label.pack(pady=10)
ctk.CTkLabel(
    sidebar,
    text="Forensic Toolkit",
    font=("Arial", 24, "bold")
).pack(pady=20)

ctk.CTkButton(
    sidebar,
    text="Dashboard",
    width=200,
    command=show_dashboard
).pack(pady=5)

ctk.CTkButton(
    sidebar,
    text="Case Management",
    width=200,
    command=show_case_management
).pack(pady=5)

ctk.CTkButton(
    sidebar,
    text="View Cases",
    width=200,
    command=show_view_cases
).pack(pady=5)

ctk.CTkButton(
    sidebar,
    text="Hash Analysis",
    width=200,
    command=show_hash_analysis
).pack(pady=5)
ctk.CTkButton(
    sidebar,
    text="Metadata Analysis",
    width=200,
    command=show_metadata_analysis
).pack(pady=5)
ctk.CTkButton(
    sidebar,
    text="EXIF Analysis",
    width=200,
    command=show_exif_analysis
).pack(pady=5)
ctk.CTkButton(
    sidebar,
    text="PDF Analysis",
    width=200,
    command=show_pdf_analysis
).pack(pady=5)
ctk.CTkButton(
    sidebar,
    text="Timeline Analysis",
    width=200,
    command=show_timeline_analysis
).pack(pady=5)
ctk.CTkButton(
    sidebar,
    text="Suspicious Scanner",
    width=200,
    command=show_suspicious_scanner
).pack(pady=5)
ctk.CTkButton(
    sidebar,
    text="Generate Report",
    width=200,
    command=show_report_generator
).pack(pady=5)

# ---------------- Main Area ----------------

main = ctk.CTkFrame(app)
main.pack(side="right", fill="both", expand=True)

content = ctk.CTkFrame(main)
content.pack(fill="both", expand=True, padx=20, pady=20)

# Load dashboard initially
show_dashboard()

app.mainloop()
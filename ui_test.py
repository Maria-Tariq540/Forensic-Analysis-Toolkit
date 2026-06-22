import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1200x700")
app.title("Digital Forensic Analysis Toolkit")

sidebar = ctk.CTkFrame(app, width=250)
sidebar.pack(side="left", fill="y")

ctk.CTkLabel(
    sidebar,
    text="Forensic Toolkit",
    font=("Arial", 22, "bold")
).pack(pady=20)

ctk.CTkButton(
    sidebar,
    text="Dashboard"
).pack(pady=10)

main = ctk.CTkFrame(app)
main.pack(side="right", fill="both", expand=True)

ctk.CTkLabel(
    main,
    text="Professional Forensic Dashboard",
    font=("Arial", 24, "bold")
).pack(pady=50)

app.mainloop()
import sqlite3

def initialize_database():

    conn = sqlite3.connect("database/cases.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT,
            investigator TEXT,
            case_title TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_case(case_id, investigator, case_title):

    conn = sqlite3.connect("database/cases.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO cases
        (case_id, investigator, case_title)
        VALUES (?, ?, ?)
        """,
        (case_id, investigator, case_title)
    )

    conn.commit()
    conn.close()


def get_all_cases():

    conn = sqlite3.connect("database/cases.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT case_id, investigator, case_title FROM cases"
    )

    records = cursor.fetchall()

    conn.close()

    return records
def get_case_count():

    conn = sqlite3.connect("database/cases.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM cases")

    count = cursor.fetchone()[0]

    conn.close()

    return count
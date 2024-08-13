BANK_TABLE_NAME = "PACHISS_DIN_PEA_PAISA_DOUBLE"
BANK_ACCOUNT_TABLE_NAME = "PAISA_HEE_PAISA_HOGA"


myQueries = {
    "bank": {
        "create_table": ( f"""
            CREATE TABLE IF NOT EXISTS {BANK_TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ac_holder_num TEXT NOT NULL,
            ac_holder_name TEXT NOT NULL,

            FOREIGN KEY (ac_holder_num) REFERENCES {BANK_ACCOUNT_TABLE_NAME}(ac_holder_num),
            FOREIGN KEY (ac_holder_name) REFERENCES {BANK_ACCOUNT_TABLE_NAME} (ac_holder_name)
        ) """
        ),
        
        "ac_create": (
            f"""
            INSERT INTO {BANK_TABLE_NAME} (ac_holder_num, ac_holder_name)
            VALUES (?, ?)
            """
        ),
        "find_by_ac_name": (
            f"""
            SELECT ac_holder_num FROM {BANK_TABLE_NAME}
            WHERE ac_holder_name = ?
            """
        ),
        "find_by_ac_num": (
            f"""
            SELECT ac_holder_num FROM {BANK_TABLE_NAME}
            WHERE ac_holder_num = ?
            """
        ),
        "get_user": (
            f"""
            SELECT ac_holder_num, ac_holder_name FROM {BANK_ACCOUNT_TABLE_NAME}
            WHERE ac_holder_num = ?
    """
        ),
    },
    "bank_ac": {
        "create_table": (f"""
            CREATE TABLE IF NOT EXISTS {BANK_ACCOUNT_TABLE_NAME} (
            ac_holder_num TEXT NOT NULL PRIMARY KEY,
            ac_holder_name TEXT NOT NULL,
            balance REAL NOT NULL,
            passkey TEXT NOT NULL )
        """
        ),
        "ac_create": (
            f"""
            INSERT INTO {BANK_ACCOUNT_TABLE_NAME} (ac_holder_num, ac_holder_name, passkey, balance)
            VALUES (?, ?, ?, ?)
            """
        ),
        "withdraw_details": (f"""
            SELECT passkey, balance FROM {BANK_ACCOUNT_TABLE_NAME} WHERE ac_holder_num = ?
        """),

        "get_balance": (f"""
            SELECT balance FROM {BANK_ACCOUNT_TABLE_NAME} WHERE ac_holder_num = ?
        """),

        "update_balance": (f"""
            UPDATE {BANK_ACCOUNT_TABLE_NAME}
            SET balance = ?
            WHERE ac_holder_num = ?
        """),

        "get_info": (f"""
            SELECT ac_holder_num, ac_holder_name, balance FROM {BANK_ACCOUNT_TABLE_NAME}
            WHERE ac_holder_num = ?
        """)
    },
}

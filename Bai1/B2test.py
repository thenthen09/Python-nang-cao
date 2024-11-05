import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import sql

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database App")

        # Database connection fields
        self.db_name = tk.StringVar(value='test')
        self.user = tk.StringVar(value='postgres')
        self.password = tk.StringVar(value='123456')
        self.host = tk.StringVar(value='localhost')
        self.port = tk.StringVar(value='5432')
        self.table_name = tk.StringVar(value='students')

        # Create the GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Connection section
        connection_frame = tk.Frame(self.root)
        connection_frame.pack(pady=10)

        tk.Label(connection_frame, text="DB Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.db_name).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="User:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.user).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Host:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.host).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Port:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.port).grid(row=4, column=1, padx=5, pady=5)

        tk.Button(connection_frame, text="Connect", command=self.connect_db).grid(row=5, columnspan=2, pady=10)

        # Query section
        query_frame = tk.Frame(self.root)
        query_frame.pack(pady=10)

        tk.Label(query_frame, text="Table Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(query_frame, textvariable=self.table_name).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(query_frame, text="Load Data", command=self.load_data).grid(row=1, columnspan=2, pady=10)

        self.data_display = tk.Text(self.root, height=10, width=50)
        self.data_display.pack(pady=10)

        # Insert and Delete section
        insert_frame = tk.Frame(self.root)
        insert_frame.pack(pady=10)

        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.gender = tk.StringVar()
        self.major = tk.StringVar()

        tk.Label(insert_frame, text="Họ tên:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.name).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(insert_frame, text="Tuổi:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.age).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(insert_frame, text="Giới tính:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.gender).grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(insert_frame, text="Ngành:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.major).grid(row=3, column=1, padx=5, pady=5)

        button_frame = tk.Frame(insert_frame)
        button_frame.grid(row=4, columnspan=2, pady=10)

        tk.Button(button_frame, text="Insert Data", command=self.insert_data).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Data", command=self.delete_data).pack(side=tk.LEFT, padx=5)

        # ID to delete
        delete_frame = tk.Frame(self.root)
        delete_frame.pack(pady=10)

        self.delete_id = tk.StringVar()

        tk.Label(delete_frame, text="ID để xóa:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(delete_frame, textvariable=self.delete_id).grid(row=0, column=1, padx=5, pady=5)

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name.get(),
                user=self.user.get(),
                password=self.password.get(),
                host=self.host.get(),
                port=self.port.get()
            )
            self.cur = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def load_data(self):
        try:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(self.table_name.get()))
            self.cur.execute(query)
            rows = self.cur.fetchall()
            self.data_display.delete(1.0, tk.END)
            for row in rows:
                self.data_display.insert(tk.END, f"{row}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

    def insert_data(self):
        try:
            insert_query = sql.SQL("INSERT INTO {} (hoten, tuoi, gioitinh, nganh) VALUES (%s, %s, %s, %s)").format(sql.Identifier(self.table_name.get()))
            data_to_insert = (self.name.get(), self.age.get(), self.gender.get(), self.major.get())
            self.cur.execute(insert_query, data_to_insert)
            self.conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    def delete_data(self):
        try:
            delete_query = sql.SQL("DELETE FROM {} WHERE id = %s").format(sql.Identifier(self.table_name.get()))
            self.cur.execute(delete_query, (self.delete_id.get(),))
            self.conn.commit()
            messagebox.showinfo("Success", "Data deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Thông tin kết nối cơ sở dữ liệu
db_config = {
    'dbname': 'test',  # Thay bằng tên cơ sở dữ liệu của bạn
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

# Kết nối đến cơ sở dữ liệu
def get_db_connection():
    conn = psycopg2.connect(**db_config)
    return conn

# Trang chủ, hiển thị dữ liệu từ cơ sở dữ liệu
@app.route('/')
def index():
    # Kết nối đến cơ sở dữ liệu
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students;')  # Thay 'students' bằng tên bảng của bạn
    students = cur.fetchall()
    cur.close()
    conn.close()

    # Hiển thị dữ liệu lên trang web
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)

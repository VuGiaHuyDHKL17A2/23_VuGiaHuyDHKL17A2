import sqlite3

def create_database():
    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PHONG (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        amount INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS NHAN_VIEN (
        id INTEGER PRIMARY KEY,
        ho_ten TEXT NOT NULL,
        tuoi INTEGER NOT NULL,
        dia_chi TEXT NOT NULL,
        luong REAL NOT NULL,
        id_phong INTEGER,
        FOREIGN KEY (id_phong) REFERENCES PHONG(id)
    )
    """)
    conn.commit()
    print("Đã tạo bảng PHONG và NHAN_VIEN thành công!")
    conn.close()

def add_phong():
    name = input("Nhập tên phòng: ")
    price = float(input("Nhập giá trị: "))
    amount = int(input("Nhập số lượng: "))

    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO PHONG (name, price, amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    print("Đã thêm phòng thành công!")
    conn.close()

def add_nhan_vien():
    ho_ten = input("Nhập họ tên nhân viên: ")
    tuoi = int(input("Nhập tuổi nhân viên: "))
    dia_chi = input("Nhập địa chỉ: ")
    luong = float(input("Nhập lương: "))
    id_phong = int(input("Nhập ID phòng: "))

    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO NHAN_VIEN (ho_ten, tuoi, dia_chi, luong, id_phong)
        VALUES (?, ?, ?, ?, ?)
    """, (ho_ten, tuoi, dia_chi, luong, id_phong))
    conn.commit()
    print("Đã thêm nhân viên thành công!")
    conn.close()

def show_phong():
    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PHONG")
    rows = cursor.fetchall()
    print("\nDanh sách các phòng ban:")
    for row in rows:
        print(row)
    conn.close()

def show_nhan_vien():
    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT NV.id, NV.ho_ten, NV.tuoi, NV.dia_chi, NV.luong, P.name AS phong
        FROM NHAN_VIEN NV
        JOIN PHONG P ON NV.id_phong = P.id
    """)
    rows = cursor.fetchall()
    print("\nDanh sách nhân viên:")
    for row in rows:
        print(row)
    conn.close()

def main():
    create_database()
    while True:
        print("\nQUẢN LÝ NHÂN VIÊN VÀ PHÒNG BAN")
        print("1. Thêm phòng ban")
        print("2. Thêm nhân viên")
        print("3. Hiển thị danh sách phòng ban")
        print("4. Hiển thị danh sách nhân viên")
        print("5. Thoát chương trình")
        choice = input("Chọn chức năng (1-5): ")
        if choice == '1':
            add_phong()
        elif choice == '2':
            add_nhan_vien()
        elif choice == '3':
            show_phong()
        elif choice == '4':
            show_nhan_vien()
        elif choice == '5':
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
if __name__ == "__main__":
    main()

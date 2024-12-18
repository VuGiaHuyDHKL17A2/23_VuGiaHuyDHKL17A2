import sqlite3

def create_database():

    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        amount INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def show_products():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    print("\nDanh sách sản phẩm:")
    for row in rows:
        print(row)
    conn.close()

def add_product():
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))

    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (name, price, amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    print("Đã thêm sản phẩm thành công!")
    conn.close()

def search_product():
    name = input("Nhập tên sản phẩm cần tìm: ")
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    if rows:
        print("\nKết quả tìm kiếm:")
        for row in rows:
            print(row)
    else:
        print("Không tìm thấy sản phẩm nào.")
    conn.close()

def update_product():
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))

    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET price = ?, amount = ? WHERE id = ?", (new_price, new_amount, product_id))
    conn.commit()
    print("Đã cập nhật sản phẩm thành công!")
    conn.close()

def delete_product():
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE id = ?", (product_id,))
    conn.commit()
    print("Đã xóa sản phẩm thành công!")
    conn.close()

def main():
    create_database()
    while True:
        print("\nỨNG DỤNG QUẢN LÝ SẢN PHẨM")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật giá và số lượng sản phẩm")
        print("5. Xóa sản phẩm theo ID")
        print("6. Thoát chương trình")
        
        choice = input("Chọn chức năng (1-6): ")
        
        if choice == '1':
            show_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại")

if __name__ == "__main__":
    main()

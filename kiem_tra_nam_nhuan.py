def la_nam_nhuan(nam):
    """Kiem tra mot nam co phai nam nhuan hay khong.

    Quy tac:
    - Nam chia het cho 4 la nam nhuan.
    - Nhung nam chia het cho 100 thi khong phai nam nhuan.
    - Tru khi nam do cung chia het cho 400 thi van la nam nhuan.
    """
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)


def main():
    try:
        nam = int(input("Nhap nam can kiem tra: "))
        if la_nam_nhuan(nam):
            print(f"Nam {nam} la nam nhuan.")
        else:
            print(f"Nam {nam} khong phai nam nhuan.")
    except ValueError:
        print("Vui long nhap mot so nguyen hop le.")


if __name__ == "__main__":
    main()

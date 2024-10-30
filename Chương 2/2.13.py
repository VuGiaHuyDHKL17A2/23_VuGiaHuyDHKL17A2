import requests

def hien_thi_bai_post_noi_bat():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    response = requests.get(url)

    if response.status_code == 200:
        comments = response.json()
        print("Danh sách các bài post nổi bật:")
        
        # Giới hạn hiển thị 3 bình luận đầu tiên
        for i, comment in enumerate(comments[:3], start=1):
            print(f"\nBài Post {i}:")
            print(f"ID: {comment['id']}")
            print(f"Tên: {comment['name']}")
            print(f"Email: {comment['email']}")
            print(f"Nội dung: {comment['body']}")
    else:
        print("Không thể truy cập API")

hien_thi_bai_post_noi_bat()
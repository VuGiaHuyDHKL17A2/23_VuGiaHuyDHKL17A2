import requests

def hien_thi_bai_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        bai_posts = response.json()
        print(f"Tổng số bài post: {len(bai_posts)}")
        
        for bai_post in bai_posts:
            user_id = bai_post['userId']
            id = bai_post['id']
            title = bai_post['title']
            body = bai_post['body']
            print(f"User ID: {user_id}, ID: {id}, Title: {title}")
            print(f"Body: {body}\n")
    else:
        print("Không thể truy cập API")

hien_thi_bai_post()
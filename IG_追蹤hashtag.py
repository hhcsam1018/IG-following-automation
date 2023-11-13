import instabot
import time

# 設定 IG 帳號資訊
username = "帳號"
password = "密碼"

# 建立 Instabot 物件
bot = instabot.Bot(username, password)
response = bot.get(f"https://www.instagram.com/explore/tags/%E5%8A%A0%E5%AF%86%E8%B2%A8%E5%B9%A3/")
# 取得指定 hashtag 標籤貼文的 URL
def get_posts(hashtag):
    response = bot.get(f"https://www.instagram.com/explore/tags/%E5%8A%A0%E5%AF%86%E8%B2%A8%E5%B9%A3/")
    return response.json()["data"]

# 追蹤每則貼文的留言者
def follow_commenters(posts):
    followed_users = set()
    for post in posts:
        comments = post["comments"]
        for comment in comments:
            commenter_username = comment["user"]["username"]

            # 檢查是否已追蹤
            if commenter_username not in followed_users:
                bot.follow(commenter_username)
                followed_users.add(commenter_username)

# 主程式
def main():
    # 取得指定 hashtag 標籤貼文
    hashtag = "您的 hashtag 標籤"
    posts = get_posts(hashtag)

    # 每天追蹤 100 個帳號
    for i in range(100):
        follow_commenters(posts)
        time.sleep(5)

# 執行主程式
if __name__ == "__main__":
    main()
import requests

# Danh sách URL của các proxy
urls = [
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/https/data.txt",
    "https://daudau.org/api/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt",
    "https://raw.githubusercontent.com/SevenworksDev/proxy-list/refs/heads/main/proxies/http.txt",
    "https://raw.githubusercontent.com/SevenworksDev/proxy-list/refs/heads/main/proxies/https.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt",
]

# Tập hợp để lưu các proxy đã xử lý (tự động loại bỏ trùng lặp)
unique_proxies = set()

for url in urls:
    # Gửi yêu cầu GET cho từng URL
    response = requests.get(url)
    
    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        # Đọc các proxy từ nội dung phản hồi và xử lý
        proxies = response.text.splitlines()
        for proxy in proxies:
            # Xóa phần `http://` hoặc `https://` nếu có
            cleaned_proxy = proxy.replace("http://", "").replace("https://", "")
            # Thêm proxy đã xử lý vào tập hợp để loại bỏ trùng lặp
            unique_proxies.add(cleaned_proxy)
        print(f"Proxies từ {url} đã được xử lý và thêm vào tập hợp.")
    else:
        print(f"Lỗi khi lấy proxy từ {url}: {response.status_code}")

# Ghi các proxy duy nhất vào file proxy.txt
with open("proxy.txt", "w") as file:
    for proxy in unique_proxies:
        file.write(proxy + "\n")

print("Proxies đã được xử lý, loại bỏ trùng lặp, và lưu vào file proxy.txt")

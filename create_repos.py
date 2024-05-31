import requests

# Thông tin xác thực GitHub
username = 'your_github_username'
token = 'your_github_personal_access_token'

# Danh sách tên các repo cần tạo
repo_names = ['repo1', 'repo2', 'repo3']

# URL API GitHub
api_url = 'https://api.github.com/user/repos'

# Headers cho request
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Tạo từng repo
for repo_name in repo_names:
    data = {
        'name': repo_name,
        'description': 'Mô tả cho repo ' + repo_name,
        'private': False  # Đặt True nếu muốn tạo repo riêng tư
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f'Tạo repo {repo_name} thành công!')
    else:
        print(f'Lỗi khi tạo repo {repo_name}: {response.json()}')

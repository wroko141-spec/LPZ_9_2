import requests


class APIClient:
    def __init__(self, base_url=None, timeout=10):
        self.base_url = base_url or "https://jsonplaceholder.typicode.com"
        self.timeout = timeout
        self.request_count = 0
        self.last_response = None

    def get_posts(self, limit=10):
        url = f"{self.base_url}/posts"

        try:
            print(f"Запрос GET: {url}")
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()

            self.request_count += 1
            self.last_response = response

            data = response.json()
            print(f"Получено {len(data)} постов")
            return data[:limit]

        except requests.exceptions.Timeout:
            print("Ошибка: превышено время ожидания ответа")
            return None
        except requests.exceptions.ConnectionError:
            print("Ошибка: проблема с подключением к интернету")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"HTTP ошибка: {e}")
            return None
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            return None

    def get_users(self):
        url = f"{self.base_url}/users"

        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()

            self.request_count += 1
            self.last_response = response
            return response.json()

        except Exception as e:
            print(f"Ошибка при получении пользователей: {e}")
            return None

    def get_user_posts(self, user_id):
        url = f"{self.base_url}/posts?userId={user_id}"

        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()

            self.request_count += 1
            self.last_response = response
            return response.json()

        except Exception as e:
            print(f"Ошибка при получении постов пользователя: {e}")
            return None

    def get_random_quote(self):
        url = "https://api.quotable.io/random"

        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()

            self.request_count += 1
            self.last_response = response

            data = response.json()
            return {
                "text": data.get("content", ""),
                "author": data.get("author", "Unknown"),
                "tags": data.get("tags", []),
            }

        except Exception as e:
            print(f"Ошибка при получении цитаты: {e}")
            return None

    def get_statistics(self):
        return {
            "total_requests": self.request_count,
            "last_response_code": self.last_response.status_code if self.last_response else None,
            "base_url": self.base_url,
            "timeout": self.timeout,
        }


if __name__ == "__main__":
    client = APIClient()

    posts = client.get_posts(5)
    if posts:
        print("\nПоследние посты:")
        for post in posts[:3]:
            print(f"  - {post['title'][:50]}...")

    quote = client.get_random_quote()
    if quote:
        print("\nЦитата дня:")
        print(f"  \"{quote['text']}\"")
        print(f"  — {quote['author']}")

    print(f"\nСтатистика: {client.get_statistics()}")
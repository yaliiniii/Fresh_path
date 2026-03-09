import requests

def test_add_habit():
    url = "http://127.0.0.1:8000/habits/?user_id=1"
    payload = {"name": "Test Habit"}
    response = requests.post(url, json=payload)
    print(f"POST Status: {response.status_code}")
    print(f"POST Response: {response.json()}")

    if response.status_code == 200:
        habit_id = response.json()["id"]
        # Now get habits for today
        from datetime import date
        today = date.today().isoformat()
        get_url = f"http://127.0.0.1:8000/habits/?user_id=1&date={today}"
        get_res = requests.get(get_url)
        print(f"GET Status: {get_res.status_code}")
        print(f"GET Response: {get_res.json()}")

if __name__ == "__main__":
    test_add_habit()

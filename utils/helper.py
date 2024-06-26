import json
import os

# Path to the JSON file
# Получаем путь до директории проекта
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../.'))

# Создаем универсальный путь к файлу
USER_DATA_PATH = os.path.join(project_root, 'test_data', 'user_data.json')


def save_token(content):
    with open(".env", "w") as f:
        for key, value in content.items():
            f.write(f"{key}={value}\n")


def load_data():
    if os.path.exists(USER_DATA_PATH):
        with open(USER_DATA_PATH, "r") as file:
            return json.load(file)
    else:
        return {"users": {}}


def save_data(data):
    with open(USER_DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)


def add_user(email, workspace_id, folder_id, role):
    data = load_data()
    data["users"][email] = {
        "workspace_id": workspace_id,
        "folder_id": folder_id,
        "role": role,
    }
    save_data(data)


def get_user_data(email):
    data = load_data()
    return data["users"].get(email, None)


def get_wid(email):
    data = load_data()
    return data["users"][email].get("workspace_id")


def get_fid(email):
    data = load_data()
    return data["users"][email].get("folder_id")

from db_helper import add_user

DATA_SIZE = 10


def creat_demo_data():
    for idx in range(DATA_SIZE):
        data = {
            "name": f"user {idx}",
            "username": f"user_{idx}",
            "phone_number": "01521202936",
            "email": f"user_{idx}@email.com"
        }
        add_user(**data)


if __name__ == "__main__":
    creat_demo_data()

from instagrapi import Client
import os

USERNAME = "team7solutions"
PASSWORD = "team7solutions1"


def login_client():

    print("Starting login...")

    cl = Client()

    # human-like delay
    cl.delay_range = [1, 3]

    # mobile device emulation
    cl.set_device({
        "manufacturer": "samsung",
        "model": "SM-G973F",
        "android_version": 26
    })

    # load trusted session if exists
    if os.path.exists("session.json"):
        print("Loading existing session...")
        cl.load_settings("session.json")

    try:
        print("Attempting login...")
        cl.login(USERNAME, PASSWORD)
        print("Login API returned")

    except Exception as e:
        print("Login Exception:", e)
        return None

    # save trusted device session
    cl.dump_settings("session.json")

    print("✅ Login Successful")
    return cl


if __name__ == "__main__":
    login_client()
from packages import fetch, login, OTP as otp

def main():
    user = fetch.user("admin","1234")
    login.login_attempt(user)

if __name__ == "__main__":
    main()

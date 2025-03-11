try:
    username = "Admin"
    password = "ad123@"

    if len(username) >= len(password):
        print("password length Suffiecient")
    else:
        if "a0" in password:
            print(username.upper())
        else:
            print(hello)

except Exception:
    print("Exception available")
def greet(name: str) -> str:
    return f"[feature] Hello, {name}"


if __name__ == "__main__":
    message = greet("Git Demo")
    print(message)

    user_message = greet("Second Commit")
    print(user_message)

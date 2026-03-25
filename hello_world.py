def greet_user(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Willkommen bei Softwareengineering."
if __name__ == "__main__":
    user_name = input("Geben Sie Ihren Namen ein: ")
    print(greet_user(user_name))
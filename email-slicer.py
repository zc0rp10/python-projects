from email_validator import validate_email, EmailNotValidError


def validate_email_internal(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
        return False


def get_user_email() -> str:
    email_valid: bool = False
    email: str = ""

    while not email_valid:
        email = input("Enter your email address: ").strip()
        email_valid = validate_email_internal(email)

    return email


def get_split_email(email: str) -> tuple[str, str, str]:
    if not validate_email_internal(email):
        raise Exception("Invalid e-mail address")

    username, domain_ext = email.split("@")
    domain, ext = domain_ext.rsplit(".", 1)

    return username, domain, ext


def main():
    print("==== E-Mail Slicer ====")
    email = get_user_email()
    user_name, domain, extension = get_split_email(email)
    print_result(user_name, domain, extension)


def print_result(user_name: str, domain: str, extension: str):
    print("\n")
    print(f"User name: {user_name}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")


if __name__ == "__main__":
    main()

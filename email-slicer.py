# collect email from the user
# validate the email
# splice the email using the @, first part as username, secondpart i saved as domain
# split domain from the extension

import re


def validate_email(email: str) -> bool:
    email_regex = re.compile(
        r"^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+"
        r"(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|"
        r"((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?"
        r"(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]"
        r"|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|"
        r"(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|"
        r"[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*"
        r"(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@"
        r"((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|"
        r"(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])"
        r"([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*"
        r"([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+"
        r"(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|"
        r"(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])"
        r"([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*"
        r"([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$",
        re.IGNORECASE,
    )
    return email_regex.match(email) is not None


def get_user_email() -> str:
    email_valid: bool = False
    email: str = ""

    while not email_valid:
        email = input("Enter your email address: ").strip()
        email_valid = validate_email(email)
        if not email_valid:
            print("Invalid email format. Try again..")

    return email


def get_split_email(email: str) -> tuple[str, str, str]:
    if not validate_email(email):
        raise Exception("Invalid e-mail address")

    username, domain_ext = email.split("@")
    domain, ext = domain_ext.split(".")

    return username, domain, ext


def main():
    print("==== E-Mail Slicer ====")
    email = get_user_email()
    user_name, domain, extension = get_split_email(email)
    print("\n")
    print(f"User name: {user_name}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")


if __name__ == "__main__":
    main()

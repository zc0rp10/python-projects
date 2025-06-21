from email_validator import ValidatedEmail, validate_email, EmailNotValidError
from typing import Optional


def main() -> None:
    print("==== E-Mail Slicer ====\n")

    email_validated: Optional[ValidatedEmail] = None

    while not email_validated:
        try:
            email_input: str = input("Enter your email address: ").strip()
            email_validated = validate_email(email_input, check_deliverability=False)
        except EmailNotValidError as e:
            print(f"Invalid e-mail: {e}")

    (user_name, domain_and_extension) = email_validated.email.split("@")
    domain_parts = domain_and_extension.split(".")
    domain = ".".join(domain_parts[:-1])
    extension = domain_parts[-1]

    print("\nEmail successfully parsed:")
    print(f" - User name : {user_name}")
    print(f" - Domain    : {domain}")
    print(f" - Extension : {extension}")


if __name__ == "__main__":
    main()

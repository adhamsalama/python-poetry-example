import secrets
import string


def generate_random_id() -> str:
    return "".join(
        secrets.choice(
            string.ascii_uppercase + string.ascii_lowercase,
        )
        for _ in range(10)
    )

from models.base_model import BaseModel
import peewee as pw
import re
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


class User(BaseModel, UserMixin):
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(unique=True, null=False)
    password_hash = pw.TextField(null=False)
    password = None
    gender = pw.CharField(null=True)

    def validate(self):
        email_existing = User.get_or_none(User.email == self.email)
        if email_existing:
            self.errors.append("Email already exists")

        existing_username = User.get_or_none(User.username == self.username)
        if existing_username:
            self.errors.append("Username already exists!")

        if len(self.password) <= 6:
            self.errors.append("Password should be longer than 6 characters")

        has_lowercase = re.search(r"[a-z]", self.password)
        has_uppercase = re.search(r"[A-Z]", self.password)
        has_speacial_char = re.search(
            r"[\[ \] \{ \} \# \% \$ \* \@]", self.password)

        if has_lowercase and has_uppercase and has_speacial_char:
            self.password_hash = generate_password_hash(self.password)
        else:
            self.errors.append(
                "Password either does not have a lowercase, uppercase, or a special character")

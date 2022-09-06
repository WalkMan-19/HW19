import base64
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import hashlib


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        user = self.dao.get_one(uid)
        user.username = data.get("username")
        user.password = self.get_hash(data["password"])
        user.role = data.get("role")
        self.dao.update(user)

    def update_partial(self, data):
        uid = data.get("id")
        user = self.dao.get_one(uid)
        if "username" in data:
            user.username = data.get("username")
        if "password" in data:
            user.password = self.get_hash(data["password"])
        if "role" in data:
            user.role = data.get("role")
        self.dao.update(user)

    def delete(self, uid):
        return self.dao.delete(uid)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def compare_passwords(self, password_hash, password) -> bool:
        decode_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decode_digest, hash_digest)

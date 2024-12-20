import json

from qa_guru_hw17 import utils

import os.path

SCHEMA_DIR = os.path.abspath(os.path.join(os.path.dirname(utils.__file__), "schemas"))


def get_users_schema():
    with open(os.path.join(SCHEMA_DIR, 'users_schema.json')) as file:
        return json.loads(file.read())


def get_user_update_schema():
    with open(os.path.join(SCHEMA_DIR, 'user_update_schema.json')) as file:
        return json.loads(file.read())


def get_user_create_schema():
    with open(os.path.join(SCHEMA_DIR, 'user_create_schema.json')) as file:
        return json.loads(file.read())


def get_user_existing_schema():
    with open(os.path.join(SCHEMA_DIR, 'user_get_existing_schema.json')) as file:
        return json.loads(file.read())


def get_login_success_schema():
    with open(os.path.join(SCHEMA_DIR, 'login_success_schema.json')) as file:
        return json.loads(file.read())


def get_login_failure_schema():
    with open(os.path.join(SCHEMA_DIR, 'login_failure_schema.json')) as file:
        return json.loads(file.read())

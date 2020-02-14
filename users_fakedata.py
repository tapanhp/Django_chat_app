import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

import django

django.setup()

from users.models import User
from faker import Faker

fackegen = Faker()


def user_create(N=5):
    for entry in range(N):
        fake_username = fackegen.name()
        fakuse_firstname = fackegen.name()
        fake_lastname = fackegen.name()
        fake_email = fackegen.email()
        fake_password = fackegen.password()
        fake_phone = fackegen.phone_number()
        user = User.objects.create_user(username=fake_username, first_name=fakuse_firstname, last_name=fake_lastname,
                                        email=fake_email, password=fake_password, phone=fake_phone)


if __name__ == '__main__':
    print("populating data...")
    user_create(2)
    print("populating done.")

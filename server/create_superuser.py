import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproj.settings")
django.setup()

User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")

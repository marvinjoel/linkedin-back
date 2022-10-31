from django.contrib import admin

from accounts.models import User, SocialMedia

admin.site.register(User)
admin.site.register(SocialMedia)

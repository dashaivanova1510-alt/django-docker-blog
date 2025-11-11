from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Створюємо групу "author"
    Group.objects.get_or_create(name='author')

    moderator_group, created = Group.objects.get_or_create(name='moderator')

    if sender.name == 'blog':
        try:
            Comment = apps.get_model('blog', 'Comment')
            content_type = ContentType.objects.get_for_model(Comment)
            
            comment_permission_delete = Permission.objects.get(
                content_type=content_type,
                codename='delete_comment'
            )
            comment_permission_change = Permission.objects.get(
                content_type=content_type,
                codename='change_comment'
            )

            moderator_group.permissions.add(comment_permission_delete, comment_permission_change)
            print('До групи "moderator" додано права на коментарі')
        except (LookupError, Permission.DoesNotExist):

            pass
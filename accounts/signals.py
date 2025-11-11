from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Comment 

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    author_group, created = Group.objects.get_or_create(name='author')
    if created:
        print('Групу "author" створено')

    moderator_group, created = Group.objects.get_or_create(name='moderator')
    if created:
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
        print('Групу "moderator" створено з правами на видалення та зміну коментарів')
from microdjango.db import migrations, models

class Migration(migrations.Migration):
    operations = [
        {'model': 'Tag', 'fields': {
            'name': models.CharField(),
            'num': models.IntegerField(),
        }},
    ]

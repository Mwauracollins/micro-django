from microdjango.db import migrations, models

class Migration(migrations.Migration):
    operations = [
        migrations.CreateModel('Tag',
            fields={
                'name': models.CharField(),
                'id': models.IntegerField(),
            },
    )]

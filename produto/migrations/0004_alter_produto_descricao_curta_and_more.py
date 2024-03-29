# Generated by Django 5.0 on 2024-01-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0003_alter_produto_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="descricao_curta",
            field=models.TextField(max_length=255, verbose_name="Descrição Curta"),
        ),
        migrations.AlterField(
            model_name="produto",
            name="preco_marketing",
            field=models.FloatField(default=0, verbose_name="Preço"),
        ),
        migrations.AlterField(
            model_name="produto",
            name="preco_marketing_promocional",
            field=models.FloatField(default=0, verbose_name="Preço Promo"),
        ),
    ]

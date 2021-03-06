# Generated by Django 2.1.7 on 2019-03-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190327_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_method',
            field=models.SmallIntegerField(choices=[('wexin', '微信'), ('zhifubao', '支付宝'), ('orther', '其他')], default=1, verbose_name='支付方式'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('waitpay', '待支付'), ('success', '已支付'), ('cancel', '已取消')], default='待支付', max_length=32, verbose_name='订单状态'),
        ),
    ]

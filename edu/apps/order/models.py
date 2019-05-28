from django.db import models

class Order(models.Model):
    '''订单表'''

    ORDER_STATUS = (
        ('waitpay', "待支付"),
        ('success', "已支付"),
        ("cancel", "已取消"),
    )
    PAY_METHOD = (
        ('wexin', "微信"),
        ('zhifubao', "支付宝"),
        ("orther", "其他"),
    )

    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=64, verbose_name="订单号")
    user = models.ForeignKey('user.User', on_delete=models.PROTECT,null=True, verbose_name="下单用户")
    course = models.ForeignKey('course.Course', on_delete=models.PROTECT,null=True, verbose_name="下单商品")
    usercourse = models.ForeignKey('course.UserCourse', on_delete=models.PROTECT,null=True, verbose_name="课程用户关联")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0, verbose_name="商品总金额")
    discount = models.DecimalField(max_digits=10, decimal_places=2,default=0, verbose_name="免付金额")
    pay_method = models.CharField(max_length=64,choices=PAY_METHOD, default="其他", verbose_name="支付方式")
    status = models.CharField(max_length=32, choices=ORDER_STATUS, default='待支付',verbose_name="订单状态")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "order"
        ordering = ['c_time']
        verbose_name = '订单'
        verbose_name_plural = '订单'





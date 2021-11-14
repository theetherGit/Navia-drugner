from django.db import models

class DrugList(models.Model):
    sku_id = models.IntegerField(verbose_name="SKU ID", primary_key=True, unique=True, null=False)
    product_id = models.IntegerField(verbose_name="Product ID", null=True)
    sku_name = models.CharField(verbose_name="SKU Name", max_length=200, null=True)
    price = models.CharField(verbose_name="Price", max_length=200, null=True)
    manufacturer_name = models.CharField(verbose_name="Manufacturer Name", max_length=200, null=True)
    salt_name = models.CharField(verbose_name="Salt Name", max_length=200, null=True)
    drug_form = models.CharField(verbose_name="Drug Form", max_length=200, null=True)
    Pack_size = models.CharField(verbose_name="Pack Size", max_length=200, null=True)
    strength = models.CharField(verbose_name="Strength", max_length=200, null=True)
    product_banned_flag = models.CharField(verbose_name="Ban", max_length=200, null=True)
    unit = models.CharField(verbose_name="unit", max_length=200, null=True)
    price_per_unit = models.CharField(verbose_name="Price Per Unit", max_length=200, null=True)

    class Meta:
        ordering = ['product_id']

    def __str__(self):
        return f'''{self.sku_id} ===> {self.sku_name} ==> {self.salt_name}'''
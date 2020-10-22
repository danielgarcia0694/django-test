from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import DecimalValidator, MaxLengthValidator, MinLengthValidator, MinValueValidator


class Product(models.Model):
    name = models.CharField(
        verbose_name='Producto',
        max_length=250,
        null=False,
        blank=False,
        validators=[MinLengthValidator(3, "Invalid product name"), MaxLengthValidator(55, "Invalid product name")]
    )
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField(validators=[MinValueValidator(0, "Invalid stock value")])

    def clean(self):
        """
            Validation: El producto debe tener un valor mayor a 0 y menor a 99999.9
            Message in case of failure: "Invalid value"
        """
        if self.value < 0 or self.value > 99999.9:
            raise ValidationError({"value": "Invalid value"})

        """
            Validation: El producto en caso de tener un discount value, debe ser menor al precio normal.
            Message in case of failure: "Invalid discount value"
        """
        # if self.discount_value < 0 or self.discount_value > 99999.9:
        #     raise ValidationError({"discount_value": "Invalid value"})

        if self.discount_value > self.value:
            raise ValidationError({"discount_value": "Invalid discount value"})

    def __str__(self):
        return self.name
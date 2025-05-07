from django.db import models
# from category_management.models import Category
import uuid

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey("category_management.Category", on_delete=models.CASCADE, related_name="items")
    business = models.ForeignKey(
        "business_management.Business",
        on_delete=models.CASCADE,
        related_name="items"
    )
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('name', 'business')  # ✅ Restricción para nombre único por negocio

    def __str__(self) -> str:
        return self.name

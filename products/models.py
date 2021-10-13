from django.db import models
from multiselectfield import MultiSelectField
from djchoices import DjangoChoices, ChoiceItem


class ProductCategory(models.Model):
    """
    Class to define categories for products and Products Types within the categories
    """
    class Meta:
        """
        Class to designate plural name
        """
        verbose_name_plural = 'Categories'

    PRODUCT_TYPE_CHOICES = (
        (1, "Earrings"),
        (2, "Pendants / Necklaces"),
        (3, "Rings"),
        (4, "Bracelets / Bangles"),
        (5, "Tops"),
        (6, "Knitwear"),
        (7, "Skirts"),
        (8, "Shorts"),
        (9, "Trousers"),
        (10, "Jeans"),
        (11, "Ponchos"),
        (12, "Beanie Hats"),
        (13, "Scarves"),
        (14, "Beanie Hats"),
        (15, "Leather Bags"),
        (16, "Beltbags / Bumbags"),
        (17, "Wallets / Purses"),
        (18, "Belts"),
    )

    name = models.CharField(max_length=90)
    friendly_name = models.CharField(max_length=90, null=False, blank=False)
    product_type = MultiSelectField(
                                    'ProductType', max_length=3,
                                    choices=PRODUCT_TYPE_CHOICES,
                                    default="Earrings")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductType(models.Model):
    """
    Class to identify different product types and which Categories they belong to
    """
    class Meta:
        """
        Class to designate plural name
        """
        verbose_name_plural = 'Product Types'

    name = models.CharField(max_length=90)
    friendly_name = models.CharField(max_length=90, null=False, blank=False)

    PRODUCT_CATEGORIES = (
        ('jewellery', 'Jewellery'),
        ('leather_accessories', 'Leather Accessories'),
        ('blankets', 'Blankets'),
        ('knitted_accessories', 'Knitted Accessories'),
        ('clothing', 'Clothing'),
        )

    product_categories = models.CharField(max_length=30,
                                          choices=PRODUCT_CATEGORIES)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Class to define the generic product model - Subclasses for products with
    differing sizes are properties are included as sub-classes
    """
    class ProductProperties(DjangoChoices):
        """
        Subclass for general product properties - use on more info section
        """
        sterling_silver = ChoiceItem("SS")
        gold_plated = ChoiceItem("GP")
        wool = ChoiceItem("PW")
        hand_crafted = ChoiceItem("HC")
        fairly_produced = ChoiceItem("FP")
        low_environmental_impact = ChoiceItem("LI")
   
    class SizeType(DjangoChoices):
        """
        Subclass to define product size options - use to display size entry
        """
        one_size = ChoiceItem("universal_size_type")
        jewellery_sizes = ChoiceItem("jewellery_size_type")
        clothing_sizes = ChoiceItem("clothing_size_type")

    product_name = models.CharField(max_length=90)
    product_category = models.ForeignKey(
        'ProductCategory', null=True, blank=False, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(
        'ProductType', null=True, blank=False, on_delete=models.SET_NULL)
    product_properties = MultiSelectField(max_length=2,
                                          choices=ProductProperties.choices,
                                          default="FP")
    product_sku = models.CharField(max_length=90, null=False, blank=False)
    product_description = models.TextField()
    product_is_bestseller = models.BooleanField(default=False,
                                                null=False, blank=False)
    size_type = MultiSelectField(max_length=30, choices=SizeType.choices,
                                 default="universal_size_type")
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    rrp_price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class Ring(Product):
    """
    Child class of product to define Rings products
    they have different properties & sizes
    """

    class JewelleryProperties(DjangoChoices):
        """
        Subclass of Rings for metal choice definition
        """
        silver = ChoiceItem("SR")
        gold = ChoiceItem("GD")

    class RingSizes(DjangoChoices):
        """
        Subclass of Rings for size run definition
        """
        L = ChoiceItem("6")
        N = ChoiceItem("7")
        P = ChoiceItem("8")
        S = ChoiceItem("9")
        U = ChoiceItem("10")

    jewellery_properties = models.CharField(
        max_length=2, choices=JewelleryProperties.choices)
    ring_sizes = MultiSelectField(max_length=2, choices=RingSizes.choices,
                                   default="6")

    def __str__(self):
        return self.product_name


class Clothing(Product):
    """
    Child class of product to define Clothing products
    they have different properties & sizes
    """

    class ClothingSizes(DjangoChoices):
        """
        Subclass of Clothing for size run definition
        """
        XS = ChoiceItem("XS")
        S = ChoiceItem("S")
        M = ChoiceItem("M")
        L = ChoiceItem("L")
        XL = ChoiceItem("XL")
    
    clothing_sizes = MultiSelectField(max_length=2, choices=ClothingSizes.choices, default="XS")

    def __str__(self):
        return self.product_name

from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

# Modelo para Categorias
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# Modelo para Marcas (Brand)
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# Modelo de Produto
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Campo SKU (Stock Keeping Unit)
    sku = models.CharField(max_length=100, unique=True, help_text="Código único para controle de estoque")
    
    # Percentual de desconto (por exemplo, 10.00 para 10%)
    discount = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0.00, 
        help_text="Percentual de desconto (em %)"
    )
    
    # Controle de estoque geral
    stock = models.PositiveIntegerField(default=0, help_text="Quantidade disponível em estoque")
    available = models.BooleanField(default=True)
    
    # Tamanhos disponíveis: utilizando ArrayField para armazenar os tamanhos (PP, P, M, G, GG)
    sizes = ArrayField(
        models.CharField(
            max_length=2,
            choices=[('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')]
        ),
        blank=True,
        default=list,
        help_text="Tamanhos disponíveis"
    )
    
    # Opções de cor: pode ser livre ou padronizada. Se desejar padronizar, poderá usar ManyToMany.
    color_options = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list,
        help_text="Opções de cores disponíveis"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        # Gera o slug automaticamente se não estiver preenchido
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# Modelo para imagens dos produtos
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(
        max_length=255, 
        blank=True,
        help_text="Texto alternativo para a imagem"
    )
    
    def __str__(self):
        return f"Imagem de {self.product.name}"

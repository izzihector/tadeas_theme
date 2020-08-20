from odoo.http import request
from odoo import models, fields, api


class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Product Brands'

    name = fields.Char("Brand Name", required=True)
    brand_image = fields.Binary("brand_image", attachment=True)
    is_website_publish = fields.Boolean("is_website_publish")

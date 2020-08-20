from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo.addons.http_routing.models.ir_http import slug
from odoo.osv import expression


class WebsiteSaleExt(WebsiteSale):
    def _get_search_domain_ext(self, search, category, attrib_values, brand_values, search_in_description=True):
        domains = [request.website.sale_product_domain()]
        if search:
            for srch in search.split(" "):
                subdomains = [
                    [('name', 'ilike', srch)],
                    [('product_variant_ids.default_code', 'ilike', srch)]
                ]
                if search_in_description:
                    subdomains.append([('description', 'ilike', srch)])
                    subdomains.append([('description_sale', 'ilike', srch)])
                domains.append(expression.OR(subdomains))

        if category:
            domains.append([('public_categ_ids', 'child_of', int(category))])

        if attrib_values:
            attrib = None
            ids = []
            for value in attrib_values:
                if not attrib:
                    attrib = value[0]
                    ids.append(value[1])
                elif value[0] == attrib:
                    ids.append(value[1])
                else:
                    domains.append([('attribute_line_ids.value_ids', 'in', ids)])
                    attrib = value[0]
                    ids = [value[1]]
            if attrib:
                domains.append([('attribute_line_ids.value_ids', 'in', ids)])

        if brand_values:
            domains.append([('product_brand_id', 'in', brand_values)])

        return expression.AND(domains)

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        if ppg:
            try:
                ppg = int(ppg)
                post['ppg'] = ppg
            except ValueError:
                ppg = False
        if not ppg:
            ppg = request.env['website'].get_current_website().shop_ppg or 20

        res = super(WebsiteSaleExt, self).shop(page=page, category=category,
                                               search=search, ppg=ppg, **post)
        # For Attributes
        attrib_list = request.httprequest.args.getlist('attrib')
        attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        attributes_ids = {v[0] for v in attrib_values}
        attrib_set = {v[1] for v in attrib_values}

        # For Brands
        brand_list = request.httprequest.args.getlist('brand-id')
        brand_values = [list(map(str, v.split("-"))) for v in brand_list if v]
        brand_set = set([int(v[1]) for v in brand_values])

        Product = request.env['product.template']

        domain = self._get_search_domain_ext(search, category, attrib_values,
                                             list(brand_set))
        keep = QueryURL('/shop', category=category and int(category),
                        search=search, attrib=attrib_list,
                        order=post.get('order'), brands=brand_list)

        url = "/shop"

        if category:
            url = "/shop/category/%s" % slug(category)

        if attrib_list:
            post['attrib'] = attrib_list
        if brand_list:
            post['brands'] = brand_list

        if search:
            post["search"] = search
        product_count = Product.search_count(domain)
        pager = request.website.pager(url=url, total=product_count,
                                      page=page, step=ppg, scope=7,
                                      url_args=post)
        products = Product.search(domain, limit=ppg, offset=pager['offset'],
                                  order=self._get_search_order(post))

        ProductAttribute = request.env['product.attribute']
        ProductBrand = request.env['product.brand']
        if products:
            selected_products = Product.search(domain, limit=False)
            attributes = ProductAttribute.search([('attribute_line_ids.product_tmpl_id', 'in', selected_products.ids)])
            prod_brands = []
            for product in selected_products:
                if product.product_brand_id:
                    prod_brands.append(product.product_brand_id.id)
            brands = ProductBrand.browse(list(set(prod_brands)))
        else:
            attributes = ProductAttribute.browse(attributes_ids)
            brands = ProductBrand.browse(brand_set)


        res.qcontext.update({
            'pager': pager, 'products': products,
            'brands': brands, 'bins': TableCompute().process(products, ppg),
            'attributes': attributes, 'search_count': product_count,
            'attrib_values': attrib_values,
            'brand_values': brand_values, 'brand_set': brand_set,
            'attrib_set': attrib_set,
            'ppg': ppg, 'keep': keep,
            'search': search,
        })
        return res

    @http.route(['/shop/get_brand'], type='http', auth='public', website=True)
    def get_brand_carousel(self, **post):
        brands = request.env['product.brand'].search(
            [('is_website_publish', '=', True)], limit=int(post.get('brand_objects_limit')))
        if brands:
            return request.render("website_product_brand.brand_slider_content",
                                  {'brands': brands})
        return ''

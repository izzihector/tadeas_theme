{
    'name': 'Theme Tadeas',
    'category': 'Theme/eCommerce',
    'summary': 'Theme Tadeas is Odoo Multipurpose Theme'
               'with Modern style, Extremely customizable, Clean and Fully Responsive.',
    'description': 'Theme Tadeas is Odoo Multipurpose Theme'
                   'with Modern style, Extremely customizable, Clean and Fully Responsive.',
    'version': '13.0.1.0.0',
    'author': 'Tecspek',
    'data': [
        'views/assets.xml',
        'views/mid_header.xml',
        'views/product_carousel.xml',
        'views/customize_assets.xml',
        'views/shop_template.xml',
        'views/product_public_category_view.xml',
        'views/collapse_categories_template.xml',
        'views/single_product_template.xml',
        'views/contact_us.xml',
        'views/about_us.xml',

        'snippets/s_our_team.xml',
        'snippets/s_services.xml',
        'snippets/s_tab_carousel.xml',
        'snippets/s_theme_banner.xml',
        'snippets/s_three_img_contain.xml',
        'snippets/s_three_imgs.xml',
        'snippets/s_ecommerce.xml',
        'snippets/s_business.xml',
    ],
    'depends': [
        'mass_mailing',
        'website_blog',
        'website_crm',
        'website_sale',
        'website_sale_wishlist',
        'website_sale_comparison',
        'website_sale_stock',
        # ================================================================ #
        # TecSpek Extra Addons
        # ================================================================ #

        # 'website_product_quick_view',
        # 'website_product_carousel',
        # 'website_product_brand',
    ],
    'demo': [
        'data/brand_demo.xml',
        'data/homepage.xml',
        'data/footer.xml',
        'data/menu.xml',
        'data/homepage_bussines.xml',
    ],
    'images': [
        'static/description/main.png',
        'static/description/full_screenshot.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'price': 75,
    'currency': 'EUR',
    'live_test_url': 'http://159.65.4.139:7070/r/NDD',
}

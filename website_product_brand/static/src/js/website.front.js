odoo.define('website_product_brand.website_front_js', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    publicWidget.registry.js_brand_in_slide = publicWidget.Widget.extend({
        selector: ".s_brand_carousel",
        disabledInEditableMode:!1,
        start: function () {
            var t = this;
            console.log(">>>>>>>>>test>>>>>>>",t.$target)
            t.editableMode && t.$target.empty().append('<div class="container"><div class="brand-title-js"><h2>Our Brand</h2></div></div>'), t.editableMode || $.get("/shop/get_brand", {brand_objects_limit: t.$target.attr("data-brand_objects_limit") || 0}).then(function (e) {
                e && (t.$target.empty().append(e), t.$el.find(".owl-carousel").owlCarousel({
                    items: 4,
                    margin: 25,
                    navigation: !0,
                    pagination: !1,
                    animateOut: "slideOutDown",
                    animateIn: "flipInX",
                    loop: !1,
                    responsive: {
                        0: {items: 1},
                        481: {items: 2},
                        768: {items: t.$target.data("brand_objects_in_slide")},
                        1024: {items: t.$target.data("brand_objects_in_slide")}
                    }
                }))
            })
        }
    });
});

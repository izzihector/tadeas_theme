odoo.define('website_product_brand.brand_carousel_editor', function (require) {
    "use strict";

    var options = require('web_editor.snippets.options');
    options.registry.js_get_brand_in_slide = options.Class.extend({
         _setActive: function () {
            this._super.apply(this, arguments);
            var activeLimit = this.$target.data('brand_objects_in_slide') || 3;

            this.$el.find('[data-brand_objects_in_slide]').removeClass('active');
            this.$el.find('[data-brand_objects_in_slide=' + activeLimit + ']').addClass('active');
        },
        start: function () {
            var t = this;
            setTimeout(function () {
                if (t.$target.attr("data-brand_objects_in_slide")) {
                    var a = t.$target.attr("data-brand_objects_in_slide");
                    $(t.$el).find('we-button[data-brand_objects_in_slide="' + a + '"]').addClass("active")
                } else $(t.$el).find('we-button[data-brand_objects_in_slide="' + a + '"]').addClass("active")
            }, 100)
        }, brand_objects_in_slide: function (t, a, i) {
            0 == t && (a = parseInt(a), this.$target.attr("data-brand_objects_in_slide", a).data("brand_objects_in_slide", a), this.trigger_up("animation_start_demand", {
                editableMode: !0,
                $target: this.$target
            }), setTimeout(function () {
                i.parent().find("a").removeClass("active"), i.addClass("active")
            }, 100))
        }
    }), options.registry.js_brand_limit = options.Class.extend({
        _setActive: function () {
            this._super.apply(this, arguments);
            var activeLimit = this.$target.data('brand_objects_limit') || 3;

            this.$el.find('[data-brand_objects_limit]').removeClass('active');
            this.$el.find('[data-brand_objects_limit=' + activeLimit + ']').addClass('active');
        },start: function () {
            var t = this;
            setTimeout(function () {
                if (t.$target.attr("data-brand_objects_limit")) {
                    var a = t.$target.attr("data-brand_objects_limit");
                    $(t.$el).find('we-button[data-brand_objects_limit="' + a + '"]').addClass("active")
                } else $(t.$el).find('we-button[data-brand_objects_limit="' + a + '"]').addClass("active")
            }, 100)
        }, brand_objects_limit: function (t, a, i) {
            0 == t && (a = parseInt(a), this.$target.attr("data-brand_objects_limit", a).data("brand_objects_limit", a), this.trigger_up("animation_start_demand", {
                editableMode: !0,
                $target: this.$target
            }), setTimeout(function () {
                i.parent().find("a").removeClass("active"), i.addClass("active")
            }, 100))
        }
    });
});


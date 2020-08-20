$(document).ready(function(){ 
	if($('.clear-brand-filter')){
		$(".clear-brand-filter").click(function(e){
			var self=$(this)
            var curent_div = $(self).parents('.product_brand_shop').find('ul');
            e.preventDefault()
			$(curent_div).find("input:checked").each(function(){
				$(this).removeAttr("checked");
			});
			$("form.js_attributes input").closest("form").submit();
		});
	}
	if($('.clear-attrib-filter')){
		$(".clear-attrib-filter").click(function(e){
			var target = $(e.target);
			e.stopPropagation();
			e.preventDefault();
            if(target.parent().next('.nav-pills').length){
                target.parent().next('.nav-pills').find("input:checked").each(function(){
                    $(this).removeAttr("checked");
                });
                $("form.js_attributes input").closest("form").submit();
            }else{
                target.parents().find('label').find("input:checked").each(function(){
                    $(this).removeAttr("checked");
                });
                target.parent().next('select').find("option:selected").each(function(){
                    $(this).removeAttr("selected");
                });
                $("form.js_attributes input").closest("form").submit();
            }
		});
	}
});


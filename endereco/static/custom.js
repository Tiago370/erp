django.jQuery(function() {
    django.jQuery('.mask-cep ').mask('00000-000', {reverse: true});
    django.jQuery('#endereco_form').submit(function() {
        django.jQuery('#endereco_form').find(':input[class*="mask-"]').unmask();
    });

});
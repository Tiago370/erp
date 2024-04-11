// var SPMaskBehavior = function (val) {
//     return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-0000';
//   },
//   spOptions = {
//     onKeyPress: function(val, e, field, options) {
//         field.mask(SPMaskBehavior.apply({}, arguments), options);
//       }
//   };

// django.jQuery(function() {
//     django.jQuery('.mask-whatsapp').mask(SPMaskBehavior, spOptions);
// });
django.jQuery(function() {
    django.jQuery('.mask-whatsapp').mask('(00) 0000-0000', {reverse: true});
});
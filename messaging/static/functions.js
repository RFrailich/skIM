$("<select />").appendTo("nav");

$("<option />", {
   "selected": "selected",
   "value"   : "",
   "text"    : "Go to..."
}).appendTo("nav select");

$("nav a").each(function() {
 var elem = $(this);
 $("<option />", {
     "value"   : elem.attr("href"),
     "text"    : elem.text()
 }).appendTo("nav select");
});

$("nav select").change(function() {
  window.location = $(this).find("option:selected").val();
});

$(document).ready(function() {

    $('#search_field').hide();

    $("#drop").change(function() {
        var val = $(this).val();
        
        if (val == 'Search') {
            $('#search_field').show();
        } else {
            $('#search_field').hide();
        }
    }).change();

});
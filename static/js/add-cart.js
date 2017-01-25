// CSRF token
$(document).ready(function(){
        $.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
}); 
});

//adding product to cart
function onAddSuccess()
{
  alert("Product has been added the cart");
}

function addCart(productid){
	$(document).ready(function(){
		$.post(
			url = "/cart/",
			{productid: productid},
            onAddSuccess
		);
	});
}

// deleting product from cart
function delCart(cartitemid){
    $(document).ready(function(){
        $.post(
            url = "/cart/",
            {cartitemid: cartitemid}
        );
    });
}

// changing quantity of selected product
function changeCart(cartitemid){
    quantity = document.getElementById(cartitemid).value;
    $(document).ready(function(){
        $.post(
            url = "/cart/",
            {
            cartitem: cartitemid,
            quantity: quantity
            }
        );
    });
}

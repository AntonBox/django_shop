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
        $delElement = $('input[id=' + cartitemid + ']');
        $.post(
            url = "/cart/",
            {cartitemid: cartitemid},
            onDellSuccess($delElement)
        );
    });
}

function onDellSuccess($delElement)
{
    $(document).ready(function(){
        $delElement.parent().remove();
    });
    alert("Product deleted");
}


// changing quantity of selected product
function changeCart(cartitemid, price){
    quantity = document.getElementById(cartitemid).value;
    cartitemid = cartitemid;
    price = price;
    $(document).ready(function(){
        $.post(
            url = "/cart/",
            {
            cartitem: cartitemid,
            quantity: quantity
            },
            onChangeSuccess(cartitemid, price, quantity)
        );
    });
}

function onChangeSuccess(cartitemid, price, quantity)
{
    price = price * quantity;
    element = 'price' + cartitemid;
    console.log(document.getElementById(element));
    document.getElementById(element).innerHTML = price;
}
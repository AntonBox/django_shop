
//adding product to cart
function onAddSuccess()
{
  alert("Product has been added the cart");
}

function addCart(productid){
	$.post(
		url = "/cart/cartitem/",
		{product: productid,
        quantity: 1},
        onAddSuccess
	).fail(function() {
        alert("Product already in the cart");
    });
}

// deleting product from cart
function delCart(cartitemid, prodId){
    
    cartitemid = cartitemid;
    $.post(
        url = "/cart/del/",
        {cartitemid: cartitemid},
        onDellSuccess.bind(null, prodId)
    );
}

function onDellSuccess(prodId){
    $('input[id=' + prodId + ']').parent().remove();
    alert("Product deleted");
}


// changing quantity of selected product
function changeCart(cartitemid, price){
    quantity = document.getElementById(cartitemid).value;
    $(document).ready(function(){
        $.post(
            url = "/cart/change/",
            {
                cartitemid: cartitemid,
                quantity: quantity
            },
            onChangeSuccess.bind(null, cartitemid, price, quantity)
        );
    });
}

function onChangeSuccess(cartitemid, price, quantity){
    price = price * quantity;
    element = 'price' + cartitemid;
    console.log(document.getElementById(element));
    document.getElementById(element).innerHTML = price;
}


//adding product to cart
function onAddSuccess()
{
  alert("Product has been added the cart");
}

function addCart(productid){
	$(document).ready(function(){
		$.post(
			url = "/cart/cartitem/",
			{product: productid,
            quantity: 1},
            onAddSuccess
		);
	});
}

// deleting product from cart
function delCart(cartitemid, prodId){
    $(document).ready(function(){
        $delElement = $('input[id=' + prodId + ']');
        cartitemid = cartitemid;
        $.post(
            url = "/cart/del/",
            {
            cartitemid: cartitemid
            },
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
    $(document).ready(function(){
        $.post(
            url = "/cart/change/",
            {
            product: cartitemid,
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

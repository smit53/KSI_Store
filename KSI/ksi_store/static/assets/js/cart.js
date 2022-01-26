
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var updateBtns = document.getElementsByClassName('update-cart')

    for(var i = 0; i < updateBtns.length; i++)
    {
        updateBtns[i].addEventListener('click', function(){
            var productId  = this.dataset.product
            var action = this.dataset.action
            console.log('productId: ', productId)
            console.log('User is logged in, sending data..')
            update_user(productId,action)
           
        })
    }
function update_user(productId,action){ 

    fetch('/ksi_store/update_item/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'productId':productId , 'action':action})
    })
    .then((response) => {return response.json()
    })
    .then((data) => { 
        console.log('data:', data)
        location.reload()
})
}
document.getElementsByClassName("btn-purchase")[0].addEventListener('click', purchaseClicked)
function purchaseClicked() {
    
        alert('Thank you for your purchase')
        var cartItems = document.getElementsByClassName('cart-row')
        console.log('cartItems',cartItems);
        while (cartItems.hasChildNodes()){
            cartItems.removeChild(cartItems.firstChild)
            console.log('cartItems',cartItems);

        }
    }
 
// CLothing

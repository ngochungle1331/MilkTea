document.addEventListener('DOMContentLoaded', () => {
  var message = document.getElementById("message");
  if (message != null && message.getAttribute("data-message") === "Cảm ơn bạn ! Chúng tôi đã nhận được đơn của bạn") {
    localStorage.removeItem("shoppingCart");
    element.innerHTML = '';
    renderEmptyCart();
    cart = null;
  }
});

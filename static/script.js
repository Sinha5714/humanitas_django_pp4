setTimeout(function () {
    let messages = document.getElementByID('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
function editOrderText(target){
    const csrf = document.getElementById("csrf_token")
    const div_text = target.closest("div[id='div-change-data-order']")
    let order_text = div_text.querySelector("p textarea")
    if (order_text.value.trim() == ""){
        alert("Ошибка. Введите данные.")
        return
    }
    let response = fetch("/admin/edit_order_text",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: order_text.value,
            })
    }).then(response=>{
        if (!response.ok) return;
        order_text.placeholder = order_text.value
        order_text.value = null
    })
}
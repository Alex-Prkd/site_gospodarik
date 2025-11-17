function saveChangeDiscount(target){
    const csrf = document.getElementById("csrf_token")
    const container = target.closest("div")
    let text = container.querySelector("textarea")
        if (text.value.trim() == ""){
        alert("Поле пустое!")
        return
    }
    let response = fetch("/admin/edit_discount",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: text.value,
            id: text.name
            })
    }).then(response=>{
        if (!response.ok) return;
        text.placeholder = text.value
        text.value = null
    })
}


function removeDiscount(target){
    const csrf = document.getElementById("csrf_token")
    const container = target.closest("div")
    let text = container.querySelector("textarea")
    confirm_remove = confirm("Удалить?")
    if (!confirm_remove) return;
        let response = fetch("/admin/remove_discount",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            id: text.name
            })
        }).then(response => {
            if (!response.ok) return;
            container.remove()
        })
}


function addNewDiscount(target){
    const csrf = document.getElementById("csrf_token")
    const container = target.closest("div[class='modal-content']")
    let text = container.querySelector("textarea")
    let response = fetch("/admin/add_new_discount",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: text.value
            })
        }).then(response => {
            if (!response.ok) return;
            alert("Информация добавлена")
            location.reload()
        })
}


function cleaningTextareaDiscount(target){
    const csrf = document.getElementById("csrf_token")
    const container = target.closest("div[class='modal-content']")
    let text = container.querySelector("textarea")
    text.value = null
}
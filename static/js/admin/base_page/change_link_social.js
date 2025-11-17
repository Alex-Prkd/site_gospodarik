function TgLink(target){
    let csrf = document.getElementById("csrf_token")
    const content_div = target.closest("div")
    const text_input =  content_div.querySelector("input[type='text']")
    if (text_input.value.trim() == ""){
        alert("Ошибка! Пусто поле.")
        return
    }
    let response = fetch("/admin/edit_telegram_link",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            link_telegram: text_input.value,
            })
    }).then(response=>{
        if (!response.ok) return;
        text_input.placeholder = text_input.value
        text_input.value = null
    })
}

function InstagramLink(target){
    let csrf = document.getElementById("csrf_token")
    const content_div = target.closest("div")
    const text_input =  content_div.querySelector("input[type='text']")
    if (text_input.value.trim() == ""){
        alert("Ошибка! Пусто поле.")
        return
    }
    let response = fetch("/admin/edit_instagram_link",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            link_instagram: text_input.value,
            })
    }).then(response=>{
        if (!response.ok) return;
        text_input.placeholder = text_input.value
        text_input.value = null
    })
}
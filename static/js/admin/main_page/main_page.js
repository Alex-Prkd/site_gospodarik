function editQuote(target){
    let csrf = document.getElementById("csrf_token")
    const content_div = target.closest("div[id='content-quote']")
    const text = content_div.querySelector("textarea")
    if (text.value.trim() == ""){
        alert("Ошибка! Поле пустое.")
        return
    }
    let response = fetch("/admin/edit_quote",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: text.value,
            })
    }).then(response=>{
        if (!response.ok) return;
        text.placeholder = text.value
        text.value = null
    })
}

function editFollowMeText(target){
    let csrf = document.getElementById("csrf_token")
    const content_div = target.closest("div")
    const text = content_div.querySelector("textarea")
    if (text.value.trim() == ""){
        alert("Ошибка! Поле пустое.")
        return
    }
    let response = fetch("/admin/edit_follow_me_text",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: text.value,
            })
    }).then(response=>{
        if (!response.ok) return;
        text.placeholder = text.value
        text.value = null
    })
}

function editLinkFollowMe(target){
    let csrf = document.getElementById("csrf_token")
    const content_div = target.closest("div")
    const text = content_div.querySelector("textarea")
    if (text.value.trim() == ""){
        alert("Ошибка! Поле пустое.")
        return
    }
    let response = fetch("/admin/edit_follow_me_link",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            link: text.value,
            })
    }).then(response=>{
        if (!response.ok) return;
        text.placeholder = text.value
        text.value = null
    })
}


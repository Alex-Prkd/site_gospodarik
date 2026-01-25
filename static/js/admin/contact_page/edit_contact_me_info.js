function ContactMeTitle(target){
    const csrf = document.getElementById("csrf_token")
    const text = target.closest("div").querySelector("input[type='text']")
    if (text.value.length == 0) {
        alert("Поле пустое!")
         return
     }
    fetch("/admin/contacts/new_contact_me_title",{
        method: "POST",
        headers: {
            "X-CSRFToken": csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: text.value
        })
    }).then(response =>{
        if (!response.ok) return;
        text.placeholder = text.value
        text.value = null
        alert("Сохранено.")
    })
}


function ContactMeText(target){
    const csrf = document.getElementById("csrf_token")
    const text = target.closest("div").querySelector("textarea")
    if (text.value.length == 0) {
        alert("Поле пустое!")
         return
     }
    fetch("/admin/contacts/new_contact_me_text",{
        method: "POST",
        headers: {
            "X-CSRFToken": csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: text.value
        })
    }).then(response =>{
        if (!response.ok) return;
        text.placeholder = text.value
        text.value = null
        alert("Сохранено.")
    })
}


function ContactMeNumber(target){
    const csrf = document.getElementById("csrf_token")
    const number = target.closest("div").querySelector("input[type='tel']")
    if (number.value.length == 0) {
        alert("Поле пустое!")
         return
     }
    fetch("/admin/contacts/new_contact_me_number",{
        method: "POST",
        headers: {
            "X-CSRFToken": csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            number: number.value
        })
    }).then(response =>{
        if (!response.ok) return;
        number.placeholder = number.value
        number.value = null
        alert("Сохранено.")
    })
}
function changePreview(target){
    let new_text = target.closest("div").querySelector("textarea")
    let csrf = target.closest("div").querySelector("input")
    if (new_text.value.trim() == "") {
        alert("Поле пустое!")
        return
    }

    let response = fetch("/admin/edit_preview_contact_page",{
    method: "POST",
    headers: {
        "X-CSRFToken":csrf.value,
        "Content-Type": 'application/json'
    },
    body: JSON.stringify({new_preview: new_text.value})
    }).then(response => {
        if (!response.ok){
            return
        }
        new_text.placeholder = new_text.value
        new_text.value = null
        alert("Текст сохранён.")
    })
}
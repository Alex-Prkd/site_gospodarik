function saveInactiveReview(target){
    const csrf = document.getElementById("csrf_token")
    let block_content = target.closest("div[class='col-6']")
    confirm_save = confirm("Сохранить?")
    if (!confirm_save) return;
    let response = fetch("/admin/accept_inactive_review",{
        method: "PATCH",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            review_id: block_content.id,
            })
    }).then(response => {
        if (!response.ok) return;
        alert("Отзыв сохранён.")
        block_content.closest("div[class='container-content']").remove()
    })
}


function removeInactiveReview(target){
    const csrf = document.getElementById("csrf_token")
    let block_content = target.closest("div[class='col-6']")
    confirm_remove = confirm("Удалить?")
    if (!confirm_remove) return;
    let response = fetch("/admin/delete_inactive_review",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            review_id: block_content.id,
            })
    }).then(response => {
        if (!response.ok) return;
        alert("Отзыв удалён.")
        block_content.closest("div[class='container-content']").remove()
    })
}
function removeReview(target){
    const csrf = document.getElementById("csrf_token")
    let btn_remove = target
    let content = target.closest("div[class='col-4']")
    let confirm_remove = confirm("Удалить отзыв?")
    if (!confirm_remove) return;
    let response = fetch("/admin/remove_review",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            review_id: btn_remove.id,
            })
    }).then(response => {
        if (!response.ok) return;
        alert("Отзыв удалён.")
        content.remove()
    })
}
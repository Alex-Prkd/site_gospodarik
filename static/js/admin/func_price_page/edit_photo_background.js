function confirmEditPhoto(target){
    const csrf = document.getElementById("csrf_token")
    let res = confirm("Изменить фото?")
    if (!res) return;
    let formData = new FormData();
    formData.append("photo_bg", target.files[0]);
    fetch("/admin/edit_photo_background_price_page", {
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value
        },
        body: formData,
        }).then(response =>{
            if(!response.ok){
                alert("Ошибка.")
                return
            }
            let container_photo_background = target.closest("div[id='section-container-photo']")
            container_photo_background.style.backgroundImage = "url('../static/img/background_price_page/"+target.files[0].name+"')"
        })
}
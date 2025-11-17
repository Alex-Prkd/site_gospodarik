function checkOldPreviewAvatar(content_block){
    let old_img = content_block.querySelectorAll("div[class='col-12 input-file-list-avatar']")
    if (old_img.length == 0) return;
    old_img[0].remove()
}


function addPreviewAvatar(target){
    const file = target.files[0]
    const content_block = target.closest("div[class='row']")
    const preview_div = content_block.querySelector("div[class='input-file-preview']")
    const save_btn = content_block.querySelector("button[name='saveAvatar']")
    checkOldPreviewAvatar(content_block)
    let reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onloadend = function(){
        let new_avatar_div = document.createElement("div")
        new_avatar_div.className = "col-12 input-file-list-avatar"
        const img = document.createElement("img")
        img.className = "input-file-list-img-avatar"
        img.src = reader.result
        const remove_link = document.createElement("a")
        remove_link.href = "#"
        remove_link.className = "input-file-list-remove"
        remove_link.textContent = "x"
        remove_link.onclick = function() {
                removeFileAvatar(this)
                return false
            }
        new_avatar_div.appendChild(img)
        new_avatar_div.appendChild(remove_link)
        preview_div.appendChild(new_avatar_div)
        save_btn.className = "btn btn-primary"
        save_btn.disabled = false
        }
}


function removeFileAvatar(target){
    const modal_window = target.closest("div[class='modal-content']")
    const img = modal_window.querySelector("input[id='editAvatar']")
    img.value = null
    const img_preview = modal_window.querySelector("div[class='row']").querySelector("div[class='col-12 input-file-list-avatar']")
    img_preview.remove()
    const save_btn = modal_window.querySelector("button[name='saveAvatar']")
    save_btn.className = "btn btn-dark"
    save_btn.disabled = true
}


function sendNewAvatar(target){
    let csrf = document.getElementById("csrf_token")
    let inputFile = document.getElementById("editAvatar")
    let formData = new FormData();
    formData.append("image", inputFile.files[0]);
    fetch("/admin/edit_avatar_photo/", {
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value
        },
        body: formData
    })
    .then(response =>{
        if (!response.ok){
            return
        }
        const avatar = target.closest("main").querySelector("img[class='logo-link']")
        avatar.src = "../static/img/link/"+inputFile.files[0].name
        const close_btn = target.closest("div[class='modal-content']").querySelector("button[class='btn-close btn-close-black']")
        close_btn.click()
        alert("Фото изменено.")
    })
}

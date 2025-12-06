window.addEventListener("load", function(){
    avatarPhotoContactPage()
})

window.onbeforeunload = function() {
    let preview_photo = document.getElementById("preview-photo")
    if (preview_photo.files[0]) return false;
}

function avatarPhotoContactPage(){
    const contact_canvas = document.getElementById('contact-canvas');
    const contact_ctx = contact_canvas.getContext('2d');
    const contact_img = document.getElementById('contact-image');
    contact_ctx.clearRect(0, 0, contact_canvas.width, contact_canvas.height);
    contact_ctx.beginPath();
    contact_ctx.arc(
            contact_canvas.width / 2,
            contact_canvas.height / 2,
            160,
            0,
            Math.PI * 2
    );
    contact_ctx.clip();
    let scale = Math.max(
        contact_canvas.width / contact_img.width,
        contact_canvas.height / contact_img.height
    )

    let imgWidth = contact_img.width * scale;
    let imgHeight = contact_img.height * scale;

    let x = (contact_canvas.width - imgWidth) / 2;
    let y = (contact_canvas.height - imgHeight) / 2
    contact_ctx.drawImage(contact_img,
        x, y,
        imgWidth,
        imgHeight
    );
}


function changeAvatarPhoto(target){
    let new_photo = target.files[0]
    let btn = target
    let img = btn.closest("div[class='col-6']").querySelector("img[id='contact-image']")
    let reader = new FileReader()
    reader.readAsDataURL(new_photo)
    reader.onloadend = function(){
        img.src = reader.result
        img.onload = function(){
            avatarPhotoContactPage()
        }
    }
    let save_btn = btn.closest("div").querySelector("input[name='save_image']")
    save_btn.disabled = false
}


function saveNewAvatarPhoto(target){
    const csrf = document.getElementById("csrf_token")
    let save_btn = target
    let new_photo = target.closest("div").querySelector("label input[type='file']")
    const formData = new FormData();
    formData.append("image", new_photo.files[0])
    fetch("/admin/contacts/new_preview_avatar",{
        method: "POST",
        headers: {
            "X-CSRFToken": csrf.value
        },
        body: formData
    }).then(response=>{
        if (!response.ok) return;
        alert("Фото сохранено.")
        new_photo.value = null
        save_btn.disabled = true
    })
}
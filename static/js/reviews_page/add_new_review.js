function addReview(target){
    const csrf = document.getElementById("csrf_token")
    let allow_review = true
    let content_block = target.closest("div").closest("div[class='modal-content']")
    let name = content_block.querySelector("input[name='name']")
    let social_link = content_block.querySelector("input[name='social_link']")
    let review = content_block.querySelector("textarea[name='review']")
    let photo = document.getElementById("previewReview").files
    if (name.value.trim() == ""){
        name.classList.add("err-enter")
        setTimeout(() => {
            name.classList.remove("err-enter")
        }, 3000)
        allow_review = false

    }
    if (review.value.trim() == ""){
        review.classList.add("err-enter")
        setTimeout(() => {
            review.classList.remove("err-enter")
        }, 3000)
        allow_review = false
    }
    let social_link_value
    if (social_link.value.trim() == "") {
        social_link_value = null
    }
    else{
        social_link_value = social_link.value
    }
    /* Отправка текста и фотографии(если такая имеется)*/
    if (allow_review){
        const formData = new FormData()
        formData.append("photo", photo[0])
        formData.append("data", JSON.stringify({
            name: name.value,
            social_link: social_link_value,
            review: review.value
        }))
        let response = fetch("/new_review",{
            method: "POST",
            headers: {
                "X-CSRFToken":csrf.value
            },
            body: formData
        }).then(response=>{
            name.value = null
            social_link.value = null
            review.value = null
            if (photo.length != 0) removePreviewImage();
            document.getElementById("close-modal").click()
            let response_alert = document.getElementById("alert-reviews")
            response_alert.classList.add("show")
            setTimeout(() => {
                response_alert.classList.remove("show")
            }, 3000)
        })
    }
}


function previewPhotoReview(target){
    try {
        let default_preview_img = target.closest("div[class='col-6']").querySelector("div[class='avatar-container-inner']")
        if (default_preview_img) default_preview_img.remove();    /*удаляем дефолт изобр.*/

        let img_user = target.files[0]
        let div_content_preview_photo = target.closest("div[class='col-6']").querySelector("div[id='preview-div']")
        if (document.getElementById("preview-photo")){ /*если нет canvas для превью создаём его*/
            var canvas_new_preview = document.getElementById("preview-photo")
        }
        else{
            var canvas_new_preview = document.createElement("canvas")
            canvas_new_preview.height = 150
            canvas_new_preview.width = 150
            canvas_new_preview.id = "preview-photo"
        }
        let reader = new FileReader()
        reader.readAsDataURL(img_user)
        reader.onloadend = function() {
            let image = new Image()
            image.src = reader.result
            image.onload = function() {
                let radius = Math.min(canvas_new_preview.width, canvas_new_preview.height) / 2;
                let preview_ctx = canvas_new_preview.getContext("2d")
                preview_ctx.beginPath()
                preview_ctx.clearRect(0, 0, canvas_new_preview.width, canvas_new_preview.height)
                preview_ctx.arc(
                    canvas_new_preview.width / 2,
                    canvas_new_preview.height / 2,
                    radius,
                    0,
                    Math.PI * 2
                )
                preview_ctx.clip()

                let scale = Math.max(
                    canvas_new_preview.width / image.width,
                    canvas_new_preview.height / image.height
                )

                let imgNewWidth = image.width * scale
                let imgNewHeight = image.height * scale

                let x = (canvas_new_preview.width - imgNewWidth) / 2
                let y = (canvas_new_preview.height - imgNewHeight) / 2
                preview_ctx.drawImage(
                    image,
                    x, y,
                    imgNewWidth,
                    imgNewHeight
                )

            }
        }
        if (!document.getElementById("close-preview-btn")){
            let btn_close = document.createElement("input")
            btn_close.type = "button"
            btn_close.id = "close-preview-btn"
            btn_close.addEventListener("click", function() {
                removePreviewImage()
                })
            btn_close.className = "btn-close"
            btn_close.style = "position: absolute;"

            div_content_preview_photo.appendChild(canvas_new_preview)
            div_content_preview_photo.appendChild(btn_close)
        }
    } catch(err){
        /*отмена отправки фото (при закрытие проводника), возвращаем дефоль фото*/
        removePreviewImage()
    }
}
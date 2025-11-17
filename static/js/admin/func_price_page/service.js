function demonstrationPhotoNewService(target){
    const content_block = target.closest("div[class='col-4']")
    const demonstration_block = content_block.querySelector("div[class='new-photo']")
    const file = target.files[0]
    let reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onloadend = function(){
        let new_avatar_div = '<div class="col-12 preview-photo-service">' +
            '<img class="col-8" src="' + reader.result + '">' +
            '<a href="#" onclick="removeFilePreviewPhoto(this); return false;" class="input-file-list-remove">x</a>' +
        '</div>';
        $('.new-photo').append(new_avatar_div)
    }
}

function removeFilePreviewPhoto(target){
	let input = $(target).closest('.input-photo-newService').find('input[type=file]');
	$(target).closest('.preview-photo-service').remove();
}


function addTextArea(col){
        const modalBody = document.getElementById("textarea-div");
        const div = document.createElement("div");
        div.className = col;
        modalBody.appendChild(div)
        const textarea = document.createElement("textarea");
        textarea.rows = 5;
        textarea.placeholder = "Описание";
        textarea.style = "background: white; color: black"
        textarea.className = "descriptionService"
        div.appendChild(textarea);
}


function resetFormService(target){
    const modal_body = target.closest("div[class='modal-content']").querySelector("div[class='modal-body']")
    const title = modal_body.querySelector("input[id='nameService']")
    const descriptions = modal_body.querySelectorAll("textarea[class='descriptionService']")
    const PhotoService = modal_body.querySelector("input[id='newServiceImage']")
    preview_img_div = document.getElementsByClassName("preview-photo-service")
    const price_service = modal_body.querySelector("input[id='priceNewService']")
    title.value = null
    for (let text_descriptions of descriptions) text_descriptions.remove();
    if (preview_img_div.length != 0) preview_img_div[0].remove();
    price_service.value = null
    PhotoService.value = null
};


function addNewService(target){
    const modal_body = target.closest("div[class='modal-content']").querySelector("div[class='modal-body']")
    const title = modal_body.querySelector("input[id='nameService']")
    const descriptions = modal_body.querySelectorAll("textarea[class='descriptionService']")
    const PhotoService = modal_body.querySelector("input[id='newServiceImage']")
    preview_img_div = document.getElementsByClassName("preview-photo-service")
    const price_service = modal_body.querySelector("input[id='priceNewService']")
    let csrf = document.getElementById("csrf_token")
    let descriptionList = []
    let accept = true
    if (!title.value || title.value.trim() == ""){
        alert("Введите название.")
        accept = false
    }
    if (!price_service.value){
        alert("Введите цену.")
        accept = false
    }
    if (!PhotoService.files[0]) {
        alert("Выберете фото.");
        accept = false
    }
    for (let text_area_value of descriptions){
        if (!text_area_value.value) continue;
        descriptionList.push(text_area_value.value)
    }
    if (!descriptionList.length){
        alert("Должно быть хотя бы одно описание услуги.")
        accept = false
    }
    if (accept){
        let formData = new FormData()
        formData.append("title", title.value)
        formData.append("price", price_service.value)
        formData.append("image", PhotoService.files[0])
        formData.append("descriptions", JSON.stringify(descriptionList))
        fetch("/admin/new_service",{
            method: "POST",
            headers: {
                "X-CSRFToken":csrf.value
            },
            body: formData
        }).then(response=>{
            if (!response.ok) return;
            location.reload();
        })
    }
}
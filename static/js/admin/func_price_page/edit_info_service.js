function createPreviewIMG(id){
    let input = $(".container-preview-new-photo-service_"+id+" input[type=file]")
    let file = input[0].files[0]
    if (!file.type.startsWith("image/")){
        return
    }
    let reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onloadend = function(){
        let preview_img_div = '<div id="'+id+'" class="preview-div col-6">'+
                '<img class="col-12" src="'+ reader.result +'">' +
                    '<a class="input-file-list-remove" href="#" onclick="removePreviewPhotoService('+ id +'); return false;">x</a>'+
            '</div>'
        $(".container-preview-new-photo-service_"+id).append(preview_img_div)
    }
}


function removePreviewPhotoService(id){
    let img = $(".container-preview-new-photo-service_"+ id +" input[type=file]")
    if (img[0].files.length > 0){
//        length > 1 -> Есть превью, удаляем его
        img[0].value = ""
        $(".preview-div").remove()
    }
}


function editPhoto(id, title_img){
    const csrf = document.getElementById("csrf_token")
    const input = $(".container-preview-new-photo-service_"+id+" input[type=file]")
    new_img_service = input[0].files[0]
    if (typeof new_img_service === "undefined"){
        alert("Фотография не выбрана!")
        return
    }
    let url = "/admin/edit_photo_service"
    let formData = new FormData()
    formData.append("old_img", title_img)
    formData.append("new_photo", new_img_service)
    let response = fetch(url,
        {
            method: "POST",
            headers: {
                "X-CSRFToken":csrf.value
            },
            body: formData
        }).then(response=>{
            if (!response.ok){
                return
            }
            location.reload();
        })
};


function editTitleService(service_id){
    const input_title = document.getElementById("service_title_"+service_id)
    const new_title = input_title.value
    const csrf = document.getElementById("csrf_token")
    if (!new_title || new_title.trim()==""){
        alert("Поле пустое!")
        return
    }
    let response = fetch("/admin/edit_title_service",{
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({id: service_id, title: new_title})
    }).then(response => {
        if (!response.ok){
            return
        }
        input_title.placeholder = new_title
        input_title.value = null
        alert("Название изменено на: "+ new_title)
    })
}


function editDescriptionService(info_id, service_title){
    const textarea_input = document.getElementById("textarea_id_"+info_id)
    const text = textarea_input.value
    const csrf = document.getElementById("csrf_token")
    if (!text || text.trim() ==""){
        alert("Поле пустое!")
        return
    }
    let response = fetch("/admin/edit_info_service",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            info_id: info_id,
            new_description: text
        })
    }).then(response => {
        if (!response.ok){
            return
        }
        alert('Описание услуги: "'+ service_title + ' изменено.')
        textarea_input.placeholder = textarea_input.value
        textarea_input.value = null
    })
}


function editPriceService(service_id, service_title){
    const input_price = document.getElementById("price_service_"+service_id)
    const new_price = input_price.value
    const csrf = document.getElementById("csrf_token")
    if (!new_price || new_price.trim()==""){
        alert("Поле пустое! Введите новую цену!")
        return
    }
    let response = fetch("/admin/edit_price_service",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            service_id: service_id,
            new_price: new_price
        })
    }).then(response => {
        if (!response.ok){
            return
        }
        input_price.placeholder = new_price
        input_price.value = null
        alert('Цена услуги: "'+ service_title + '" изменена на '+new_price+' руб.')
    })
}


class GetTextAreaNewDescription {
    constructor(service_id){
        this._textarea = document.getElementById("textarea_description_"+service_id)
        this._value = this._textarea.value
    }
    get Value(){
        return this._value
    }
    rmDataTextArea(){
        if (this._value || this._value.trim() == "") this._textarea.value = null;
    }
}


function addNewDescription(service_id, service_title){
    let textarea = new GetTextAreaNewDescription(service_id)
    const new_text = textarea.Value
    const csrf = document.getElementById("csrf_token")
    if (!new_text || new_text.trim()==""){
        alert("Поле пустое!")
        return
    }
    let response = fetch("/admin/add_new_description",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            service_id: service_id,
            description: new_text
        })
    })
    .then(response =>{
        if (!response.ok) return
        textarea.rmDataTextArea()
        return response.json()
    }).then(json => {
        location.reload()
    })
}


function clearNewDescription(service_id){
    let textarea = new GetTextAreaNewDescription(service_id)
    textarea.rmDataTextArea()
}

class CheckboxDescriptions {
    constructor(){
        this._selectorDescriptions = document.querySelectorAll('input[type="checkbox"]:checked')
    }

    checkSelectedCheckbox(){
        if (this._selectorDescriptions.length == 0) return false;
        return true
    }

    get Descriptions_id(){
        if (!this.checkSelectedCheckbox()){
                alert("Нужно выбрать минимум одно описание.")
                return false
            }
        let list_id = []
        for (let descr of this._selectorDescriptions) list_id.push(descr.id)
        return list_id
    }

    clearSelectedCheckbox(){
//    При закрытии окна
        if (this.checkSelectedCheckbox()){
            for (let value of this._selectorDescriptions){
                value.checked = false
            }
        }
    }
}


function rmDescriptions(target){
    const csrf = document.getElementById("csrf_token")

    const descriptions = new CheckboxDescriptions()
    const descriptions_id = descriptions.Descriptions_id
    let description_modal_window = target.closest("div").closest("div [class='modal-content']")
        .querySelector("div [class='input-group']")
        .querySelector("p input[id='"+descriptions_id+"']")
        .closest("div")
    let close_modal_btn = target.closest("div").closest("div [class='modal-content']")
        .querySelector("div [class='modal-header']").querySelector("button")
    let div_textarea = target.closest("div [class='img-services']").querySelector("div [id='"+descriptions_id+"']")
    if (!descriptions_id) return;
    if (!confirm("Удалить описание?")) return;
    let response = fetch("/admin/remove_descriptions",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            descriptions_id: descriptions_id,
        })
    }).then(response => {
        if (!response.ok) {
            alert("Ошибка удаления!")
            close_modal_btn.click()
            return
        }
            div_textarea.remove()
        close_modal_btn.click()
        description_modal_window.remove()
        alert("Описание удалено.")
    })
}


function clearCheckBoxCloseModal(){
    const descriptions = new CheckboxDescriptions()
    descriptions.clearSelectedCheckbox()
}


function rmService(service_id, service_title){
    const csrf = document.getElementById("csrf_token")
    confirm_remove = confirm("Удалить: '"+service_title+"'?")
    if (!confirm_remove) return;
    let response = fetch("/admin/remove_services",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            service_id: service_id
        })
    }).then(response => {
        alert("Услуга: '"+service_title+"' удалена.")
        container_service = document.getElementById("container-"+service_id)
        container_service.remove()
    })
}





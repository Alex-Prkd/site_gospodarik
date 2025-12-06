/*window.onbeforeunload = function() {
    let preview_photo = document.getElementById("preview-photo")
    if (preview_photo.files[0]) return false;
}*/


function showPreview(target){
    let btn = target
    let div_preview = target.closest("div[class='screensaver']")
    let new_photo = target.files[0]
    let textBtn = target.closest("div[class='screensaver']").querySelector("span")
    let removeBtn = target.closest("div[class='screensaver']").querySelector("input[name='removeImg']")
    let btn_save = target.closest("div[class='screensaver']").querySelector("input[name='save']")
    const reader = new FileReader()
    reader.onloadend = function(){
        div_preview.style.backgroundImage = "url("+reader.result+")"
        textBtn.style.display="none"
        removeBtn.type = "button"
        btn_save.type = "button"
    }
    reader.readAsDataURL(new_photo)
}


function removeBackground(target){
    let removeBtn = target
    let divPreview = target.closest("div[class='screensaver']")
    let fileBtn = target.closest("div[class='screensaver']").querySelector("label input")
    let textFileBtn = target.closest("div[class='screensaver']").querySelector("label span")
    let saveBtn = target.closest("div[class='screensaver']").querySelector("input[name='save']")
    removeBtn.type = "hidden"
    divPreview.style.backgroundImage = "url('../static/img/img_contact_page/background/background.JPG')"
    fileBtn.value = null
    fileBtn.type = "file"
    textFileBtn.style.display = null
    saveBtn.type = "hidden"
}


function saveBackground(target){
    const csrf = document.getElementById("csrf_token")
    let btn_save = target
    let inputFile = target.closest("div[class='screensaver']").querySelector("label input")
    let textFileInput = target.closest("div[class='screensaver']").querySelector("span")
    let removeBtn = target.closest("div[class='screensaver']").querySelector("input[name='removeImg']")
    const formData = new FormData()
    formData.append("background", inputFile.files[0])
    fetch("/admin/contacts/new_background", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrf.value
        },
        body: formData
    }).then(response => {
        alert("Сохранено.")
        btn_save.type = "hidden"
        inputFile.value = null
        textFileInput.style.display = ""
        removeBtn.type = "hidden"
    })
}
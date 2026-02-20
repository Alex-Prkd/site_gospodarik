function removePreviewImage(){
    document.getElementById("preview-photo").remove()

    document.getElementById("close-preview-btn").remove()
    let file = document.getElementById("previewReview")
    file.value = ""

    let previewDiv = document.getElementById("preview-div")
    let avatar_container = document.createElement("div")
    avatar_container.className = "avatar-container-inner"
    let div_preview = document.createElement("div")
    div_preview.id = "div-preview"
    div_preview.className = "radius"
    let default_image = document.createElement("i")
    default_image.className = "bi bi-camera position-absolute top-50 start-50 translate-middle pos-camera"

    div_preview.appendChild(default_image)
    avatar_container.appendChild(div_preview)
    previewDiv.appendChild(avatar_container)
}
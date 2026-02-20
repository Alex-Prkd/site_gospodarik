function clearDataNewReview(){
    let name = document.querySelector("input[name='name']")
    let social_link = document.querySelector("input[name='social_link']")
    let review = document.querySelector("textarea[name='review']")
    let photo = document.getElementById("previewReview").files
    name.value = null
    social_link.value = null
    review.value = null
    if (photo.length != 0) removePreviewImage();
}
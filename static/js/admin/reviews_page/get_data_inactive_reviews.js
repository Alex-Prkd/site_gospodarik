const closeModalInactiveReviews = document.getElementById("inactiveReview")
closeModalInactiveReviews.addEventListener("hidden.bs.modal", event => {
    /* очистка отзывов при закрытии модалки*/
    let contentInactiveReview = document.getElementById("contentInactiveReview")
    contentInactiveReview.innerHTML = ""
})


function getInactiveReviews(target){
    let csrf = document.getElementById("csrf")
    let response = fetch("/admin/get_inactive_reviews").then(response=>{
        if (!response.ok) return;
        return response.json()
    }).then(reviews => {
        let data = reviews.inactive_reviews
        if (data.length == 0){
            let container_main = document.getElementById("contentInactiveReview")
            let text_not_found_review = document.createElement("p")
            text_not_found_review.textContent = "Новых отзывов нет."
            container_main.appendChild(text_not_found_review)
        }
        for (let review=0; review < data.length; review++){
            loadReviewsInModalWindow(
                    data[review].id,
                    data[review].nickname,
                    null,
                    data[review].review_text,
                    data[review].social_link
            )
        }
    })
}


function loadReviewsInModalWindow(id, nickname, photo_path, review_text, social_link){
    let container_main = document.getElementById("contentInactiveReview")    /*главный div куда загружаются все отзывы*/
    let container_content = document.createElement("div")
    container_content.className = "container-content"
    let div_social_link
    let div_main = document.createElement("div")
    div_main.style = "margin-bottom: 5%;"
    let div_row = document.createElement("div")
    div_row.className = "row"
    div_row.style = "margin-bottom: 10px; padding-bottom: 10px;"
    let new_div_review = document.createElement("div")

    let div_content = document.createElement("div")

    div_content.className = "col-6"     /*блок текста инфы отзыва*/
    div_content.id = id

    let div_nickname = document.createElement("div")
    tag_p_nickname = document.createElement("p")
    tag_p_nickname.textContent = nickname
    tag_p_nickname.id = "nickname"

    if (typeof social_link !== "undefined"){    /*если есть ссылка на соц. сеть определяем блок с инфой о ней*/
        div_social_link = document.createElement("div")
        tag_p_social_link = document.createElement("p")
        tag_p_social_link.textContent = social_link
        tag_p_social_link.id = "link_social"
    }

    let div_review = document.createElement("div")
    let tag_p_review = document.createElement("p")
    tag_p_review.textContent = review_text
    tag_p_review.className = "review"

    div_nickname.appendChild(tag_p_nickname)

    div_review.appendChild(tag_p_review)

    if (typeof div_social_link !== "undefined"){    /*если блок с соц сетью определён добавляем его*/
        div_social_link.appendChild(tag_p_social_link)
        div_content.appendChild(div_nickname).appendChild(div_social_link).appendChild(div_review)
    }
    else{   /*без соц сети*/
        div_content.appendChild(div_nickname).appendChild(div_review)
    }
    /*------------------*/
    let div_btn = document.createElement("div")

    let btn_save_review = document.createElement("input")
    btn_save_review.type = "button"
    btn_save_review.className = "btn btn-success"
    btn_save_review.value = "Сохранить"
    btn_save_review.addEventListener("click",function() {saveInactiveReview(this)} )

    let btn_remove_review = document.createElement("input")
    btn_remove_review.type = "button"
    btn_remove_review.className = "btn btn-danger"
    btn_remove_review.value = "Удалить"
    btn_remove_review.addEventListener("click", function() {removeInactiveReview(this)})

    div_btn.appendChild(btn_save_review)
    div_btn.appendChild(btn_remove_review)
    div_content.appendChild(div_btn)
    /*------------------*/


    let div_photo_client = document.createElement("div")
    div_photo_client.className = "col-6"

    let position_relative = document.createElement("div")
    position_relative.style = "height: 100%;"

    let position_absolute = document.createElement("div")
    position_absolute.className = "position-absolute top-50 start-50 translate-middle avatar-container"

    let div_avatar = document.createElement("div")
    div_avatar.className = "avatar-container-inner"

    let div_radius_avatar = document.createElement("div")
    div_radius_avatar.className = "radius"
    if (photo_path !== null){/*есть фото к отзыву*/
        var img = document.createElement("img")
        img.src = photo_path
    }
    else{/* если фото в отзыве нет, вставляем заглушку*/
        var img = document.createElement("i")
        img.className = "bi bi-camera position-absolute top-50 start-50 translate-middle pos-camera"
    }

    div_photo_client.appendChild(position_relative)
    position_relative.appendChild(position_absolute)
    position_absolute.appendChild(div_avatar)
    div_avatar.appendChild(div_radius_avatar)
    div_radius_avatar.appendChild(img)


    div_row.appendChild(div_content)
    div_row.appendChild(div_photo_client)
    div_main.appendChild(div_row)
    container_content.appendChild(div_main)
    container_main.appendChild(container_content)
}
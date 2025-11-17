function removePhoto(image){
   let csrf = document.getElementById("csrf_token")
   let rm_photo_confirm = confirm("Удалить фото "+ image + "?");
   if (rm_photo_confirm){
        fetch("/admin/remove_photo_main_page/",{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf.value
            },
            body: JSON.stringify({ "image": image})
        }).then(response => {
            if (response.ok){
                alert("Фото удаленно.");
                location.reload();
            }
            else{
                alert("Ошибка удаления.")
            }
        });
   };
};
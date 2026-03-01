// Добавляем фотографии на главную страницу (портфолио)

$('input[type=file]').val(null);
var dt = new DataTransfer();


$('.new-photo input[type=file]').on('change', function(){
	let $files_list = $(this).closest('.input-file').next();
	for(var i = 0; i < this.files.length; i++){
		let file = this.files.item(i);
		dt.items.add(file);
		let reader = new FileReader();
		reader.readAsDataURL(file);
		reader.onloadend = function(){
			let new_file_input = '<div class="input-file-list-item">' +
				'<img class="input-file-list-img" src="' + reader.result + '">' +
				'<span class="input-file-list-name">' + file.name + '</span>' +
				'<a href="#" onclick="removeFilesItem(this); return false;" class="input-file-list-remove">x</a>' +
			'</div>';
			$files_list.append(new_file_input);
		}
	};
	this.files = dt.files;
	btn_save= document.getElementById("submit_save")
	if (this.id == "btn_add_photo"){
	    btn_save.disabled = false
	}
});


function removeFilesItem(target){
	let name = $(target).prev().text();
	let input = $(target).closest('.input-file-row').find('input[type=file]');
	$(target).closest('.input-file-list-item').remove();
	for(let i = 0; i < dt.items.length; i++){
		if(name === dt.items[i].getAsFile().name){
			dt.items.remove(i);
		}
	}
	input[0].files = dt.files;
	btn_save= document.getElementById("submit_save")
	if (input[0].files.length == 0){
	    btn_save.disabled = true
	}
}


function sendPhoto(){
    let csrf = document.getElementById("csrf_token")
    const fileInput = document.getElementById("btn_add_photo");
    let formData = new FormData();
    formData.append("image", fileInput.files[0]);
    fetch("/admin/add_new_photo", {
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value
        },
        body: formData,
        })
};
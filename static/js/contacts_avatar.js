const contact_canvas = document.getElementById('contact-canvas');
const contact_ctx = contact_canvas.getContext('2d');
const contact_img = document.getElementById('contact-image');

contact_img.onload = function(){
    console.log("123")
    contact_ctx.beginPath();
    contact_ctx.arc(
            contact_canvas.width / 2,
            contact_canvas.height / 2,
            160,
            0,
            Math.PI * 2
    );
    contact_ctx.clip();
    let scale = Math.min(
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
};


if (contact_img.complete) contact_img.onload();


function Test(target){
    let file = target.files[0]
    let reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onloadend = function(){
        console.log(file)
        console.log(reader.result)
    contact_img.src = reader.result
    }
    contact_img.onload()
}


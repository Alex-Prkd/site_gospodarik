window.addEventListener("load", function(){
    avatarContactPage()
})


function avatarContactPage(){
    const contact_canvas = document.getElementById('contact-canvas');
    const contact_ctx = contact_canvas.getContext('2d');
    const contact_img = document.getElementById('contact-image');

    let radius = Math.min(contact_canvas.width, contact_canvas.height) / 2;
    contact_ctx.clearRect(0, 0, contact_canvas.width, contact_canvas.height);
    contact_ctx.beginPath();
    contact_ctx.arc(
            contact_canvas.width / 2,
            contact_canvas.height / 2,
            radius,
            0,
            Math.PI * 2
    );
    contact_ctx.clip();
    let scale = Math.max(
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
}



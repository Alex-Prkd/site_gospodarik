// Показать кнопку "Наверх" при скроллинге
window.onscroll = function() {
    var toTopBtn = document.getElementById("toTopBtn");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        toTopBtn.style.display = "block";
    } else {
        toTopBtn.style.display = "none";
    }
};

// Вернуться к началу страницы при нажатии на кнопку
document.getElementById("toTopBtn").addEventListener("click", function() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
});

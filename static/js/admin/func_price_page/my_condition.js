function addNewCondition(target){
    const csrf = document.getElementById("csrf_token")
    let content = target.closest("div[class='modal-content']")
    let condition = content.querySelector("textarea")
    if (condition.value.trim() == ""){
        alert("Введите данные!")
        return
    }
    let response = fetch("/admin/create_my_condition",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            new_condition: condition.value
            })
        }).then(response =>{
            if (!response.ok) return;
            alert("Условие добавлено.")
            location.reload()
        })
}

function cleaningModalCreateMyCondition(target){
    let content = target.closest("div[class='modal-content']")
    let condition = content.querySelector("textarea")
    condition.value = null;
}

function changeMyCondition(target, condition_id){
    const csrf = document.getElementById("csrf_token")
    let content = target.closest("div[class='condition']")
    let new_condition = content.querySelector("textarea")
    if (new_condition.value.trim() == ""){
        alert("Внесите данные!")
        new_condition.value = null
        return
    }
    res = confirm("Изменить '"+new_condition.placeholder+"' на '"+new_condition.value+"'?")
    if (!res){
        new_condition.value = null
        return
        }
    const response = fetch("/admin/change_my_condition", {
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            text: new_condition.value,
            condition_id: condition_id
            })
        }).then(response => {
            if (!response.ok) return;
            alert("Сохранено.")
            new_condition.placeholder = new_condition.value
            new_condition.value = null
        })
}


function removeMyCondition(target, condition_id){
    const csrf = document.getElementById("csrf_token")
    let content = target.closest("div[class='condition']")
    res = confirm("Удалить?")

    if (!res) return;
    const response = fetch("/admin/remove_my_condition", {
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            condition_id: condition_id
            })
        }).then(response => {
            if (!response.ok) return;
            content.remove()
            alert("Удалено.")
        })
}


function ChangeConditionVideo(target, id){
    const csrf = document.getElementById("csrf_token")
    let content = target.closest("div[class='ConditionVideo']")
    let text = content.querySelector("textarea")
    if (text.value.trim() == ""){
        alert("Поле пустое!")
        return
    }
    const response = fetch("/admin/change_condition_video", {
        method: "POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
                id: id,
                text: text.value
            })
        }).then(response => {
            if (!response.ok) return;
            text.placeholder = text.value
            text.value = null
        })

}
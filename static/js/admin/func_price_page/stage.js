function removeConditionStage(condition_id, target){
    csrf = document.getElementById("csrf_token")
    const div_stage = target.closest("div[id='div-stage']")
    const conditions = div_stage.querySelectorAll("li.info > textarea")
    if (conditions.length < 2){
        alert("В этапе до съёмки необходимо минимум 1 описание!")
        return
    }
    rm_condition = target.closest("li").querySelector("textarea[id='"+condition_id+"']")
    confirm_remove = confirm("Удалить: "+rm_condition.placeholder+"?")
    if (!confirm_remove) return;
    const response = fetch("/admin/remove_condition",{
    method:"POST",
    headers: {
        "X-CSRFToken":csrf.value,
        "Content-Type": 'application/json'
    },
    body: JSON.stringify({
        condition_id: condition_id
        })
    }).then(response => {
        alert("Условие удалено")
        target.closest("li").remove()
    })
}

function saveChangeStage(stage_id, target){
    csrf = document.getElementById("csrf_token")
    const container_stage = target.closest("div[id='div-stage']")
    const title_stage = container_stage.querySelector("p > input[id='title-stage-"+stage_id+"']")
    const conditions = Array.from(container_stage.querySelectorAll("li.info > textarea"))
        .filter(condition =>condition.value.trim() != "")
    let data = {}
    if (title_stage.value.trim() != "") data["edit_title"] = {id: stage_id, new_title: title_stage.value}
    if (conditions.length > 0){
        data.edit_conditions = []
        for (const condition of conditions){
            data.edit_conditions.push({
                id: condition.id,
                value: condition.value
            })
        }
    }
    if (Object.keys(data).length === 0)
        {
            alert("Введите данные.")
            return
        }
    const response = fetch("/admin/edit_stage",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            data_for_editing: data
            })
        }).then(response => {
            alert("Данные сохранены")
            if (title_stage.value.trim() != ""){
                title_stage.placeholder = title_stage.value
                title_stage.value = null
            }
            for (const condition of conditions){
                    condition.placeholder = condition.value
                    condition.value = null
                }
        })
}

function createStage(){
    const csrf = document.getElementById("csrf_token")
    const title = document.getElementById("titleStage")
    const all_textarea_condition = document.querySelectorAll("textarea.condition")
    let text_condition = new Array()
    for (const div of all_textarea_condition){
        if (div.value.trim() =="") continue;
        text_condition.push(div.value)
    }
    if (!title.value || title.value.trim() == "" || text_condition.length == 0) {
        alert("Заполните поля!")
        return
    }
    let response = fetch("/admin/create_new_stage_work",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            stage_title: title.value,
            conditions: text_condition
            })
        }).then(response => {
            alert("Этап до съёмки добавлен.")
            const div_stages = $(".container-stages")
            location.reload()
            })
}

function removeStage(stage_id, title, target){
    const csrf = document.getElementById("csrf_token")
    rm_stage_confirm = confirm("Удалить этап работы: "+title+"?")
    if (!rm_stage_confirm) return;
    let response = fetch("/admin/remove_stage",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({stage_id: stage_id})
        })
        div_stage = target.closest("div[id='div-stage']")
        div_stage.remove()
}

function addNewConditionStage(stage_id, target){
    const csrf = document.getElementById("csrf_token")
    const content = target.closest("div[class='modal-content']")
    let new_condition = content.querySelector("textarea")
    if (new_condition.value.trim() == ""){
        alert("Введите данные.")
        return
    }
    let response = fetch("/admin/add_new_condition_stage",{
        method:"POST",
        headers: {
            "X-CSRFToken":csrf.value,
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            stage_id: stage_id,
            text: new_condition.value
            })
        }).then(response =>{
            alert("Условие добавлено.")
            location.reload()
        })

}

function clearNewConditionStage(target){
    const content = target.closest("div[class='modal-content']")
    let new_condition = content.querySelector("textarea")
    new_condition.value = null
}

function addTextareaConditionStage(){
    const div_textarea = $(".container-textarea")
    new_textarea = '<div class="col-12 d-flex justify-content-between align-items-center mb-2">'+
        '<textarea class="col-10 condition" rows="5" placeholder="Условие" name="added-condition"></textarea>'+
        '<button class="btn-close col-2" href="#" onclick="removeTextareaConditionStage(this)"; return false;">'+
    '</div>'
    div_textarea.append(new_textarea)

}

function removeTextareaConditionStage(target){
    let div = target.closest("div")
    div.remove()
}

function cleaningModalCreateStage(){
    let title = document.getElementById("titleStage")
    title.value = null
    let all_textarea_condition = document.querySelectorAll("textarea.condition")
    for (const div of all_textarea_condition){
        if (div.name == "condition") {
            div.value = null;
            continue
        }
        div.closest("div").remove()
    }
}



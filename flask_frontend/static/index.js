function open_task(e, force=null){
    if (force == null){
        force = !e.parentElement.classList.contains('show')
    }
    e.parentElement.classList.toggle('show', force);
}
function open_event(e, force=null){
    if (force == null){
        force = !e.parentElement.classList.contains('show')
    }
    e.parentElement.classList.toggle('show', force);
}
function toggle_popup(){
    document.getElementsByClassName('popup')[0].classList.toggle('show')
}
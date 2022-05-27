var login_btn = document.querySelector('.login_btn')
var rigister_btn = document.querySelector('.register_btn')


var choose_log_or_reg = document.querySelector('.choose_log_or_reg')
var section_login = document.querySelector('.login')
var section_registration = document.querySelector('.registration')
login_btn.onclick = function() {
    choose_log_or_reg.style.display = "none"
    section_login.style.display = "block"

}

rigister_btn.onclick = function() {
    choose_log_or_reg.style.display = "none"
    section_registration.style.display = "block"
}

var registration_response = document.querySelector('.registration_response').textContent
var login_response = document.querySelector('.login_response').textContent
var room_id = document.querySelector('.room_id')



if (login_response.length > 7 || registration_response.length > 11) {
    if (login_response.slice(0, 7) === "Welcome" ||  registration_response.slice(0, 12) === "Registration") {
        choose_log_or_reg.style.display = "none"
        section_registration.style.display = "none"
        section_login.style.display = "none"
        room_id.style.display = "block"
    }
}

var room_entry = document.querySelector('.room_entry')
var room_entry_status = document.querySelector('.room_entry_status').textContent
if (room_entry_status) {
    choose_log_or_reg.style.display = "none"
    section_registration.style.display = "none"
    section_login.style.display = "none"
    room_id.style.display = "block"
}

// room_entry.onclick = function() {
//     if (room_entry_status) {
//         console.log("in status")
//         choose_log_or_reg.style.display = "none"
//         room_id.style.display = "none"
//     } else {
//         choose_log_or_reg.style.display = "none"
//         section_registration.style.display = "none"
//         section_login.style.display = "none"
//         room_id.style.display = "block"
//     }
// }

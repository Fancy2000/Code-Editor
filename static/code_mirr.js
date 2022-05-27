var editor = CodeMirror.fromTextArea(document.getElementById('editor'), {
    mode: 'python',
    theme: 'monokai',
    lineNumbers: true,
    autoCloseBrackets: true,
    autoCloseTags: true,
})

console.log("NEW JS")
var read_btn= document.querySelector('.read_b')
var write_btn = document.querySelector('.write_b')

if (document.querySelector('.my_role').textContent === "reader") {
    editor.setOption("readOnly", true)
    read_btn.style.backgroundColor = "#4CAF50"
    write_btn.style.backgroundColor = "white"
}

read_btn.onclick = function() {
    var role = document.querySelector('.my_role').textContent
    if (role === "writer") {
        document.querySelector('.my_role').textContent = "reader"
        editor.setOption("readOnly", true)
        read_btn.style.backgroundColor = "#4CAF50"
        write_btn.style.backgroundColor = "white"
    }
}

write_btn.onclick = function() {
    var role = document.querySelector('.my_role').textContent
    if (role === "reader but can be writer") {
        document.querySelector('.my_role').textContent = "writer"
        editor.setOption("readOnly", false)
        read_btn.style.backgroundColor = "white"
        write_btn.style.backgroundColor = "#4CAF50"
    }

}

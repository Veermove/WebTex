let codeEditor = ace.edit("text_box")
let editorLib = {
    init() {
        // Set theme
        codeEditor.setTheme("ace/theme/dracula");
        // Set language
        codeEditor.session.setMode("ace/mode/latex")
        // Set options
        codeEditor.setOptions({
            fontFamily: "Courier New",
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
        })
    }
}

editorLib.init();
var pdfHandler = document.getElementById('pdf_view')


const uploadURL = 'http://localhost:8080/submit'
const refreshURL = 'http://localhost:8080/pdf'

document.getElementById("Button").onclick = function(){
    alert("CLICK");
    var textToWrite = codeEditor.getValue();
    // var textAsBlob = new Blob([ textToWrite ], { type: 'text/plain' });
    var formData = new FormData()
    formData.append("text", textToWrite)

    fetch(uploadURL, {
        method: "POST",
        body: formData
    })
    .then(resp => {
        console.log(resp)
        pdfHandler.src = pdfHandler.src
    })
    .catch(err => alert(err));
};

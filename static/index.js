const uploadURL = 'http://localhost:8080/submit'
const refreshURL = 'http://localhost:8080/pdf'
const defaultTextURL = 'http://localhost:8080/def_text'
const setPresetURL = 'http://localhost:8080/starter?'

document.getElementById("render").onclick = recompile
document.getElementById("but_es").onclick = setPresetES
document.getElementById("but_emp").onclick = setPresetEMP
var pdfHandler = document.getElementById('pdf_view')


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


function recompile() {
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

function setPresetES() {
    setPreset("essay")
}

function setPresetEMP() {
    setPreset("empty")
}

function setPreset(sample) {
    console.log(sample)
    fetch(setPresetURL + new URLSearchParams({ preset: sample }), {
        method: "GET"
    })
    .then(resp => {
        resp.text().then(tex => {
            codeEditor.setValue(tex)
        })
        .catch(err => {
            console.log(err)
        })
    })
}

let onLoad = () => {
    fetch(defaultTextURL, {
        method: "GET"
    })
    .then(resp => {
        resp.text().then(tex => {
            codeEditor.setValue(tex)
        })
        .catch(err => {
            console.log(err)
        })
    })
};
onLoad()

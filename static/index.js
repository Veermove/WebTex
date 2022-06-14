const uploadURL = 'http://localhost:8080/submit'
const refreshURL = 'http://localhost:8080/pdf'

var pdfHandler = document.getElementById('pdf_view')

document.getElementById("Button").onclick = function(){
    alert("CLICK");
    var textToWrite = document.getElementById('text_field').value;
    var textAsBlob = new Blob([ textToWrite ], { type: 'text/plain' });
    var formData = new FormData()
    formData.append("text", textToWrite)
    fetch(uploadURL, {
        method: "POST",
        body: formData
    })
    .then(resp => {
        console.log(resp)
    })
    .catch(err => alert(err));
    pdfHandler.src = pdfHandler.src
};

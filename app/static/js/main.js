function copyTextToClip() {
  var copyText = document.getElementById("formattedText").innerText;
  navigator.clipboard.writeText(copyText);

  alert("Copied text to clipboard!");
}

function downloadFile(){
  text = document.getElementById("formattedText").innerText;
  // filename = document.getElementById("filename").innerText;
  filename = document.getElementById("filename").value;
  var link = document.createElement('a');

  link.setAttribute('download', filename);
  link.href = makeTextFile(text);
  document.body.appendChild(link);

  // wait for the link to be added to the document
  window.requestAnimationFrame(function () {
    var event = new MouseEvent('click');
    link.dispatchEvent(event);
    document.body.removeChild(link);
  });
}

function makeTextFile (text) {
  var data = new Blob([text], {type: 'text/plain'});
  var textFile = null
  if (textFile !== null) {
    window.URL.revokeObjectURL(textFile);
  }
  textFile = window.URL.createObjectURL(data);
  return textFile;
};
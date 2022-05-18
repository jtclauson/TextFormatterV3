function copyTextToClip() {
  var copyText = document.getElementById("formattedText").innerText;
  navigator.clipboard.writeText(copyText);

  alert("Copied text to clipboard!");
}

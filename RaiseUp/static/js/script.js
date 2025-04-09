

labels = document.querySelectorAll('label');
for (var i = 0; i < labels.length; i++) {
    labels[i].classList.add('form-label');
}

inputs = document.querySelectorAll('input');
for (var i = 0; i < inputs.length; i++) {
    inputs[i].classList.add('form-control');
}

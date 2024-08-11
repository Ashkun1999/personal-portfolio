const errorName = document.getElementById('error-name');
const errorEmail = document.getElementById('error-email');
const errorMessage = document.getElementById('error-message');

document.getElementById('btn-send').addEventListener('click', function(e) {
  e.preventDefault();
  const form = document.forms['contact-form'];
  const name = form['name'].value;
  const email = form['email'].value;
  const message = form['message'].value;

  errorName.innerText = '';
  errorEmail.innerText = '';
  errorMessage.innerText = '';

  if (!name) {
    errorName.innerText = 'Name is required';
  }

  if (!email) {
    errorEmail.innerText = 'Email is required';
  }

  if (!message) {
    errorMessage.innerText = 'Message is required';
  }

  if (name && email && message) { 
    form.submit();
  }
});
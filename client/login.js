const domain = 'http://localhost:8000';

let form = document.getElementById('login-form');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = {
    username: form.username.value,
    password: form.password.value,
  };

  fetch(`${domain}/api/users/token/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.access) {
        localStorage.setItem('token', data.access);
        window.location = 'http://127.0.0.1:5500/client/projects-list.html';
      } else {
        alert('Wrong credentials');
      }
    });
});

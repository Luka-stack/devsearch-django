let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');

if (searchForm) {
  for (let i = 0; pageLinks.length > i; ++i) {
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault();

      let page = this.dataset.page;
      searchForm.innerHTML += `<input value=${page} name="page" hidden />`;
      searchForm.submit();
    });
  }
}

const tags = document.getElementsByClassName('project-tag');

for (let i = 0; i < tags.length; ++i) {
  tags[i].addEventListener('click', (event) => {
    const tagId = event.target.dataset.tag;
    const projectId = event.target.dataset.project;

    fetch('http://localhost:8000/api/remove-tag/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ project: projectId, tags: tagId }),
    })
      .then((response) => response.json())
      .then((data) => {
        event.target.remove();
      });
  });
}

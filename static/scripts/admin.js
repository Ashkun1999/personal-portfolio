const deleteButtons = document.querySelectorAll('button.action.delete');
deleteButtons.forEach(button => {
  button.addEventListener('click', async (e) => {
    const projectId = e.target.getAttribute('data-project-id');
    const response = await fetch(`/projects/${projectId}`, {
      method: 'DELETE',
    });
    if (response.ok) {
      window.location.reload();
    }
  });
});

const editButtons = document.querySelectorAll('button.action.edit');
const editDialog = document.getElementById('editProjectDialog');
const editForm = document.getElementById('editProjectForm');
const cancelEditButton = document.getElementById('cancelEdit');

editButtons.forEach(button => {
  button.addEventListener('click', (e) => {
    const node = e.target.tagName !== 'BUTTON' ? e.target.parentNode : e.target;
    const projectId = node.getAttribute('data-project-id');
    const projectTitle = node.getAttribute('data-project-title');
    const projectDescription = node.getAttribute('data-project-description');
    const projectIcon = node.getAttribute('data-project-icon');
    const projectLink = node.getAttribute('data-project-link');

    document.getElementById('editProjectId').value = projectId;
    document.getElementById('editTitle').value = projectTitle;
    document.getElementById('editDescription').value = projectDescription;
    document.getElementById('editIcon').value = projectIcon;
    document.getElementById('editLink').value = projectLink;

    editDialog.showModal();
  });
});

cancelEditButton.addEventListener('click', () => {
  editDialog.close();
});

editForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(editForm);
  const projectId = formData.get('id');
  const jsonData = {
    title: formData.get('title'),
    description: formData.get('description'),
    icon: formData.get('icon'),
    link: formData.get('link')
  };
  const response = await fetch(`/projects/${projectId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonData)
  });
  if (response.ok) {
    editDialog.close();
    window.location.reload();
  }
});

regPage = document.querySelector(".regPage");



function Goida(){
    regPage.style.visibility = "hidden";
}

function Goida2(){
    regPage.style.visibility = "visible";
}
function confirmDelete(postId) {
    if (confirm("Вы уверены, что хотите удалить этот пост?")) {
        // Отправляем AJAX-запрос на сервер для удаления поста
        fetch(`/delete_post/${postId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': window.csrftoken,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                // Удаляем пост из DOM, если удаление прошло успешно
                document.getElementById(`post-${postId}`).remove();
            } else {
                alert('Ошибка при удалении поста.');
            }
        })
        .catch(error => {
            location.reload();
        });
    }
}
const API = window.location.origin;

function getToken() {
    return localStorage.getItem('token');
}

async function loadTodos() {

    const res = await fetch(
        `${API}/todos`,
        {
            headers: {
                Authorization: `Bearer ${getToken()}`
            }
        }
    );

    const todos = await res.json();
    console.log("TODOS:", todos);

    const list = document.getElementById("todolist");

    list.innerHTML = "";

    todos.forEach(todo => {

        const card = document.createElement("div");

        card.className =
            "card p-3 mb-2 d-flex flex-row justify-content-between align-items-center";

        const title = document.createElement("span");

        title.innerText = todo.title;

        if (todo.completed) {
            title.style.textDecoration = "line-through";
            title.style.opacity = "0.6";
        }

        const actions = document.createElement("div");

        // COMPLETE BUTTON
        const completeBtn = document.createElement("button");

        completeBtn.className = todo.completed
            ? "btn btn-success btn-sm"
            : "btn btn-outline-success btn-sm";

        completeBtn.innerText = todo.completed
            ? "Completed"
            : "Mark Done";

        completeBtn.onclick = () => toggleTodo(todo);

        // EDIT BUTTON
        const editBtn = document.createElement("button");

        editBtn.className =
            "btn btn-primary btn-sm ms-2";

        editBtn.innerText = "Edit";

        editBtn.onclick = () => updateTodo(todo);

        // DELETE BUTTON
        const delBtn = document.createElement("button");

        delBtn.className =
            "btn btn-danger btn-sm ms-2";

        delBtn.innerText = "Delete";

        delBtn.onclick = () => deleteTodo(todo.id);

        actions.appendChild(completeBtn);
        actions.appendChild(editBtn);
        actions.appendChild(delBtn);

        card.appendChild(title);
        card.appendChild(actions);

        list.appendChild(card);
    });
}
async function addTodo() {

    const input =
        document.getElementById("todoInput");

    const title = input.value.trim();

    if (!title) {
        return;
    }

    const res = await fetch(
        `${API}/todos`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${getToken()}`
            },
            body: JSON.stringify({
                title: title,
                completed: false
            })
        }
    );

    if (!res.ok) {
        alert("Failed to create todo");
        return;
    }

    input.value = "";

    loadTodos();
}
async function toggleTodo(todo) {

    await fetch(
        `${API}/todos/${todo.id}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${getToken()}`
            },
            body: JSON.stringify({
                title: todo.title,
                completed: !todo.completed
            })
        }
    );

    loadTodos();
}
async function updateTodo(todo) {

    const newTitle = prompt(
        "Edit todo if you want :",
        todo.title
    );

    if (!newTitle) {
        return;
    }

    await fetch(
        `${API}/todos/${todo.id}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${getToken()}`
            },
            body: JSON.stringify({
                title: newTitle,
                completed: todo.completed
            })
        }
    );

    loadTodos();
}
async function deleteTodo(id) {

    const confirmed =
        confirm("Delete this todo if you want ?");

    if (!confirmed) {
        return;
    }

    await fetch(
        `${API}/todos/${id}`,
        {
            method: "DELETE",
            headers: {
                Authorization: `Bearer ${getToken()}`
            }
        }
    );

    loadTodos();
}
loadTodos();

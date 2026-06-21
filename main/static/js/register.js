async function registerUser() {

    const username =
        document.getElementById('username').value;

    const email =
        document.getElementById('email').value;

    const password =
        document.getElementById("password").value;

    const confirm_password =
        document.getElementById('confirm_password').value;

    const message =
        document.getElementById('message');

    if (!username || !email || !password || !confirm_password) {
        message.className = "text-danger text-center mt-3";
        message.innerText = "All fields are required!";
        return;
    }

    if (password !== confirm_password) {
        message.className = "text-danger text-center mt-3";
        message.innerText = "Passwords don't match!!";
        return;
    }

    try {
        const res = await fetch("/auth/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                email,
                password
            })
        });

        const data = await res.json(); 

        if (!res.ok) {
            message.className = "text-danger text-center mt-3";

            message.innerText =
                data.detail?.[0]?.msg || data.detail || "Registration failed";

            return;
        }

        message.className = "text-success text-center mt-3";
        message.innerText = "Account created successfully";

        setTimeout(() => {
            window.location.href = "/";
        }, 1500);

    } catch (error) {
        message.className = "text-danger text-center mt-3";
        message.innerText = "Something went wrong!!";
    }
}
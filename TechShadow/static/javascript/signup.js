// submit user form

document.addEventListener("DOMContentLoaded", ()=>{
    const user_form = document.getElementById("signup")
    user_form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const form = event.target;
        const data = {
            first_name: form.firstname.value,
            last_name: form.lastname.value,
            username: form.username.value,
            password: form.password.value,
            email: form.email.value,
            field: form.field.value,
            is_mentor: false,
            is_shadower: false
        }
        try{
            const response = await fetch("/user", {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            if (!response.ok) throw new Error ("Error adding new user");
            user_form.reset()
        }catch(e) {
            alert(`There was an error submitting this form: ${e.message}`);
            console.log(e)
        }
    });
});

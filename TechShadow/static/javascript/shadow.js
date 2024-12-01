// submit shadow form

document.addEventListener("DOMContentLoaded", ()=>{
    const shadow_form = document.getElementById("shadow-form")
    shadow_form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const form = event.target;
        const data = {
            position: form.position.value,
            job_description: form.description.value,
            is_remote: false,
            is_in_person: true,
            status: "open",
            required_skills: form.skills.value,
            location: form.location.value
        }
        try {
            const response = await fetch("/shadow", {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            if(!response.ok) throw new Error("error adding new shadow");
            shadow_form.reset()
            window.location.href = "/shadows";
        } catch(e) {
            alert(`There was an error submitting this form: ${e.message}`);
            console.error(e)
        }
    });
});

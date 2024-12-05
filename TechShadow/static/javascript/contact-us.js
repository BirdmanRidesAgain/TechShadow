// submit contact form
document.addEventListener("DOMContentLoaded", ()=>{
    const contact_form = document.getElementById("contact-form")
    contact_form.addEventListener("submit", async (event)=>{
        event.preventDefault();
        const form = event.target;
        const data = {
            name: form.name.value,
            email: form.email.value,
            message_content: form.message.value
        }
        try{
            const response = await fetch("/message", {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            if (!response.ok) throw new Error("Error posting message");
            contact_form.reset()
        }catch(e){
            alert(`There was an error submitting this form: ${e.message}`)
            console.error(e)
        }
    });
});

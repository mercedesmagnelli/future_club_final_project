     document.getElementById("formprincipal").addEventListener("submit", (e) => {
            e.preventDefault()
       
        const form = document.getElementById("formprincipal");
        const username = form.name.value;
        const password = form.email.value;

        const backendResponse = mandarDatosAlBack(username, password)

        
        })

        const mandarDatosAlBack = async (name, email) => {
        // Se arma el body en formato JSON (igual que en postman)
        const body = {
           name,
           email
        }
        // Se ejecuta la request
        const backResponse = await fetch('http://127.0.0.1:5000/predict', {
            headers: {
                "Content-Type": "application/json"
            },
            method: "POST",
            body: JSON.stringify(body)
        })
        // Retornamos la respuesta del backend
        return await backResponse.json()
    }
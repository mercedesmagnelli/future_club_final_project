document.getElementById("formprincipal").addEventListener("submit", (e) => {
    e.preventDefault()

    rearmarFrontend();
})

const rearmarFrontend = async () => {
    const form = document.getElementById("formprincipal");
    const name = form.name.value;
    const email = form.email.value;

    const backendResponse = await mandarDatosAlBack(name, email)

    const p = document.getElementById("p-mensaje-resultado")
    p.innerText = `Las probabilidades de tener un ACV es de ${backendResponse.key}`;
}

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
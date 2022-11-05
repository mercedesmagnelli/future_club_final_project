document.getElementById("survey-form").addEventListener("submit", (e) => {
  e.preventDefault()
  procesarYMostrar();
})

const procesarYMostrar = async () => {
  const backendResponse = await postToAPI();
  console.log(backendResponse.key);
  showPredictionResponse(backendResponse);
}

const postToAPI = async () => {
  // Se arma el body en formato JSON (igual que en postman)

  const formulario = document.getElementById('survey-form')
  const body = {
    "gender": formulario.question_1.value,
    'age': formulario.question_8.value,
    'hypertension': formulario.question_2.value,
    'heart': formulario.question_3.value,
    'married': formulario.question_4.value,
    'work': formulario.question_5.value,
    'residence': formulario.question_6.value,
    'glucose': formulario.question_7.value,
    'height': formulario.question_9_height.value,
    'weight': formulario.question_9_weight.value,
    'smokes': formulario.question_10.value
  }
  console.log(body)
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

function showPredictionResponse({ key }) {

  const formulario = document.getElementById('survey-form')
  const respuesta = document.getElementById('response')
  formulario.classList.add('hidden');
  respuesta.classList.remove('hidden');
  textoAMostrar = document.getElementById('textResponse')
  if (key === 0) {
    textoAMostrar.innerText = 'No pertenecés a un grupo de riesgo. \n Esta breve encuesta no reemplaza la opinión personal de un médico.'

  } else {
    textoAMostrar.innerText = ' Según lo ingresado, pertenecés a un grupo de riesgo. Esta breve encuesta no reemplaza la opinión personal de un médico.'

  }

}




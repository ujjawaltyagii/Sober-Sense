const input = document.createElement('input')
const submit = document.getElementById('submit-image')
const phrase = document.getElementById('phrase-container').innerText

input.type = 'file'
input.accept = 'image/*'
let selectedFile = null
input.onchange = async (e) => {
  selectedFile = e.target.files[0]
  uploadImage(selectedFile)
  
}

async function uploadImage(selectedFile){
  const formData = new FormData()
  formData.append('image', selectedFile)

  console.log(formData)

  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/upload_image')
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log('success image')
    } else {
      console.log('error err')
    }
  }
  await xhr.send(formData)
}

submit.addEventListener('click', () => {
  console.log('click')
  input.click()
})

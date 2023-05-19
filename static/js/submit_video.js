const input = document.createElement('input')
const submit = document.getElementById('submit-video')
const phrase = document.getElementById('phrase-container').innerText

input.type = 'file'
input.accept = 'video/*'
let selectedFile = null
input.onchange = async (e) => {
  selectedFile = e.target.files[0]

  const formData = new FormData()
  formData.append('video', selectedFile)
  formData.append('phrase', phrase)

  console.log(formData)

  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/upload_video')
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log('success')
    } else {
      console.log('error')
    }
  }
  await xhr.send(formData)
}

submit.addEventListener('click', () => {
  console.log('click')
  input.click()
})

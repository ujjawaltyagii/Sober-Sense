const input = document.createElement('input')
const submit = document.getElementById('submit-video')
const phrase = document.getElementById('phrase-container').innerText

input.type = 'file'
input.accept = 'video/*'
let selectedFile = null
input.onchange = (e) => {
  selectedFile = e.target.files[0]

  const formData = new FormData()
  formData.append('video', selectedFile)
  formData.append('phrase', phrase)

  console.log(formData)

  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/submit', true)
  xhr.onload = () => {
    if (xhr.status === 200) {
      path = xhr.responseText
      location.href = path
      console.log('success')
    } else {
      console.log('error')
    }
  }
  xhr.send(formData)
}

submit.addEventListener('click', () => {
  console.log('click')
  input.click()
})

const input = document.createElement('input')
const submit = document.getElementById('submit-image')

input.type = 'file'
input.accept = 'image/*'
let selectedFile = null
input.onchange = (e) => {
  selectedFile = e.target.files[0]

  const formData = new FormData()
  formData.append('image', selectedFile)

  console.log(formData)

  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/submit_image', true)
  xhr.onload = (e) => {
    if (xhr.status === 200) {
      path = xhr.responseText
      location.href = path
    } else {
      console.log('error: ', e)
    }
  }
  xhr.send(formData)
}

submit.addEventListener('click', () => {
  console.log('click')
  input.click()
})

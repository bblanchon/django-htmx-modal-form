const toastTemplate = document.querySelector("[data-toast-template]")
const toastContainer = document.querySelector("[data-toast-container]")

function createToast(message) {
  const element = toastTemplate.cloneNode(true)
  delete element.dataset.toastTemplate
  toastContainer.appendChild(element)
  element.className += " " + message.tags
  element.querySelector("[data-toast-body]").innerText = message.message

  const toast = new bootstrap.Toast(element, { delay: 2000 })
  toast.show()
}

htmx.on("messages", (e) => {
  e.detail.value.forEach(createToast)
})

const toastElements = document.querySelectorAll(
  ".toast:not([data-toast-template])"
)
for (const element of toastElements) {
  const toast = new bootstrap.Toast(element, { delay: 2000 })
  toast.show()
}

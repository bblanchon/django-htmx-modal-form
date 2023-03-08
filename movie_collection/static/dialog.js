; (function () {
  const modal = new bootstrap.Modal(document.getElementById("modal"))

  htmx.on("htmx:afterSwap", (e) => {
    // Response targeting #dialog => show the modal
    if (e.detail.target.id == "dialog") {
      modal.show()
    }
  })

  htmx.on("closeModal", (e) => {
    modal.hide()
  })

  // Remove dialog content after hiding
  htmx.on("hidden.bs.modal", () => {
    document.getElementById("dialog").innerHTML = ""
  })
})()

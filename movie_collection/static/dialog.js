;(function () {
  const modal = new bootstrap.Modal(document.getElementById("modal"))

  htmx.on("htmx:afterSwap", function (e) {
    // Response targeting #dialog => show the modal
    if (e.detail.target.id == "dialog") {
      modal.show()
    }
  })

  htmx.on("htmx:beforeSwap", (e) => {
    console.log("htmx:beforeSwap", e)
    // Empty response targeting #dialog => hide the modal
    if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
      modal.hide()
    }
  })

  // Remove dialog content after hiding
  htmx.on("hidden.bs.modal", () => {
    document.getElementById("dialog").innerHTML = ""
  })
})()

;(function () {
  const toastOptions = { delay: 2000 }

  htmx.onLoad(() => {
    htmx.findAll(".toast").forEach((element) => {
      let toast = bootstrap.Toast.getInstance(element)

      // Remove hidden toasts (optional)
      if (toast && !toast.isShown()) {
        toast.dispose()
        element.remove()
      }

      // Show new ones
      if (!toast) {
        const toast = new bootstrap.Toast(element, toastOptions)
        toast.show()
      }
    })
  })
})()

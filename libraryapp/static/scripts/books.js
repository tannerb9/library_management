const infoDialog = document.querySelector(".infoDialog");
const message = document.querySelector(".infoDialog__message");
const closeDialog = document.querySelector(".closeDialog");

document.querySelector(".books").addEventListener("click", (evt) => {
  if (evt.target.id.startsWith("details")) {
    const id = evt.target.id.split("--")[1];
    message.innerText = `You have selected book ${id}`;
    infoDialog.show();
  }
});

closeDialog.addEventListener("click", (e) => infoDialog.close());

window.addEventListener("keyup", (e) => {
  if (e.keyCode === 27) {
    infoDialog.close();
  }
});

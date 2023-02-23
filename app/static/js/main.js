let currentBox = null;
let isAnimating = false;

const boxes = document.querySelectorAll('.box');

boxes.forEach((box) => {
  box.addEventListener('click', () => {
    let be_large_inter = false;
    if (box !== currentBox) {
      console.log('Se hizo clic en la caja');
      if (!currentBox){
        box.classList.add('large');
      }
      else {
        be_large_inter = true;
      }
      document.body.classList.add('no-hover');
      if (currentBox) {
        currentBox.classList.remove('large');
      }
      if (be_large_inter){
        setTimeout(() => {
            box.classList.add('large');
          }, 300);
        be_large = false;
      }
      currentBox = box;
    }
  });
});

window.addEventListener('click', (event) => {
  if (currentBox && !currentBox.contains(event.target)) {
    console.log('Se hizo clic fuera de la caja');
    currentBox.classList.remove('large');
    document.body.classList.remove('no-hover');
    currentBox = null;
  }
});

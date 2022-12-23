function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  } 


const text = 'The #1 Feedback Hub';
const typewriter = document.getElementById('typewriter');

let i = 0;

function type() {
  if (i < text.length) {
    typewriter.innerHTML += text.charAt(i);
    i++;
    setTimeout(type, 200);
  }
}
// JavaScript
const btn = document.getElementById('btn-get-started');

type();


const quoteContainer = document.querySelector('.quote-container');
const quote = document.querySelector('.quote');

function animate() {
  quote.classList.add('animate');
}

animate()


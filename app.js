/ Flashcards Data
const flashcards = [
  { word: "manzana", translation: "apple" },
  { word: "libro", translation: "book" },
  { word: "gato", translation: "cat" }
];

let currentFlashcard = 0;

function nextFlashcard() {
  currentFlashcard = (currentFlashcard + 1) % flashcards.length;
  document.getElementById("word").textContent = flashcards[currentFlashcard].word;
  document.getElementById("translation").textContent = flashcards[currentFlashcard].translation;
}

// Quiz Data
const quizData = {
  question: "Translate 'cat' to Spanish",
  options: ["perro", "libro", "gato", "pluma"],
  answer: "gato"
};

function loadQuiz() {
  document.getElementById("quiz-question").textContent = quizData.question;
  const optionsContainer = document.getElementById("quiz-options");
  optionsContainer.innerHTML = "";

  quizData.options.forEach(option => {
    const btn = document.createElement("button");
    btn.textContent = option;
    btn.onclick = () => {
      const result = option === quizData.answer ? "Correct!" : "Try again.";
      document.getElementById("quiz-result").textContent = result;
      if (result === "Correct!") {
        document.getElementById("last-score").textContent = 1;
        document.getElementById("lessons-completed").textContent = 1;
      }
    };
    optionsContainer.appendChild(btn);
  });
}

// Navigation Tabs
function showSection(id) {
  document.querySelectorAll(".section").forEach(section => {
    section.classList.add("hidden");
  });
  document.getElementById(id).classList.remove("hidden");

  if (id === "quiz") {
    loadQuiz();
  }
}

window.onload = () => {
  nextFlashcard(); // Load first flashcard
};

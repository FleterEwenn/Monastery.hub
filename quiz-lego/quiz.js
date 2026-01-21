const params = new URLSearchParams(window.location.search);
const theme = params.get("theme");
const imageEl = document.getElementById("question-image");

let index = 0;
let score = 0;
let questions = [];

//  Association thème - questions
if (theme === "anime") {
    questions = animeQuestions;
}

if (theme === "ninjago") {
    questions = ninjagoQuestions;
}

if (theme === "culture") {
    questions = cultureQuestions;
}

if (theme === "info") {
    questions = informatiqueQuestions;
}

if (theme === "cinema") {
    questions = cinemaQuestions;
}

// Sécurité si problème
if (questions.length === 0) {
    document.body.innerHTML = "<h2>Aucune question chargée</h2>";
    throw new Error("Questions non chargées");
}

document.getElementById("quiz-title").textContent = "Quiz " + theme;

const questionEl = document.getElementById("question");
const buttons = document.querySelectorAll(".answer");
const nextBtn = document.getElementById("next");

function loadQuestion() {
    const q = questions[index];

    questionEl.textContent = q.question;

    // 🔹 AFFICHER OU CACHER L’IMAGE
    if (q.image) {
        imageEl.src = q.image;
        imageEl.style.display = "block";
    } else {
        imageEl.style.display = "none";
        imageEl.src = "";
    }

    buttons.forEach((btn, i) => {
        btn.textContent = q.answers[i];
        btn.disabled = false;
        btn.style.backgroundColor = "";

        btn.onclick = () => {
            if (i === q.correct) {
                btn.style.backgroundColor = "green";
                score++;
            } else {
                btn.style.backgroundColor = "red";
                buttons[q.correct].style.backgroundColor = "green";
            }
            buttons.forEach(b => b.disabled = true);
        };
    });
}

nextBtn.onclick = () => {
    index++;
    if (index < questions.length) {
        loadQuestion();
    } else {
        questionEl.textContent = `Quiz terminé ! Score : ${score}/${questions.length}`;
        document.querySelector(".answers").style.display = "none";
        nextBtn.style.display = "none";
    }
};

loadQuestion();

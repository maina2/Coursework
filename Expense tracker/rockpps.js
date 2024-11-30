// DOM Elements
const message = document.getElementById("message");
const playerChoiceDisplay = document.getElementById("player-choice");
const computerChoiceDisplay = document.getElementById("computer-choice");
const resultDisplay = document.getElementById("result");
const playerScoreDisplay = document.getElementById("player-score");
const computerScoreDisplay = document.getElementById("computer-score");

// Game Variables
let playerScore = 0;
let computerScore = 0;

// Choices
const choices = ["Rock", "Paper", "Scissors"];

// Add event listeners to buttons
document.querySelectorAll(".choice-btn").forEach(button => {
  button.addEventListener("click", () => {
    const playerChoice = button.getAttribute("data-choice");
    playRound(playerChoice);
  });
});

// Play a round
function playRound(playerChoice) {
  const computerChoice = getComputerChoice();
  const result = determineWinner(playerChoice, computerChoice);

  // Update the UI
  playerChoiceDisplay.textContent = playerChoice;
  computerChoiceDisplay.textContent = computerChoice;
  resultDisplay.textContent = result;

  // Update Scores
  if (result === "You win!") {
    playerScore++;
  } else if (result === "Computer wins!") {
    computerScore++;
  }

  playerScoreDisplay.textContent = playerScore;
  computerScoreDisplay.textContent = computerScore;
}

// Get a random choice for the computer
function getComputerChoice() {
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

// Determine the winner
function determineWinner(playerChoice, computerChoice) {
  if (playerChoice === computerChoice) {
    return "It's a tie!";
  }

  if (
    (playerChoice === "Rock" && computerChoice === "Scissors") ||
    (playerChoice === "Scissors" && computerChoice === "Paper") ||
    (playerChoice === "Paper" && computerChoice === "Rock")
  ) {
    return "You win!";
  }

  return "Computer wins!";
}

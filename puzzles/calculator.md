---
layout: clue
title: Calculator
permalink: /puzzles/calculator/
robots: noindex
is_puzzle: true
---
<style>
  .calculator {
    display: inline-block;
    background: #000;
    padding: 15px;
    border-radius: 10px;
    font-family: sans-serif;
    width: max-content;
    position: relative;
  }

  .calc-display-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
  }

  .calc-left-display {
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .calc-status {
    font-size: 1em;
    line-height: 1;
    margin: 0;
  }

  .calc-color-previews {
    display: flex;
    gap: 5px;
  }

  .color-circle {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 1px solid #fff;
  }

  .calc-value {
    font-size: 1.5em;
    color: #fff;
    flex-grow: 1;
    text-align: right;
    font-family: monospace;
    min-height: 1.5em;
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }

  .calc-buttons {
    display: grid;
    grid-template-columns: repeat(4, 50px) repeat(2, 50px);
    gap: 5px;
  }

  .calc-buttons button {
    font-size: 1em;
    padding: 12px;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .calc-buttons .operator, .calc-buttons .equals {
    background: #ff9500;
    color: #fff;
  }

  .calc-buttons button:hover {
    filter: brightness(1.2);
  }

  .calc-buttons button:active {
    filter: brightness(0.8);
  }

  .calc-history {
    color: #ccc;
    font-family: monospace;
    font-size: 0.9em;
    margin-top: 10px;
    max-height: 200px;
    overflow-y: auto;
    background: #1a1a1a;
    padding: 5px;
    border-radius: 5px;
  }

  .success-button {
    display: none;
    margin-bottom: 10px;
    padding: 10px 20px;
    font-size: 1em;
    background: #28a745;
    color: #fff !important;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    animation: fadeIn 1s forwards;
    text-decoration: none !important;
  }

  .calculator.disabled .calc-buttons button,
  .calculator.disabled .calc-buttons {
    pointer-events: none;
    opacity: 0.5;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
  }
</style>

<a href="https://example.com" id="successButton" class="success-button" style="pointer-events: auto;">Continue</a>
<div class="calculator" id="calculatorContainer">
  <div class="calc-display-wrapper">
    <div class="calc-left-display">
      <div class="calc-color-previews">
        <div id="targetColor" class="color-circle"></div>
        <div id="currentColor" class="color-circle"></div>
      </div>
      <span id="calcStatus" class="calc-status">❌</span>
    </div>
    <div id="hexCalcDisplay" class="calc-value"> </div>
  </div>
  <div class="calc-buttons">
    <button onclick="appendHex('0')">0</button>
    <button onclick="appendHex('1')">1</button>
    <button onclick="appendHex('2')">2</button>
    <button onclick="appendHex('3')">3</button>
    <button onclick="appendHex('+')" class="operator">+</button>
    <button onclick="appendHex('-')" class="operator">-</button>

    <button onclick="appendHex('4')">4</button>
    <button onclick="appendHex('5')">5</button>
    <button onclick="appendHex('6')">6</button>
    <button onclick="appendHex('7')">7</button>
    <button onclick="appendHex('*')" class="operator">*</button>
    <button onclick="appendHex('/')" class="operator">/</button>

    <button onclick="appendHex('8')">8</button>
    <button onclick="appendHex('9')">9</button>
    <button onclick="appendHex('A')">A</button>
    <button onclick="appendHex('B')">B</button>
    <button onclick="clearHex()" class="operator">C</button>
    <button onclick="calculateHex()" class="equals">=</button>

    <button onclick="appendHex('C')">C</button>
    <button onclick="appendHex('D')">D</button>
    <button onclick="appendHex('E')">E</button>
    <button onclick="appendHex('F')">F</button>
  </div>
  <div id="calcHistory" class="calc-history"></div>
</div>

<script>
  const hexDisplay = document.getElementById('hexCalcDisplay');
  const calcStatus = document.getElementById('calcStatus');
  const targetColor = document.getElementById('targetColor');
  const currentColor = document.getElementById('currentColor');
  const calcHistory = document.getElementById('calcHistory');
  const successButton = document.getElementById('successButton');
  const calculatorContainer = document.getElementById('calculatorContainer');
  const correctResult = "3DEB97"; // Example target
  const correctHexColor = "#" + correctResult.padStart(6, correctResult);

  let history = JSON.parse(localStorage.getItem('calcHistory')) || [];
  renderHistory();

  targetColor.style.background = correctHexColor;

  function appendHex(value) {
    hexDisplay.textContent += value;
    calcStatus.textContent = '❌';
    updateCurrentColor("#" + (hexDisplay.textContent.padStart(6, hexDisplay.textContent)).substring(0, 6));
  }

  function clearHex() {
    hexDisplay.textContent = '';
    calcStatus.textContent = '❌';
    currentColor.style.background = "#000";
  }

  function updateCurrentColor(hex) {
    if (/^#[0-9A-Fa-f]{1,6}$/.test(hex)) {
      currentColor.style.background = hex;
    } else {
      currentColor.style.background = "#000";
    }
  }

  function renderHistory() {
    calcHistory.innerHTML = history.map(entry => `<div>${entry}</div>`).join('');
  }

  function calculateHex() {
    if (hexDisplay.textContent.trim() === '') return;

    try {
      const expressionOriginal = hexDisplay.textContent.trim();
      const expression = expressionOriginal.replace(/([A-Fa-f0-9]+)/g, match => parseInt(match, 16));
      const result = eval(expression);
      const resultHex = result.toString(16).toUpperCase();
      
      if (expressionOriginal !== resultHex) {
        const historyEntry = expressionOriginal + ' = ' + resultHex;
        history.unshift(historyEntry);
      }
      if (history.length > 10) history.pop();
      localStorage.setItem('calcHistory', JSON.stringify(history));
      renderHistory();

      hexDisplay.textContent = resultHex;
      updateCurrentColor("#" + resultHex.padStart(6, resultHex).substring(0, 6));
      calcStatus.textContent = (resultHex === correctResult) ? '✅' : '❌';

      if (resultHex === correctResult) {
        successButton.style.display = 'inline-block';
        calculatorContainer.classList.add('disabled');
      }
    } catch (e) {
      hexDisplay.textContent = 'ERROR';
      calcStatus.textContent = '❌';
      currentColor.style.background = "#000";
    }
  }
</script>

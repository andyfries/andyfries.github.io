---
layout: clue
title: Combo
permalink: /puzzles/lock-combo-answer-page/
robots: noindex
is_puzzle: true
---
<style>
  .rotation {
    font-size: 2em;
    margin: 20px 0;
  }

  .right::before {
    content: '\21BB'; /* Clockwise arrow */
    margin-right: 10px;
    display: inline-block;
    transform: rotate(180deg);
  }

  .left::before {
    content: '\21BA'; /* Counter-clockwise arrow */
    margin-right: 10px;
    display: inline-block;
    transform: rotate(180deg);
  }

  .number {
    font-family: monospace;
    background: #444;
    color: #f0f0f0;
    padding: 2px 5px;
    border-radius: 3px;
  }
</style>

<div class="rotation right">3x right, stop at <span class="number">39</span></div>
<div class="rotation left">left past first number, stop at <span class="number">24</span></div>
<div class="rotation right">right, stop at <span class="number">29</span></div>

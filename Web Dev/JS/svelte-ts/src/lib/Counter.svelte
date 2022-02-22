<script lang="ts">
  let count: number = 0
  const increment = () => {
    count += 1
  }

  let active: boolean = false;
  const changeState = () => {
    if (active === true) {
      active = false
    } else if (active === false) {
      active = true
    }
  }
</script>

<button on:click={increment}>
  Clicks: {count}
</button>

{#if active === true}
  <button on:click={changeState}>Inactive 😞</button>

{:else if active === false}

  <button on:click={changeState}>Active 😄</button>

{/if}

<style>
  button {
    font-family: inherit;
    font-size: inherit;
    padding: 1em 2em;
    color: #ff3e00;
    background-color: rgba(255, 62, 0, 0.1);
    border-radius: 2em;
    border: 2px solid rgba(255, 62, 0, 0);
    outline: none;
    width: 200px;
    font-variant-numeric: tabular-nums;
    cursor: pointer;
  }

  button:focus {
    border: 2px solid #ff3e00;
  }

  button:active {
    background-color: rgba(255, 62, 0, 0.2);
  }
</style>

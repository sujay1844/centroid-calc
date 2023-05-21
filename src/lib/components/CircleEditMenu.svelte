<script lang="ts">
  import { createEventDispatcher } from 'svelte';
	import type { CircleDataType } from "$lib/models";

  const dispatch = createEventDispatcher();
	export let CircleData: CircleDataType;

	function deleteCircle() {
		dispatch('delete', CircleData);
		dispatch('close');
	}

	function closeContextMenu() {
		dispatch('close');
	}

</script>

<div class="context-menu">
	<button on:click={deleteCircle}>🗑</button>
	<button on:click={closeContextMenu}>✕</button>

  <form>
    <label for="radius">Radius:</label>
    <input type="number" id="radius" bind:value={CircleData.radius} />

		<label for="cx">X:</label>
		<input type="number" id="x" bind:value={CircleData.x} />

		<label for="cy">Y:</label>
		<input type="number" id="y" bind:value={CircleData.y} />

		<label for="fillColor">Fill color:</label>
		<input type="text" id="fillColor" bind:value={CircleData.fillColor} />
  </form>
</div>

<style>
  .context-menu {
    position: absolute;
    background-color: white;
    padding: 10px;
    border: 1px solid #ccc;
  }
	button {
		margin: 5px;
	}
</style>

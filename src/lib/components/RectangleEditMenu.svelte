<script lang="ts">
  import { createEventDispatcher } from 'svelte';
	import type { RectangleDataType } from "$lib/models";

  const dispatch = createEventDispatcher();
	export let RectangleData: RectangleDataType;

  $: {
		RectangleData.left = window.innerWidth / 2 + RectangleData.x - RectangleData.width / 2;
		RectangleData.top = window.innerHeight / 2 + RectangleData.y - RectangleData.height / 2;
  }

	function rotate() {
		const temp = RectangleData.width;
		RectangleData.width = RectangleData.height;
		RectangleData.height = temp;

		dispatch('close');
	}

	function deleteRectangle() {
		dispatch('delete', RectangleData);
		dispatch('close');
	}

	function closeContextMenu() {
		dispatch('close');
	}

</script>

<div class="context-menu">
	<button on:click={rotate}>↺</button>
	<button on:click={deleteRectangle}>🗑</button>
	<button on:click={closeContextMenu}>✕</button>

  <form>
    <label for="width">Width:</label>
    <input type="number" id="width" bind:value={RectangleData.width} />

		<label for="height">Height:</label>
		<input type="number" id="height" bind:value={RectangleData.height} />

		<label for="x">X:</label>
		<input type="number" id="x" bind:value={RectangleData.x} />

		<label for="y">Y:</label>
		<input type="number" id="y" bind:value={RectangleData.y} />

		<label for="fillColor">Fill color:</label>
		<input type="text" id="fillColor" bind:value={RectangleData.fillColor} />
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

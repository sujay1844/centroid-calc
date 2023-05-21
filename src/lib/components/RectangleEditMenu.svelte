<script lang="ts">
  import { createEventDispatcher } from 'svelte';
	import type { RectangleDataType } from "$lib/models";
	import { onMount } from "svelte";

  const dispatch = createEventDispatcher();
	export let RectangleData: RectangleDataType;

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

	onMount(() => {
		window.addEventListener("resize", () => {
			closeContextMenu();
		});

		window.addEventListener("click", (event: MouseEvent) => {
			if (!event.target.closest(".context-menu")) {
			closeContextMenu();
		}
		});

		document.querySelector(".context-menu")?.addEventListener("click", (event: MouseEvent) => {
			event.stopPropagation();
		});

	});

</script>

<div class="context-menu">
	<button on:click={rotate}>↺</button>
	<button on:click={deleteRectangle}>🗑</button>
	<button on:click={closeContextMenu}>✕</button>

  <form>
    <label for="width">Width:</label>
    <input type="number" id="width" bind:value={RectangleData.width} />
	<input type="range" id="width-range" min=0 max=500 bind:value={RectangleData.width} /> {RectangleData.width}

	<label for="height">Height:</label>
	<input type="number" id="height" bind:value={RectangleData.height} />
	<input type="range" id="height-range" min=0 max=500 bind:value={RectangleData.height} /> {RectangleData.height}

	<label for="x">X:</label>
	<input type="number" id="x" bind:value={RectangleData.x} />
	<input type="range" id="x-range" min=-100 max=100 bind:value={RectangleData.x} /> {RectangleData.x}

	<label for="y">Y:</label>
	<input type="number" id="y" bind:value={RectangleData.y} />
	<input type="range" id="y-range" min=-100 max=100 bind:value={RectangleData.y} /> {RectangleData.y}

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

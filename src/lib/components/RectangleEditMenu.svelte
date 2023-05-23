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

		window.addEventListener("click", (event: Event) => {
			const target = event.target as HTMLElement;
			if (target == null || !target.closest(".context-menu")) {
				closeContextMenu();
			}
		});

		document.querySelector(".context-menu")?.addEventListener("click", (event: Event) => {
			event.stopPropagation();
		});

	});

</script>

<div class="context-menu">
	<button on:click={rotate}>↺ Rotate</button>
	<button on:click={deleteRectangle}>🗑 Delete</button>
	<button on:click={closeContextMenu}>✕</button>

  <form>
	<label for="isFilled">Filled:</label>
	<input type="checkbox" id="isFilled" bind:checked={RectangleData.isFilled} />
	<br>

    <label for="width">Width:</label>
    <input type="number" id="width" bind:value={RectangleData.width} />
	<input type="range" id="width-range" min=0 max=500 bind:value={RectangleData.width} /> {RectangleData.width}
	<br>

	<label for="height">Height:</label>
	<input type="number" id="height" bind:value={RectangleData.height} />
	<input type="range" id="height-range" min=0 max=500 bind:value={RectangleData.height} /> {RectangleData.height}
	<br>

	<label for="x">X:</label>
	<input type="number" id="x" bind:value={RectangleData.x} />
	<input type="range" id="x-range" min=-100 max=100 bind:value={RectangleData.x} /> {RectangleData.x}
	<br>

	<label for="y">Y:</label>
	<input type="number" id="y" bind:value={RectangleData.y} />
	<input type="range" id="y-range" min=-100 max=100 bind:value={RectangleData.y} /> {RectangleData.y}
	<br>

	<label for="fillColor">Fill color:</label>
	<input type="text" id="fillColor" bind:value={RectangleData.fillColor} />
	<br>

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

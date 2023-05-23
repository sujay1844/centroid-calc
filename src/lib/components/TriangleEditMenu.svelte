<script lang="ts">
	import type { TriangleDataType } from "$lib/models";
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
	import { onMount } from "svelte";
	
	export let TriangleData: TriangleDataType;

	function handleVerticalFlip() {
		TriangleData.flippedVertically = !TriangleData.flippedVertically;
	}
	function handleHorizontalFlip() {
		TriangleData.flippedHorizontally = !TriangleData.flippedHorizontally;
	}
	function handleDelete() {
		dispatch("delete", TriangleData);
		dispatch("close");
	}
	function closeContextMenu() {
		dispatch("close");
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

<section class="context-menu">
	<button on:click={handleVerticalFlip}>Flip Vertically</button>
	<button on:click={handleHorizontalFlip}>Flip Horizontally</button>
	<button on:click={handleDelete}>🗑 Delete</button>
	<button on:click={closeContextMenu}>✕</button>
	<form>
		<label for="isFilled">Filled:</label>
		<input type="checkbox" id="isFilled" bind:checked={TriangleData.isFilled} />
	<br>

		<label for="width">Width:</label>
		<input type="number" id="width" bind:value={TriangleData.width} />
		<input type="range" id="width-range" min=0 max=500 bind:value={TriangleData.width} /> {TriangleData.width}
	<br>

		<label for="height">Height:</label>
		<input type="number" id="height" bind:value={TriangleData.height} />
		<input type="range" id="height-range" min=0 max=500 bind:value={TriangleData.height} /> {TriangleData.height}
	<br>

		<label for="x">X:</label>
		<input type="number" id="x" bind:value={TriangleData.x} />
		<input type="range" id="x-range" min=-100 max=100 bind:value={TriangleData.x} /> {TriangleData.x}
	<br>

		<label for="y">Y:</label>
		<input type="number" id="y" bind:value={TriangleData.y} />
		<input type="range" id="y-range" min=-100 max=100 bind:value={TriangleData.y} /> {TriangleData.y}
	<br>

		<label for="fillColor">Fill color:</label>
		<input type="text" id="fillColor" bind:value={TriangleData.fillColor} />
	<br>

	</form>


</section>

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
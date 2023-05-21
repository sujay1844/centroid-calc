<script lang="ts">
  import { createEventDispatcher } from 'svelte';
	import type { CircleDataType } from "$lib/models";
	import { onMount } from "svelte";

  const dispatch = createEventDispatcher();
	export let CircleData: CircleDataType;

	function deleteCircle() {
		dispatch('delete', CircleData);
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
	<button on:click={deleteCircle}>🗑 Delete</button>
	<button on:click={closeContextMenu}>✕</button>

  <form>
    <label for="radius">Radius:</label>
    <input type="number" id="radius" bind:value={CircleData.radius} />
	<input type="range" id="radius-range" min=0 max=500 bind:value={CircleData.radius} /> {CircleData.radius}

		<label for="cx">X:</label>
		<input type="number" id="x" bind:value={CircleData.x} />
		<input type="range" id="x-range" min=-100 max=100 bind:value={CircleData.x} /> {CircleData.x}

		<label for="cy">Y:</label>
		<input type="number" id="y" bind:value={CircleData.y} />
		<input type="range" id="y-range" min=-100 max=100 bind:value={CircleData.y} /> {CircleData.y}

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

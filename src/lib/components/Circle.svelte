<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import type { CircleDataType } from "$lib/models";
  import { scalingFactor } from "$lib/store";
  import CircleEditMenu from "./CircleEditMenu.svelte";
  import { onMount } from "svelte";

  export let CircleData: CircleDataType;

  let moving = false;
  let showContextMenu = false;

  let left: number;
  let top: number;
	let radius: number;
  let zIndex: number = 1;
  $: {
		left = window.innerWidth / 2 + (CircleData.x - CircleData.radius) * $scalingFactor;
		top = window.innerHeight / 2 - (CircleData.y + CircleData.radius) * $scalingFactor;
		radius = CircleData.radius * $scalingFactor;
  }

  function onMouseDown() {
		if (!showContextMenu) {
			moving = true;
			zIndex = 999;
		}
  }

  function onMouseMove(event: MouseEvent) {
    if (moving) {
      CircleData.x += event.movementX / $scalingFactor;
      CircleData.y -= event.movementY / $scalingFactor;
    }
  }

  function onMouseUp() {
    moving = false;
		zIndex = 1;
  }

  function handleContextMenu(event: MouseEvent) {
    event.preventDefault();
    showContextMenu = !showContextMenu;
  }

  function deleteCircle() {
    dispatch("delete", CircleData);
  }

  onMount(() => {
    window.addEventListener("resize", () => {
      showContextMenu = false;
      moving = false;
			left = window.innerWidth / 2 + (CircleData.x - CircleData.radius) * $scalingFactor;
			top = window.innerHeight / 2 - (CircleData.y + CircleData.radius) * $scalingFactor;
    });
    window.addEventListener("mouseout", (event: MouseEvent) => {
      if (event.relatedTarget === null && moving) {
        moving = false;
        zIndex = 1;
      }
    });
  });

</script>

<style>
  .draggable {
    user-select: none;
    cursor: move;
    position: absolute;
	margin: 5px;
  }
  .context-menu {
    position: absolute;
    top: 50%;
    left: 50%;
    background-color: #fff;
    border: 1px solid #000;
  }
</style>

<section
  on:mousedown={onMouseDown}
  on:mouseup={onMouseUp}
  on:mousemove={onMouseMove}
  on:contextmenu={handleContextMenu}
  class="draggable"
  style="left:{left}px; top:{top}px; z-index:{zIndex};"
>
  {#if showContextMenu}
    <div class="context-menu">
      <CircleEditMenu
        on:delete={deleteCircle}
        on:close={()=> {showContextMenu = false;}}
        bind:CircleData={CircleData}
      />
    </div>
  {/if}

  <svg width="{radius * 2}" height="{radius *2}">
    <pattern id="diagonalPattern" patternUnits="userSpaceOnUse" width="20" height="20">
      <line x1="0" y1="0" x2="20" y2="20" stroke="red" stroke-width="1" />
    </pattern>
    <circle
      cx="{radius}"
      cy="{radius}"
      r="{radius}"
      style="fill:{CircleData.isFilled? CircleData.fillColor: 'url(#diagonalPattern)'}"
    />
  </svg>
</section>

<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import type { CircleDataType } from "$lib/models";
  import CircleEditMenu from "./CircleEditMenu.svelte";
  import { onMount } from "svelte";

  export let CircleData: CircleDataType;

  let moving = false;
  let showContextMenu = false;

  let left: number;
  let top: number;
  $: {
    left = window.innerWidth / 2 + CircleData.x - CircleData.radius;
    top = window.innerHeight / 2 + CircleData.y - CircleData.radius;
  }

  function onMouseDown() {
    moving = true;
  }

  function onMouseMove(event: MouseEvent) {
    if (moving) {
      CircleData.x += event.movementX;
      CircleData.y += event.movementY;
    }
  }

  function onMouseUp() {
    moving = false;
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
      left = window.innerWidth / 2 + CircleData.x - CircleData.radius;
      top = window.innerHeight / 2 + CircleData.y - CircleData.radius;
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
  style="left:{left}px;top:{top}px;"
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

  <svg width="{CircleData.radius * 2}" height="{CircleData.radius * 2}">
    <circle
      cx="{CircleData.radius}"
      cy="{CircleData.radius}"
      r="{CircleData.radius}"
      style="fill:{CircleData.fillColor};stroke-width:3;stroke:#000000"
    />
  </svg>
</section>

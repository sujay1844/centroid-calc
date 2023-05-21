<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import type { RectangleDataType } from "$lib/models";
  import RectangleEditMenu from "./RectangleEditMenu.svelte";
  import { onMount } from "svelte";

  export let RectangleData: RectangleDataType;

  let moving = false;
  let showContextMenu = false;

  let left: number;
  let top: number;
  let zIndex: number = 1;
  $: {
    left = window.innerWidth / 2 + RectangleData.x - RectangleData.width / 2;
    top = window.innerHeight / 2 + RectangleData.y - RectangleData.height / 2;
  }

  function onMouseDown() {
    moving = true;
    zIndex = 999;
  }

  function onMouseMove(event: MouseEvent) {
    if (moving) {
      RectangleData.x += event.movementX;
      RectangleData.y += event.movementY;
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

  function deleteRectangle() {
    dispatch("delete", RectangleData);
  }

  onMount(() => {
    window.addEventListener("resize", () => {
      showContextMenu = false;
      moving = false;
      left = window.innerWidth / 2 + RectangleData.x - RectangleData.width / 2;
      top = window.innerHeight / 2 + RectangleData.y - RectangleData.height / 2;
    });
  });

</script>

<style>
  .draggable {
    user-select: none;
    cursor: move;
    position: absolute;
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
      <RectangleEditMenu
        on:delete={deleteRectangle}
        on:close={()=> {showContextMenu = false;}}
        bind:RectangleData={RectangleData}
      />
    </div>
  {/if}

  <svg width="{RectangleData.width}" height="{RectangleData.height}">
    <rect
      width="{RectangleData.width}"
      height="{RectangleData.height}"
      style="fill:{RectangleData.fillColor};stroke-width:3;stroke:#000000"
    />
  </svg>
</section>

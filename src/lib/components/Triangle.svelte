<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import type { TriangleDataType } from "$lib/models";
  import { onMount } from "svelte";
  import TriangleEditMenu from './TriangleEditMenu.svelte';

	export let TriangleData: TriangleDataType;

  let moving = false;
  let showContextMenu = false;

  let left: number;
  let top: number;
  let width: number;
  let height: number;
  let zIndex: number = 1;
  export let scalingFactor: number = 1;
  $: {
    left = window.innerWidth / 2 + (TriangleData.x - TriangleData.width / 2) * scalingFactor;
    top = window.innerHeight / 2 - (TriangleData.y + TriangleData.height / 2) * scalingFactor;
    width = TriangleData.width * scalingFactor;
    height = TriangleData.height * scalingFactor;
  }

  function onMouseDown() {
    if (!showContextMenu) {
      moving = true;
      zIndex = 999;
    }
  }

  function onMouseMove(event: MouseEvent) {
    if (moving) {
      TriangleData.x += event.movementX / scalingFactor;
      TriangleData.y -= event.movementY / scalingFactor;
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

  function deleteTriangle() {
    dispatch("delete", TriangleData);
  }

  onMount(() => {
    window.addEventListener("resize", () => {
      showContextMenu = false;
      moving = false;
      left = window.innerWidth / 2 + (TriangleData.x - TriangleData.width / 2) * scalingFactor;
      top = window.innerHeight / 2 - (TriangleData.y + TriangleData.height / 2) * scalingFactor;
    });
    window.addEventListener("mouseout", (event: MouseEvent) => {
      if (moving) {
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
      <TriangleEditMenu
        on:delete={deleteTriangle}
        on:close={()=> {showContextMenu = false;}}
        bind:TriangleData={TriangleData}
      />
    </div>
  {/if}

    {#if TriangleData.flippedHorizontally && TriangleData.flippedVertically}

    <svg viewBox={`0 0 ${width} ${height}`} width={width} height={height}>
      <polygon
        points={`0,0 ${width},0 ${width},${height}`}
        style="fill:{TriangleData.fillColor};stroke-width:3;stroke:#000000"
      />
    </svg>

    {:else if TriangleData.flippedHorizontally}
    <svg viewBox={`0 0 ${width} ${height}`} width={width} height={height}>
      <polygon
        points={`0,0 ${width},0 0,${height}`}
        style="fill:{TriangleData.fillColor};stroke-width:3;stroke:#000000"
      />
    </svg>

    {:else if TriangleData.flippedVertically}
    <svg viewBox={`0 0 ${width} ${height}`} width={width} height={height}>
      <polygon
        points={`${width},0 ${width},${height} 0,${height}`}
        style="fill:{TriangleData.fillColor};stroke-width:3;stroke:#000000"
      />
    </svg>
    {:else}
    <svg viewBox={`0 0 ${width} ${height}`} width={width} height={height}>
      <polygon
        points={`0,0 0,${height} ${width},${height}`}
        style="fill:{TriangleData.fillColor};stroke-width:3;stroke:#000000"
      />
    </svg>
    {/if}

</section>
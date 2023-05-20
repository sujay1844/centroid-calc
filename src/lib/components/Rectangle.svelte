<script lang="ts">
  import type { RectangleDataType } from "$lib/models";

  export let RectangleData: RectangleDataType;

  let moving = false;
  let showContextMenu = false;

  function onMouseDown() {
    moving = true;
  }

  function onMouseMove(event: MouseEvent) {
    if (moving) {
      RectangleData.left += event.movementX;
      RectangleData.top += event.movementY;
    }
  }

  function onMouseUp() {
    moving = false;
  }

  function handleContextMenu(event: MouseEvent) {
    event.preventDefault();
    showContextMenu = !showContextMenu;
  }

  function rotate() {
    const temp = RectangleData.width;
    RectangleData.width = RectangleData.height;
    RectangleData.height = temp;

    showContextMenu = false;
  }

  function deleteRectangle() {
    RectangleData.deleted = true;
    showContextMenu = false;
  }
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
  style="left: {RectangleData.left}px; top: {RectangleData.top}px;"
  class="draggable"
>
  {#if showContextMenu}
    <div class="context-menu">
      <button on:click={rotate}>Rotate</button>
      <button on:click={deleteRectangle}>Delete</button>
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

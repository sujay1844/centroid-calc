<script lang="ts">
  import { onMount } from "svelte";

  import Rectangle from "$lib/components/Rectangle.svelte";
  import type { RectangleDataType } from "$lib/models";


  let rectangles: RectangleDataType[] = [];

  function createRandomRectangle(): void {
    const width: number = getRandomNumber(100, 400);
    const height: number = getRandomNumber(100, 400);
    const left: number = getRandomNumber(0, window.innerWidth - width);
    const top: number = getRandomNumber(0, window.innerHeight - height);
    const fillColor: string = getRandomColor();

    rectangles = [
      ...rectangles,
      {
        width: width,
        height: height,
        left: left,
        top: top,
        x: left - window.innerWidth / 2 + width / 2,
        y: top - window.innerHeight / 2 + height / 2,
        fillColor: fillColor,
      }
    ];
  }

  function getRandomNumber(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

  function getRandomColor(): string {
    const letters: string = "0123456789ABCDEF";
    let color: string = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function handleDelete(event: CustomEvent): void {
    const rectangle: RectangleDataType = event.detail;
    rectangles = rectangles.filter((r: RectangleDataType) => r !== rectangle);
  }

</script>

<style>
  .x-axis, .y-axis {
  position: absolute;
  background-color: #000;
}

.x-axis {
  top: 50%;
  left: 0;
  width: 100%;
  height: 1px;
}

.y-axis {
  top: 0;
  left: 50%;
  width: 1px;
  height: 100%;
}
</style>

<section>
  <div class="x-axis"></div>
  <div class="y-axis"></div>
  <h1>Generate rectangles
  <button on:click={createRandomRectangle}>+</button>
  </h1>
  {#each rectangles as rectangle}
    <Rectangle
    bind:RectangleData={rectangle}
    on:delete={handleDelete}
    />
  {/each}
</section>

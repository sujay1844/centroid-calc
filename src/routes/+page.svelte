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
        fillColor: fillColor,
        deleted: false,
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

  onMount((): void => {
    createRandomRectangle();
  });

  $: {
    rectangles = rectangles.filter((rectangle: RectangleDataType) => {
      return !rectangle.deleted;
    });
  }
</script>

<section>
  <h1>Generate rectangles
  <button on:click={createRandomRectangle}>+</button>
  </h1>
  {#each rectangles as rectangle}
    <Rectangle
    bind:RectangleData={rectangle}
    />
  {/each}
</section>

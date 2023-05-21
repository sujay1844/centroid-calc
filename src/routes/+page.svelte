<script lang="ts">
  import { onMount } from "svelte";

  import Rectangle from "$lib/components/Rectangle.svelte";
  import Circle from "$lib/components/Circle.svelte";
  import GithubLink from "$lib/components/GithubLink.svelte";
  import type { RectangleDataType, CircleDataType } from "$lib/models";

  let scalingFactor: number = 1;

  let rectangles: RectangleDataType[] = [];
  let circles: CircleDataType[] = [];

  let centroid: { x: number; y: number } = { x: 0, y: 0 };

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
        x: left - window.innerWidth / 2 + width / 2,
        y: top - window.innerHeight / 2 + height / 2,
        fillColor: fillColor,
      }
    ];
  }

  function createRandomCircle(): void {
    const radius: number = getRandomNumber(50, 200);
    const left: number = getRandomNumber(0, window.innerWidth - radius);
    const top: number = getRandomNumber(0, window.innerHeight - radius);
    const fillColor: string = getRandomColor();

    circles = [
      ...circles,
      {
        radius: radius,
        x: left - window.innerWidth / 2 + radius / 2,
        y: top - window.innerHeight / 2 + radius / 2,
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

  function handleDeleteRectangle(event: CustomEvent): void {
    const rectangle: RectangleDataType = event.detail;
    rectangles = rectangles.filter((r: RectangleDataType) => r !== rectangle);
  }

  function handleDeleteCircle(event: CustomEvent): void {
    const circle: CircleDataType = event.detail;
    circles = circles.filter((c: CircleDataType) => c !== circle);
  }

  onMount(() => {
    window.addEventListener("wheel", (event: WheelEvent) => {
      if (event.ctrlKey) {
        event.preventDefault();
        scalingFactor += event.deltaY * -0.01;
      }
    });
  });

  function getCentroid(): { x: number; y: number } {
    const areas: number[] = [];
    const centroids: { x: number; y: number }[] = [];
    rectangles.forEach(rectangle => {
      const area: number = rectangle.width * rectangle.height;
      const centroid: { x: number; y: number } = {
        x: rectangle.x,
        y: rectangle.y,
      };
      areas.push(area);
      centroids.push(centroid);
    });
    circles.forEach(circle => {
      const area: number = Math.PI * circle.radius * circle.radius;
      const centroid: { x: number; y: number } = {
        x: circle.x,
        y: circle.y,
      };
      areas.push(area);
      centroids.push(centroid);
    });
    console.log(areas);
    console.log(centroids);

    const totalArea: number = areas.reduce((a, b) => a + b, 0);
    const x: number = centroids.reduce(
      (currentCentroid, nextCentroid, i) => currentCentroid + nextCentroid.x * areas[i] / totalArea,
      0
    );
    const y: number = centroids.reduce(
      (currentCentroid, nextCentroid, i) => currentCentroid + nextCentroid.y * areas[i] / totalArea,
      0
    );
    return { x: x, y: y };
  }
  function updateCentroid(): void {
    centroid = getCentroid();
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
  <h1>Generate Shapes
  <button on:click={createRandomRectangle}>+ Rectangle</button>
  <button on:click={createRandomCircle}>+ Circle</button>
  </h1>
  <p>Click and drag to move shapes</p>
  <p>Right click to edit them</p>
  <button on:click={updateCentroid}>Calculate Centroid</button>
  <h1>Centroid = ({centroid.x}, {centroid.y})</h1>
  <GithubLink />

  {#each rectangles as rectangle}
    <Rectangle
    bind:RectangleData={rectangle}
    bind:scalingFactor={scalingFactor}
    on:delete={handleDeleteRectangle}
    />
  {/each}
  {#each circles as circle}
    <Circle
    bind:CircleData={circle}
    bind:scalingFactor={scalingFactor}
    on:delete={handleDeleteCircle}
    />
  {/each}
  


</section>

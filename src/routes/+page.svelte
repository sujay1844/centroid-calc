<script lang="ts">
	import { onMount } from "svelte";
	import { scalingFactor } from "$lib/store";

	import Rectangle from "$lib/components/Rectangle.svelte";
	import Circle from "$lib/components/Circle.svelte";
	import Triangle from "$lib/components/Triangle.svelte";
	import GithubLink from "$lib/components/GithubLink.svelte";
	import type { RectangleDataType, CircleDataType, TriangleDataType, Point } from "$lib/models";
	import { readable } from "svelte/store";

	let rectangles: RectangleDataType[] = [];
	let circles: CircleDataType[] = [];
	let triangles: TriangleDataType[] = [];

	let centroid: Point = { x: 0, y: 0 };

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
				isFilled: true,
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
				isFilled: true,
			}
		];
	}

	function createRandomTriangle(): void {
		const width: number = getRandomNumber(100, 400);
		const height: number = getRandomNumber(100, 400);
		const left: number = getRandomNumber(0, window.innerWidth - width);
		const top: number = getRandomNumber(0, window.innerHeight - height);
		const fillColor: string = getRandomColor();

		triangles = [
			...triangles,
			{
				width: width,
				height: height,
				x: left - window.innerWidth / 2 + width / 2,
				y: top - window.innerHeight / 2 + height / 2,
				fillColor: fillColor,
				flippedHorizontally: false,
				flippedVertically: false,
				isFilled: true,
			}
		];
		console.log(triangles);
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
	function handleDeleteTriangle(event: CustomEvent): void {
		const triangle: TriangleDataType = event.detail;
		triangles = triangles.filter((t: TriangleDataType) => t !== triangle);
	}

	onMount(() => {
		window.addEventListener("wheel", (event: WheelEvent) => {
			if (event.ctrlKey) {
				event.preventDefault();
				$scalingFactor += event.deltaY * -0.01;
			}
		});
	});

	function getCentroid(): { x: number; y: number } {
		const areas: number[] = [];
		const centroids: { x: number; y: number }[] = [];
		rectangles.forEach(rectangle => {
			const area: number = rectangle.width * rectangle.height * (rectangle.isFilled ? 1 : -1);
			const centroid: { x: number; y: number } = {
				x: rectangle.x,
				y: rectangle.y,
			};
			areas.push(area);
			centroids.push(centroid);
		});
		circles.forEach(circle => {
			const area: number = Math.PI * circle.radius * circle.radius * (circle.isFilled ? 1 : -1);
			const centroid: { x: number; y: number } = {
				x: circle.x,
				y: circle.y,
			};
			areas.push(area);
			centroids.push(centroid);
		});
		triangles.forEach(triangle => {
			const area: number = triangle.width * triangle.height / 2 * (triangle.isFilled ? 1 : -1);
			const centroid: { x: number; y: number } = {
				x: triangle.x,
				y: triangle.y,
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
	.x-axis,
	.y-axis {
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

	button {
		border-radius: 5px;
		background-color: #222;
		color: white;
		/* height: 20px; */
		font-size: 15px;
		padding: 5px 10px;
	}
</style>

<section>
	<div class="x-axis"></div>
	<div class="y-axis"></div>
	<h1>Generate Shapes</h1>
		
	<button on:click={createRandomRectangle}>+ Rectangle</button>&emsp;&emsp;
	<button on:click={createRandomCircle}>+ Circle</button>&emsp;&emsp;
	<button on:click={createRandomTriangle}>+ Triangle</button>&emsp;&emsp;
	
	<p>Click and drag to move shapes</p>
	<p>Right click to edit them</p>
	<button on:click={updateCentroid}>Calculate Centroid</button>
	<h1>Centroid = ({centroid.x}, {centroid.y})</h1>
	<GithubLink />

	{#each rectangles as rectangle}
	<Rectangle bind:RectangleData={rectangle} on:delete={handleDeleteRectangle} />
	{/each}
	{#each circles as circle}
	<Circle bind:CircleData={circle} on:delete={handleDeleteCircle} />
	{/each}
	{#each triangles as triangle}
	<Triangle bind:TriangleData={triangle} on:delete={handleDeleteTriangle} />
	{/each}



</section>
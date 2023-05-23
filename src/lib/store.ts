import { writable } from "svelte/store";
import type { Point } from "$lib/models";

export const scalingFactor = writable(1);

export const origin = writable<Point>({
	x: 0,
	y: 0
});
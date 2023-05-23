export interface Point {
	x: number;
	y: number;
}

export interface RectangleDataType {
	width: number;
	height: number;
	x: number;
	y: number;
	fillColor: string;
}

export interface CircleDataType {
	radius: number;
	x: number;
	y: number;
	fillColor: string;
}

export interface TriangleDataType {
	width: number;
	height: number;
	x: number;
	y: number;
	flippedVertically: boolean;
	flippedHorizontally: boolean;
	fillColor: string;
}
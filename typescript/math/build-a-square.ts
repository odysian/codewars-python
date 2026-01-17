// https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/typescript

// For loop
export function generateShape(n: number): string {
  // Init empty string array
  let rows: string[] = [];
  // Explicit for loop
  for (let i = 0; i < n; i++) {
    // .repeat(n) works like "+" * n
    let row: string = "+".repeat(n);
    // .push() == .append()
    rows.push(row)
  }
  // Join together on newline
  return rows.join("\n")
}

// One liner
export function generateShape1(n: number): string {
  // 1. Create an Array of size n
  // 2. Fill it (required so we can map over it)
  // 3. Map each item to a row of +++
  // 4. Join them with newlines
  return Array(n).fill("+".repeat(n)).join("\n");
}
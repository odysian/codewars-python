// For loop
export const vaporcode = (str: string ): string => {
  let words: string[] = [];
  for (let s of str) {
    if (s !== " ") {
      words.push(s.toUpperCase());
    }
  };
  return words.join("  ");
}

// One liner
export const vaporcode1 = (str: string ): string => {
  return str
    .toUpperCase()
    .split(" ")
    .join("")
    .split("")
    .join("  ")
}
// https://www.codewars.com/kata/57873ab5e55533a2890000c7/train/typescript

export const timeCorrect = (timestring: string | null): string | null => {
  // Validation
  if (!timestring || timestring === "") return timestring;
  const parts = timestring.split(":");
  if (parts.length !== 3) return null;
  for (const part of parts) {
    if (part.length !== 2) return null;
    if (isNaN(Number(part))) return null;
  }
  // Map to numbers
  let [h, m, s] = parts.map(Number);
  // Check values starting with seconds, floor and add
  if (s >= 60) {
    m += Math.floor(s / 60);
    s = s % 60;
  } 
  if (m >= 60) {
    h += Math.floor(m / 60);
    m = m % 60;
  }
  
  h = h % 24;
  // Helper to pad numbers with 0 if below 10
  const pad = (n: number) => {
    if (n < 10) return "0" + n;
    return String(n)
  }

  return `${pad(h)}:${pad(m)}:${pad(s)}`
}
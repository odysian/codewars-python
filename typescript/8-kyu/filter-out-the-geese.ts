// https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/typescript

export const gooseFilter = (birds: string[]): string[] => {
  const geese: string[] = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
  // Use filter!
  return birds.filter(bird => !geese.includes(bird));
}
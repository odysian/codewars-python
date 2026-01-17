// https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/typescript

export const sumArray = (array:number[] | null) : number  => {
  // Validation
  if (!array || array.length < 2) {
    return 0;
  }
  // Reduce array to sum all numbers
  const total = array.reduce((acc, curr) => acc + curr, 0)
  // Find min and max
  const min = Math.min(...array);
  const max = Math.max(...array);
  // Subtract them from the total
  return total - min - max;
}
// https://www.codewars.com/kata/580a4734d6df748060000045/train/typescript


// Initial attempt: Counter pattern
export function isSortedAndHow(array: number[]): string {
  let asc_count: number = 1
  let desc_count: number = 1

  for (let i = 0; i < array.length - 1; i++) {
    const current = array[i]!;
    const next = array[i+1]!;
    if (current <= next){
      asc_count++
    } 
    if (current >= next) {
      desc_count++
    }
  }

  if (asc_count === array.length) {
    return "yes, ascending"
  } else if (desc_count === array.length) {
    return "yes, descending"
  } else {
    return "no"
  }
}

// Smarter approach: Flag pattern 
export function isSortedAndHow1(array: number[]): string {
  let ascending: boolean = true;
  let descending: boolean = true;

  for (let i = 0; i < array.length - 1; i++) {
    const current = array[i]!;
    const next = array[i+1]!;

    if (current > next){
      ascending = false;
    } 
    if (current < next) {
      descending = false;
    }
    if (!ascending && !descending) {
      return "no";
    }
  }

  if (ascending) return "yes, ascending";
  if (descending) return "yes, descending";
  return "no";
}
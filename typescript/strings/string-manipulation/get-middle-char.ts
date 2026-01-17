// https://www.codewars.com/kata/56747fd5cb988479af000028/train/typescript

export function getMiddle1(s:string) {
  if (!s) return '';
  let mid = Math.floor(s.length / 2);
  if (s.length % 2 == 0) {
    return s[mid-1] + s[mid];
  } else {
    return s[mid];
  }
}

export const getMiddle = (s:string) => {
  if (!s) return '';
  let mid = Math.floor(s.length / 2);
  return s.length % 2 == 0
    ? s[mid-1] + s[mid]
    : s[mid];
}
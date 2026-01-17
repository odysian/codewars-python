// https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/typescript

// Split, reverse, join, compare
export function isPalindrome(x: string): boolean {
  const normal = x.toLowerCase();
  const reversed = normal.split('').reverse().join('');
  
  return normal === reversed;
}
// Two pointers
export function isPalindrome1(x: string): boolean {
  const str = x.toLowerCase();
  
  let left = 0;
  // No index [-1] like python, use .length -1
  let right = str.length - 1;
  
  while (left < right) {
    if (str[left] !== str[right]) {
      return false;
    }
    // ++ and -- instead of += 1  
    left++;
    right--;
  }
  return true;
}
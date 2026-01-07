// https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/typescript


// Works for any braces, just add to dict
export function validParentheses(parenStr: string): boolean {
  let pairs: Record<string, string> = {
    ")": "("
  }
  let stack: string[] = []
  
  for (const p of parenStr) {
    if (p in pairs) {
      if (!stack || stack.at(-1) !== pairs[p])
      return false;
    stack.pop()
    }
    
    else {
      stack.push(p);
    }
  }
  
  return stack.length === 0;
}

// Just for parentheses
export const validParentheses1 = (parenStr: string): boolean => {
  let depth = 0;

  for (const p of parenStr) {
    if (p === "(") depth++;
    if (p === ")") depth--;

    if (depth < 0) return false;
  }
  
  return depth === 0;
}
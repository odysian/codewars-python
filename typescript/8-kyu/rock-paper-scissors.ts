// https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/typescript

export function rps(p1: string, p2: string): string{
  if (p1 === p2) return "Draw!";
  // Hashmap for p1 winning moves
  const rules: Record<string, string> = {
    rock: "scissors",
    scissors: "paper",
    paper: "rock"
  };
  // If found, p1 wins, if not p2
  if (rules[p1] === p2) {
    return "Player 1 won!"    
  } else {
    return "Player 2 won!"
  }
}
// Solution with custom type
type Move = "rock" | "paper" | "scissors";
// Outside codewars we'd make p1/p2 Move type
export function rps1(p1: string, p2: string): string{
  
  if (p1 === p2) return "Draw!";
  // Map uses Move type
  const rules: Record<Move, Move> = {
    rock: "scissors",
    scissors: "paper",
    paper: "rock"
  };
  // Codewars testing didnt like me changing param to Move type
  // So we type assert p1 as Move here
  if (rules[p1 as Move] === p2) {
    return "Player 1 won!"    
  } else {
    return "Player 2 won!"
  }
}
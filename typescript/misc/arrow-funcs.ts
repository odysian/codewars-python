// 1
export const isPositive = (n:number): boolean => n > 0;

// 2
const numbers: number[] = [1,2,3,4,5];

export const squared = (numbers: number[]): number[] =>
  numbers.map(n => n ** 2);

// 3
interface User {
  name: string;
  age: number;
}

const users: User[] = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 17 },
  { name: "Charlie", age: 30 }
];

export const filterUser = (users: User[]): User[] =>
  users.filter(u => u.age >= 18);


// 4
interface Task {
  id: number;
  title: string;
  completed: boolean;
}

const tasks: Task[] = [
  { id: 1, title: "Learn TS", completed: true },
  { id: 2, title: "Build project", completed: false },
  { id: 3, title: "Deploy", completed: false }
];

export const complexTrans = (tasks: Task[]): string[] =>
  tasks.filter(t => !t.completed).map(t => t.title);

// Take an array, return a transformed array
// const functionName = (input: InputType[]): OutputType[] => 
//   input.arrayMethod(item => transformation);

// Map tasks to components
// {tasks.map(task => <TaskCard key={task.id} task={task} />)}

// Filter and display
// {tasks.filter(t => !t.completed).map(t => <div>{t.title}</div>)}

// Transform data
// const userNames = users.map(u => u.name);
// https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/typescript

export class Kata {
    public static bonusTime(salary:number, bonus:boolean):string {
      if (bonus) {
        // Concat string to a number converts result to string
        // To convert otherwise use .toString() or String()
        return "£" + (salary * 10);
      } else {
        return "£" + salary;
      }
    }
}
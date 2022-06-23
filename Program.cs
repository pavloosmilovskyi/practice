using System;
using System.Collections.Generic;

namespace talon
{
    class Tasks
    {
        public bool checkAnagram(string firstW, string secondW)
        {
            Dictionary<char, int> firstWD = new Dictionary<char, int>();
            Dictionary<char, int> secondWD = new Dictionary<char, int>();
            for (int i = 0; i < firstW.Length; i++)
            {
                if (firstWD.ContainsKey(firstW[i]))
                {
                    firstWD[firstW[i]] = firstWD[firstW[i]] + 1;
                }
                else
                {
                    firstWD[firstW[i]] = 1;
                }
            }
            for (int i = 0; i < secondW.Length; i++)
            {
                if (secondWD.ContainsKey(secondW[i]))
                {
                    secondWD[secondW[i]] = secondWD[secondW[i]] + 1;
                }
                else
                {
                    secondWD[secondW[i]] = 1;
                }
            }
            foreach (char el in secondWD.Keys)
            {
                if (firstWD.ContainsKey(el) && secondWD.ContainsKey(el))
                {
                    if (firstWD[el] >= secondWD[el])
                        continue;
                    else
                        return false;
                }
                else
                    return false;
            }
            return true;
        }
        public T[] mergeSort<T>(T[] array)
        {
            T[] left;
            T[] right;
            T[] result = new T[array.Length];
            if (array.Length <= 1)
                return array;
            int midPoint = array.Length / 2;
            left = new T[midPoint];
            if (array.Length % 2 == 0)
                right = new T[midPoint];
            else
                right = new T[midPoint + 1];
            for (int i = 0; i < midPoint; i++)
                left[i] = array[i];
            int x = 0;
            for (int i = midPoint; i < array.Length; i++)
            {
                right[x] = array[i];
                x++;
            }
            left = mergeSort(left);
            right = mergeSort(right);
            Array.Copy(right, result, right.Length);
            Array.Copy(left, 0, result, right.Length, left.Length);
            return result;
        }
        public List<int> Series(List<int> list)
        {
            List<int> resultList = new List<int>();
            List<int> seriesList = new List<int>();
            for (int i = 0; i < list.Count; i++)
            {
                if (i == list.Count - 1)
                {
                    seriesList.Add(list[i]);
                    seriesList.Reverse();
                    resultList.AddRange(seriesList);
                }
                else
                {
                    if (list[i] > 0 && list[i + 1] < 0 || list[i] < 0 && list[i + 1] > 0)
                    {
                        seriesList.Add(list[i]);
                        Console.WriteLine(list[i]);
                    }
                    else
                    {
                        seriesList.Add(list[i]);
                        seriesList.Reverse();
                        resultList.AddRange(seriesList);
                        seriesList.Clear();
                    }
                }
            }
            return resultList;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Tasks tasks = new Tasks();
            //перше слово головне, друге - його анаграма або ні
            Console.WriteLine(tasks.checkAnagram("coala", "cola"));
            Console.WriteLine(tasks.checkAnagram("coala", "mopse"));
            //сортування масиву 
            string[] array = new string[] { "test", "Test", "complex", "alfa" };
            foreach (string el in tasks.mergeSort<string>(array))
            {
                Console.Write($"{el} ");
            }
            Console.WriteLine();
            //Пошук серій елементів та обернення їх
            List<int> newList = tasks.Series(new List<int>() { 1, 2, -2, 3, -5, -5, -7, 1, -4 });
            foreach (int el in newList)
            {
                Console.Write($"{el} ");
            }
            Console.ReadLine();
        }
    }
}
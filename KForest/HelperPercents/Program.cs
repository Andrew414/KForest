using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace HelperPercents
{
    class Program
    {
        static void Main(string[] args)
        {

            double prob = 0.1;
            StreamReader read = new StreamReader("test.csv");

            Random rand = new Random(DateTime.Now.Millisecond);

            StreamWriter write = new StreamWriter("test2.csv");
            write.WriteLine(read.ReadLine());

            while (!read.EndOfStream)
            {
                string s = read.ReadLine();
                if (rand.NextDouble() < 0.1)
                {
                    write.WriteLine(s);
                }
            }

            write.Close();
            read.Close();
        }
    }
}

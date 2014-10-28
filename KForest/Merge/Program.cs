using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Merge
{
    class Program
    {
        static void Main(string[] args)
        {
            string test = args[0];
            string ans = args[1];
            string final = args[2];

            StreamReader rt = new StreamReader(test);
            StreamReader ra = new StreamReader(ans);

            StreamWriter rf = new StreamWriter(final);

            while (!rt.EndOfStream)
            {
                string s1 = rt.ReadLine();
                string s2 = ra.ReadLine();

                rf.WriteLine(s1.Split(new char[]{','})[0] + "," + s2);
            }

            rf.Close();
            rt.Close();
            ra.Close();
        }
    }
}

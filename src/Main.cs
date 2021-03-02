using System;

namespace AleksBot{
class MainFile{

static void Main(){
Console.WriteLine("If you have not already made an account please make one at http://aleksbot.cf/register");
Console.WriteLine("Please enter your username and press enter when done.");
string username = Console.ReadLine();
Console.WriteLine("Please enter your password and press enter when done");
string password = Console.ReadLine();
Console.WriteLine("aaa");
Console.ReadLine();
Login.Auth(username,password);
Console.ReadLine();


}
}
}

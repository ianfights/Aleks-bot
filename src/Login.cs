using System;
using System.Net.Http;
using System.Collections.Generic;


  public class Login{


    public static async void Auth(string username, string password){
    var client = new HttpClient();
    Console.WriteLine("In function");
    var values = new Dictionary<string, string>{
    	{ "username", username },
    	{ "password", password }
		};

var content = new FormUrlEncodedContent(values);
var response = await client.PostAsync("http://aleksbot.cf/backend/login.php", content);
//Console.WriteLine(response.Content.ToString());
//Console.WriteLine(response.StatusCode.ToString());
var responseString = await response.Content.ReadAsStringAsync();
Console.WriteLine(responseString);

    }


    
  
}

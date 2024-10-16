using System;
using System.IO;
using Newtonsoft.Json.Linq;

class Program
{
	static void Main(string[] args)
	{
		if (args.Length == 0)
		{
			Console.WriteLine("Please drag a JSON file onto this program.");
			return;
		}

		string filePath = args[0];
		if (!File.Exists(filePath))
		{
			Console.WriteLine("File not found: " + filePath);
			return;
		}

		try
		{
			string jsonContent = File.ReadAllText(filePath);
			JToken root = JToken.Parse(jsonContent);

			// Recursively find and print MorphTarget names
			FindMorphTargets(root);
		}
		catch (Exception ex)
		{
			Console.WriteLine("An error occurred: " + ex.Message);
		}

		Console.WriteLine("Press any key to exit...");
		Console.ReadKey();
	}

	static void FindMorphTargets(JToken token)
	{
		if (token.Type == JTokenType.Object)
		{
			JObject obj = (JObject)token;
			JToken typeToken = obj["Type"];
			JToken nameToken = obj["Name"];

			if (typeToken != null && typeToken.ToString() == "MorphTarget" && nameToken != null)
			{
				Console.WriteLine(nameToken.ToString());
			}

			foreach (JProperty property in obj.Properties())
			{
				FindMorphTargets(property.Value);
			}
		}
		else if (token.Type == JTokenType.Array)
		{
			foreach (JToken item in token)
			{
				FindMorphTargets(item);
			}
		}
	}
}
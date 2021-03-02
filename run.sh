mcs -out:Main.exe /reference:System.Net.Http.dll ./src/*.cs 
mono Main.exe